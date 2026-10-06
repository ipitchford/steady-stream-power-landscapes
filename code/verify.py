#!/usr/bin/env python3
"""Reproducible algebraic and numerical checks, not a formal PDE proof.
Run from any directory: python code/verify.py
Requires Python 3.10+, numpy, scipy, sympy. Writes results/checks.json.
"""
from __future__ import annotations
import hashlib, json, platform, time
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp, quad
import sympy as sp

def require(condition, message):
    """A release check that remains active with Python optimization."""
    if not condition:
        raise AssertionError(message)


ROOT = Path(__file__).resolve().parents[1]


def algebra_checks() -> dict:
    x, y, lam = sp.symbols('x y lam', real=True)
    T = sp.Rational(2,5)-x*x/10-2*y*y/5
    G = (x*x+16*y*y)/25
    W = (1-x*x/4-y*y)*(44+3*x*x+52*y*y)/1025
    B1 = x*x/35+16*y*y/65
    grad = lambda f: sp.Matrix([sp.diff(f,x),sp.diff(f,y)])
    div = lambda q: sp.diff(q[0],x)+sp.diff(q[1],y)
    lap = lambda f: div(grad(f))
    require(sp.expand(-lap(T)-1) == 0, 'Verification failed: verify.py:26')
    require(sp.expand(-lap(W)-G) == 0, 'Verification failed: verify.py:27')
    require(sp.expand(-grad(T).dot(grad(B1))+B1-G) == 0, 'Verification failed: verify.py:28')
    Z, B = T-lam*W, 1+lam*B1
    area_residual = sp.expand(div(-B*grad(Z))-1)
    bed_residual = sp.expand(-lap(Z)+lam*B*grad(Z).dot(grad(Z))-1)
    for residual in [area_residual, bed_residual]:
        require(sp.expand(residual).coeff(lam,0) == 0, 'Verification failed: verify.py:33')
        require(sp.expand(residual).coeff(lam,1) == 0, 'Verification failed: verify.py:34')
    # Full BDN wet-up: all three conservative residuals vanish.
    t,e,s,r,Gv,m = sp.symbols('t e s r Gv m', positive=True)
    A=e*r**m*Gv/(s+(m+1)*r)
    h=r*t; c=A*t**m; z=-r*A*t**(m+1)
    water=sp.simplify(sp.diff(h,t)-r)
    bed=sp.simplify(sp.diff(z,t)-s*c+e*h**m*Gv)
    sediment=sp.simplify(sp.diff(h*c,t)-e*h**m*Gv+s*c)
    require(water == bed == sediment == 0, 'Verification failed: verify.py:42')
    # Wet-side planar front in a moving normal coordinate; Gv = |v_w|^n.
    xi,alpha,V = sp.symbols('xi alpha V', positive=True)
    H=alpha*xi; C=(e/s)*Gv*H**m
    front_water=sp.simplify(-V*sp.diff(H,xi)+V*sp.diff(H,xi))
    front_bed=sp.simplify(s*C-e*H**m*Gv)
    front_sed=sp.simplify(-V*sp.diff(H*C,xi)+V*sp.diff(H*C,xi)-e*H**m*Gv+s*C)
    require(front_water == front_bed == front_sed == 0, 'Verification failed: verify.py:49')
    # Separable factor: time derivative and mth power have the SAME scaling.
    T0,a = sp.symbols('T0 a', positive=True)
    exponent=sp.simplify(-1/(m-1)-1)
    require(sp.simplify(exponent+m/(m-1)) == 0, 'Verification failed: verify.py:53')
    factor=(T0-t)**(-m/(m-1))
    require(sp.simplify(sp.diff((T0-t)**(-1/(m-1)),t)-factor/(m-1)) == 0, 'Verification failed: verify.py:55')
    return {
        'status':'PASS',
        'ellipse_torsion': str(T),
        'ellipse_first_elevation_correction':str(sp.factor(W)),
        'ellipse_first_transport_correction':str(B1),
        'ellipse_area_residual_minimum_lambda_degree':2,
        'ellipse_bed_residual_minimum_lambda_degree':2,
        'wet_up_three_interior_residuals':[str(water),str(bed),str(sediment)],
        'planar_front_three_wet_interior_residuals':[str(front_water),str(front_bed),str(front_sed)],
        'moving_front_distributional_and_viscosity_checks':'Analytical proof in companion; NOT certified by these symbolic interior checks.',
        'separable_Dirac_coefficient_factor':str(factor),
        'warning':'Polynomial identities are exact SymPy checks. They do not certify functional analysis, fixed points, or PDE theorems.'
    }


