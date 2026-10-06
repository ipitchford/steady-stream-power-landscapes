#!/usr/bin/env python3
"""Exact symbolic identities and independent profile quadratures.
These checks are not a formal verification of any PDE existence theorem.
Run: python code/verify_structural.py
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import sympy as sp

def require(condition, message):
    """A release check that remains active with Python optimization."""
    if not condition:
        raise AssertionError(message)


ROOT = Path(__file__).resolve().parents[1]


def symbolic() -> dict:
    r, d, n = sp.symbols('r d n', positive=True)
    rho = r
    profiles = [(1, (1-sp.exp(-rho**d/d))/rho**(d-1)),
                (2, sp.tanh(rho**d/d)/rho**(d-1))]
    results = {}
    for exponent, y in profiles:
        m = exponent*(d-1)
        residual = sp.diff(y,rho)+(d-1)*y/rho+rho**m*y**exponent-1
        residual = sp.simplify(sp.expand_power_base(residual,force=True))
        require(residual == 0, residual)
        results[f'integrable_radial_n{exponent}_residual'] = str(residual)
    # The critical-set criterion: linearized flux derivative at a critical point.
    b, h11, h12, h22, x, y = sp.symbols('b h11 h12 h22 x y')
    flux = -b*sp.Matrix([[h11,h12],[h12,h22]])*sp.Matrix([x,y])
    div = sp.diff(flux[0],x)+sp.diff(flux[1],y)
    require(sp.expand(div+b*(h11+h22)) == 0, 'Verification failed: verify_structural.py:33')
    results['critical_flux_divergence'] = str(div)
    # Front viscosity inequality, using V = -beta-alpha.
    alpha, theta, beta = sp.symbols('alpha theta beta',real=True)
    V = -beta-alpha
    F = -theta*alpha*V-(theta*alpha)**2-beta*theta*alpha
    require(sp.expand(F-alpha**2*theta*(1-theta)) == 0, 'Verification failed: verify_structural.py:39')
    results['front_viscosity_polynomial'] = str(sp.factor(F))
    # Corrected channel profile at c=0: verify a physical m=3/2 member exactly.
    xx=sp.symbols('x',real=True)
    m=sp.Rational(3,2)
    A0=(2*m/(m*m-1))**(m/(m-1))
    w=A0*sp.cos(xx/6)**6
    # On the interior cos(x/6)>0, w^(1/m)=A0^(2/3)*cos^4.
    residual=sp.trigsimp(sp.diff(w,xx,2)+w-2*A0**sp.Rational(2,3)*sp.cos(xx/6)**4)
    require(residual == 0, residual)
    results['channel_zero_flux_m_3over2_residual']=str(residual)
    # Generic time-dependent scale requirements.
    B=sp.symbols('B',positive=True); mm=sp.symbols('m',positive=True)
    A=B**(-1/mm); tauprime=A**(mm-1)*B**2; lam=B**2
    for expression in (A**(mm-1)*B**2/tauprime-1,
                       lam*A**(mm-1)/tauprime-1,
                       B/(A*tauprime)-1):
        require(sp.simplify(expression)==0, 'Verification failed: verify_structural.py:56')
    results['normalizing_scale_relations']='PASS; derivative terms are retained in the analytical equation'
    return {'status':'PASS','identities':results}


def profile_quad(m: float, c: float) -> dict:
    if m<=1 or c<=0:
        raise ValueError('The repaired positive profile requires m>1 and c>0')
    power=(m+1)/m; coeff=m/((m-1)*(m+1))
    A0=(2*coeff)**(1/(2-power))
    energy=lambda A:A*A-2*coeff*A**power-c*c
    hi=max(2*A0,2*c)
    while energy(hi)<=0:
        hi*=2
    A=brentq(energy,A0,hi,xtol=1e-13,rtol=1e-14)
    eta=2*coeff*A**(power-2)
    # t=1-v^2 removes the square-root singularity at the maximum (v=0).
    def weight(v: float)->float:
        if v==0:
            return 2/np.sqrt(2-eta*power)
        t=1-v*v
        one_minus_power=-np.expm1(power*np.log1p(-v*v)) if v<1 else 1.0
        den=v*v*(2-v*v)-eta*one_minus_power
        if den<=0:
            raise ArithmeticError('Nonpositive quadrature denominator')
        return 2*v/np.sqrt(den)
    def integral(q:float)->float:
        val,err=quad(lambda v:A**q*(1-v*v)**q*weight(v),0,1,
                     epsabs=2e-10,epsrel=2e-11,limit=250)
        return val
    L=integral(0); mass=integral(1); rootmass=integral(1/m)
    residual=mass-c-rootmass/(m-1)
    require(np.pi/2<L<np.pi*m/(m-1), 'Verification failed: verify_structural.py:88')
    require(mass>c, 'Verification failed: verify_structural.py:89')
    require(abs(residual)<1e-7*max(1,mass), 'Verification failed: verify_structural.py:90')
    return {'m':m,'edge_flux':c,'amplitude':A,'width':L,
            'integral_w':mass,'integral_w_to_1_over_m':rootmass,
            'corrected_mass_identity_residual':residual}


def main()->None:
    records=[profile_quad(m,c) for m in [1.5,2.0,3.0] for c in [0.1,1.0,10.0]]
    for m in [1.5,2.0,3.0]:
        widths=[v['width'] for v in records if v['m']==m]
        require(widths[0]>widths[1]>widths[2], 'Verification failed: verify_structural.py:100')
    report={'symbolic':symbolic(),'corrected_channel_profile':{'status':'PASS','cases':records},
            'warning':'Symbolic identities and floating-point quadratures only; not proof-assistant or interval certificates.'}
    path=ROOT/'results'/'structural_checks.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
