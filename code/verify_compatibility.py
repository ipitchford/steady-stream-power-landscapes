#!/usr/bin/env python3
"""Exact identities and sampled numerical checks for constraint compatibility."""
from pathlib import Path
import json,math
import sympy as s
from scipy.integrate import quad

def require(condition, message):
    """A release check that remains active with Python optimization."""
    if not condition:
        raise AssertionError(message)

ROOT=Path(__file__).resolve().parents[1]
x,a=s.symbols('x a',real=True)
phi=2*s.cos(x)+9*s.cos(3*x)+5*s.cos(5*x)
require(s.trigsimp(s.expand_trig(phi)-16*s.cos(x)**3*(5*s.cos(x)**2-4))==0, 'Verification failed: verify_compatibility.py:10')
require(s.integrate(phi,(x,0,s.pi/2))==0, 'Verification failed: verify_compatibility.py:11')
require(s.diff(phi,x).subs(x,0)==0, 'Verification failed: verify_compatibility.py:12')
require(s.diff(phi,x).subs(x,s.pi/2)==0, 'Verification failed: verify_compatibility.py:13')
require(s.simplify(s.diff(phi,x,2)+phi+72*s.cos(3*x)+120*s.cos(5*x))==0, 'Verification failed: verify_compatibility.py:14')
coef=-72*(a-1)/(a+3)-120*(a-1)*(a-3)/((a+3)*(a+5))
require(s.factor(coef-192*a*(1-a)/((a+3)*(a+5)))==0, 'Verification failed: verify_compatibility.py:16')
records=[]
for m in [1.2,1.5,2.,3.]:
 a=(m-1)/m
 I=math.sqrt(math.pi)*math.gamma((a+2)/2)/(2*math.gamma((a+3)/2))
 predicted=m*192*a*(1-a)/((a+3)*(a+5))*I
 for eps in [1e-4,1e-5,1e-6]:
  def integrand(x):
   c=math.cos(x)
   v=c*(1+16*eps*c*c*(5*c*c-4))
   return m*v**a*(-72*math.cos(3*x)-120*math.cos(5*x))
  value,error=quad(integrand,0,math.pi/2,epsabs=2e-11,epsrel=2e-11)
  require(value>0, 'Verification failed: verify_compatibility.py:28')
  relative=abs(value-predicted)/predicted
  # Mean-value theorem: |(1+eps*h)^a-1| <= a*eps*16*(1-16*eps)^(a-1).
  # Here |h|<=16, |psi|<=192 and cos(x)^a<=1.
  remainder_bound=m*a*eps*16*(1-16*eps)**(a-1)*192*(math.pi/2)
  require(abs(value-predicted)<=remainder_bound+error, 'Verification failed: verify_compatibility.py:33')
  if eps==1e-6: require(relative<5e-4, 'Verification failed: verify_compatibility.py:34')
  records.append({'m':m,'epsilon':eps,'Mprime_over_epsilon':value,'predicted_limit':predicted,'relative_error':relative,'analytic_absolute_remainder_bound':remainder_bound,'quad_estimated_error':error})
result={'status':'PASS','symbolic':'factorization, initial mass, endpoint derivative and first-order coefficient identities','numerical':records,'scope':'Exact symbolic identities plus sampled floating-point quadratures, not interval arithmetic or a proof of arbitrary-data nonexistence.'}
out=ROOT/'results'/'compatibility.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