def universal_solution(d: int,m: float,n: float, end: float=120.0):
    if d<1 or min(m,n,end)<=0: raise ValueError('Positive exponents, end, and dimension required')
    eps=1e-6; a=m+n
    coeff=1/(d**n*(d+a))
    y0=eps/d-coeff*eps**(a+1)
    I0=eps**2/(2*d)-coeff*eps**(a+2)/(a+2)
    Id=eps**(d+2)/(d*(d+2))-coeff*eps**(d+a+2)/(d+a+2)
    def rhs(r,Y):
        yy=max(float(Y[0]),0.0) # only guards implicit trial iterates
        return [1-(d-1)*Y[0]/r-r**m*yy**n,Y[0],r**d*Y[0]]
    def jac(r,Y):
        deriv=-(d-1)/r-(n*r**m*float(Y[0])**(n-1) if Y[0]>0 else 0.0)
        return [[deriv,0.,0.],[1.,0.,0.],[r**d,0.,0.]]
    sol=solve_ivp(rhs,(eps,end),[y0,I0,Id],method='Radau',jac=jac,rtol=2e-10,atol=2e-12,dense_output=True)
    if not sol.success: raise RuntimeError(sol.message)
    rr=np.geomspace(eps,end,1000); yy=sol.sol(rr)[0]
    require(np.all(yy>0), 'Verification failed: verify.py:87')
    require(np.max(yy-rr/d)<2e-8, 'Verification failed: verify.py:88')
    return sol


def numeric_checks() -> dict:
    cases=[(2,0.5,1.0),(2,1.0,1.0),(2,2.0,1.0),(3,0.6,1.2),
           (1,1.0,2.0),(2,0.4,0.6),(3,3.0,1.0)]
    records=[]
    for d,m,n in cases:
        sol=universal_solution(d,m,n)
        r=float(sol.t[-1]); y,I0,Id=map(float,sol.y[:,-1]); p=m/n
        outer=r**p*y
        c=d-1-p
        correction=(outer-1)*r**(p+1)
        target=-c/n
        require(abs(outer-1)<0.02, 'Verification failed: verify.py:103')
        exact_errors=[]
        if n==1.0:
            for q in [0.1,0.4,1.0,2.0,4.0]:
                exact=quad(lambda t:(t/q)**(d-1)*np.exp(-(q**(m+1)-t**(m+1))/(m+1)),0,q,epsabs=1e-13,epsrel=1e-12)[0]
                exact_errors.append(abs(float(sol.sol(q)[0])-exact))
            require(max(exact_errors)<1e-8, 'Verification failed: verify.py:109')
        records.append({'d':d,'m':m,'n':n,'rho_max':r,'rho_to_p_times_y':outer,
                        'scaled_first_correction':correction,'predicted_first_correction':target,
                        'integral_y_to_rho_max':I0,'integral_rho_to_d_y_to_rho_max':Id,
                        'n1_max_quadrature_absolute_error':max(exact_errors) if exact_errors else None,
                        'solver_nfev':sol.nfev})
    # Critical logarithm and supercritical integral illustrate convergence, not proof.
    critical=universal_solution(2,1,1,240.0)
    supercrit=universal_solution(2,2,1,240.0)
    asymptotics=[]
    for r in [15.,30.,60.,120.,240.]:
        asymptotics.append({'rho':r,
            'critical_integral_minus_log':float(critical.sol(r)[1]-np.log(r)),
            'supercritical_integral_plus_leading_tail':float(supercrit.sol(r)[1]+1/r)})
    return {'status':'PASS','cases':records,'asymptotic_constants_illustration':asymptotics,
            'warning':'Floating-point ODE evidence only. No interval enclosures and no formal theorem verification.'}


def main() -> None:
    start=time.perf_counter()
    report={'artifact':'Problem 5 deterministic replay checks',
            'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__},
            'algebra':algebra_checks(),'numerics':numeric_checks()}
    report['wall_seconds']=time.perf_counter()-start
    out=ROOT/'results'/'checks.json'; out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
