#!/usr/bin/env python3
"""Whole-square coefficient bounds for frozen decimal ellipse polynomials.
Exact rational arithmetic verifies residual budgets and positivity. This does
not enclose an exact PDE solution or certify contraction-ball membership.
"""
import json, hashlib, sys
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
def certify(source):
    data=json.loads(source.read_text(),parse_float=str)
    u,v=sp.symbols('u v');records=[]
    for row in data['records']:
        if sp.Rational(row['K'])!=sp.Rational(1,5):continue
        exponents=row['basis_exponents']; count=len(exponents)
        N=row['degree_parameter']
        expected={(i,j) for i in range(N+1) for j in range(N+1-i)}
        if len(exponents)!=len(expected) or {tuple(e) for e in exponents}!=expected or len(row['coefficients'])!=2*count:
            raise ValueError('Global polynomial structure mismatch')
        values=[sp.Rational(c) for c in row['coefficients']]
        def polynomial(coefs):
            return sp.Poly(sum(c*u**(2*i)*v**(2*j) for c,(i,j) in zip(coefs,exponents)),u,v)
        a=polynomial(values[:count]); b=polynomial(values[count:]);z=sp.Poly(1-u*u-v*v,u,v)*a
        dx=lambda f:f.diff(u)*sp.Rational(1,2)
        dy=lambda f:f.diff(v)
        lap=dx(dx(z))+dy(dy(z))
        bed=-lap+b*(dx(z)**2+dy(z)**2)/5-sp.Poly(1,u,v)
        water=-dx(b)*dx(z)-dy(b)*dy(z)-b*lap-sp.Poly(1,u,v)
        upper=lambda p:sum(abs(c) for c in p.coeffs())
        lower=lambda p:2*p.coeff_monomial(1)-upper(p)
        bounds={'bed':upper(bed),'area':upper(water),'elevation_factor':lower(a),'multiplier':lower(b),'minus_laplacian':lower(-lap)}
        if min(bounds[k] for k in ['elevation_factor','multiplier','minus_laplacian'])<=0:
            raise ValueError('Global positivity failed')
        if row['degree_parameter']==4:
            budgets={'bed':sp.Rational('0.00000281'),'area':sp.Rational('0.00000276')}
            if any(bounds[k]>=budgets[k] for k in budgets):raise ValueError('Global residual budget failed')
            if bounds['multiplier']<=sp.Rational('.9263') or bounds['minus_laplacian']<=sp.Rational('.8269'):
                raise ValueError('Published positivity budget failed')
        records.append({'N':row['degree_parameter'],'bounds_exact':{k:str(v) for k,v in bounds.items()}})
    if len(records)!=3 or {r['N'] for r in records}!={2,3,4}:raise ValueError('Global coverage requires exactly N=2,3,4')
    return {'status':'PASS','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'arithmetic':'exact rational decimal strings; coefficient l1 bound on [-1,1]^2','records':records,'scope':__doc__}
if __name__=='__main__':
    source=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'data/ellipse-coefficients-v1.2.json'
    result=certify(source)
    (ROOT/'results/global_bounds.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
