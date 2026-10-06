#!/usr/bin/env python3
"""Asserted numerical checks for v1.1; no interval or formal PDE certification."""
from pathlib import Path
import json, platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import sympy as sp
from verify import universal_solution

def require(condition, message):
    """A release check that remains active with Python optimization."""
    if not condition:
        raise AssertionError(message)

ROOT=Path(__file__).resolve().parents[1]

def nonlinear_remainder(t,n):
    # (1+t)^n-1-n*t, evaluated without subtracting nearly equal O(t) terms.
    if abs(t)<1e-3:
        coef=n; total=0.
        for j in range(2,9):
            coef*= (n-j+1)/j
            total+=coef*t**j
        return total
    return np.expm1(n*np.log1p(t))-n*t

def transformed(d,m,n,tol):
    p=m/n; q=p+1; c=d-1-p
    base=universal_solution(d,m,n,1.)
    v0=float(base.y[0,-1])-1
    def rhs(r,V):
        v=V[0]; t=v*r**(-q)
        return [-r**p*(n*v+c)+(q-c)*v/r-r**(2*p+1)*nonlinear_remainder(t,n)]
    sol=solve_ivp(rhs,(1.,120.),[v0],method='Radau',rtol=tol,atol=tol*.01,dense_output=True)
    require(sol.success, sol.message)
    return sol

def main():
    x=sp.symbols('x',real=True)
    z=2-3*x*x+x**4; b=1/(6-4*x*x)
    require(sp.simplify(-b*sp.diff(z,x)-x)==0, 'Verification failed: verify_extensions.py:36')
    require(sp.diff(z,x,2).subs(x,0)==-6, 'Verification failed: verify_extensions.py:37')
    require(sp.diff(z,x,2).subs(x,1)==6, 'Verification failed: verify_extensions.py:38')
    require(sp.simplify(-sp.diff(1-x**4,x)/(4*x*x)-x)==0, 'Verification failed: verify_extensions.py:39')
    c,n,q=sp.symbols('c n q',positive=True)
    a=-c/n; b2=c*((3-n)*c-2*q)/(2*n*n)
    require(sp.simplify(n*a+c)==0, 'Verification failed: verify_extensions.py:42')
    require(sp.simplify(n*b2+n*(n-1)*a*a/2+(c-q)*a)==0, 'Verification failed: verify_extensions.py:43')
    records=[]
    for d,m,n in [(2,.5,1.),(2,1.,1.),(2,2.,1.),(3,.6,1.2),(1,1.,2.),(2,.4,.6),(3,3.,1.)]:
        p=m/n; q=p+1; c=d-1-p; a=-c/n; b=c*((3-n)*c-2*q)/(2*n*n)
        coarse=transformed(d,m,n,2e-9); fine=transformed(d,m,n,2e-11)
        rows=[]
        for r in [30.,60.,120.]:
            v=float(fine.sol(r)[0]); delta=abs(v-float(coarse.sol(r)[0]))
            # Fixed predeclared mixed budget: truncation-scale term plus numerical floor.
            bound=4*abs(b)*r**(-q)+2e-6
            require(abs(v-a)<bound, (d,m,n,r,v,a,bound))
            require(delta<2e-7, (d,m,n,r,delta))
            rows.append({'rho':r,'observed_first_correction':v,'predicted':a,
                         'absolute_error':abs(v-a),'asserted_tolerance':bound,
                         'tolerance_refinement_difference':delta,
                         'observed_second_correction':(v-a)*r**q,
                         'second_correction_status':'DIAGNOSTIC_ONLY'})
        records.append({'d':d,'m':m,'n':n,'predicted_second_correction':b,'samples':rows})
    critical=universal_solution(2,1.,1.,30.)
    observed=float(critical.y[1,-1]-np.log(30.))
    target=(float(np.euler_gamma)-np.log(2.))/2
    require(abs(observed-target)<1e-8, 'Verification failed: verify_extensions.py:64')
    result={'status':'PASS','versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__},
      'exact_symbolic_checks':'two multiplier examples and two outer-coefficient cancellation identities',
      'first_correction_method':'integrate v=rho^(p+1)*(rho^p*y-1), starting at rho=1 from original ODE; cancellation-safe nonlinear remainder',
      'first_correction_and_refinement':records,
      'critical_log_constant':{'observed':observed,'exact_formula_value':target,'absolute_error':abs(observed-target),'asserted_tolerance':1e-8},
      'limits':'Finite sampled floating-point checks. Second coefficients are exact symbolic identities but their numerical approach is diagnostic only. No numerical claim to verify contraction or moment PDE theorems.'}
    (ROOT/'results/extensions.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
