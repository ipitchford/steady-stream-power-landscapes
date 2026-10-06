from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
import json,time

def require(condition, message):
    """A release check that remains active with Python optimization."""
    if not condition:
        raise AssertionError(message)

# Even polynomial collocation on x=2u,y=v, u²+v²<1.
def basis(u,v,N):
    mons=[(i,j) for i in range(N+1) for j in range(N+1-i)]
    def mono(a,b):return u**a*v**b
    P=np.array([mono(2*i,2*j) for i,j in mons]).T
    Pu=np.array([2*i*mono(max(0,2*i-1),2*j) for i,j in mons]).T
    Pv=np.array([2*j*mono(2*i,max(0,2*j-1)) for i,j in mons]).T
    Puu=np.array([2*i*(2*i-1)*mono(max(0,2*i-2),2*j) for i,j in mons]).T
    Pvv=np.array([2*j*(2*j-1)*mono(2*i,max(0,2*j-2)) for i,j in mons]).T
    h=1-u*u-v*v
    Z=h[:,None]*P
    Zx=(h[:,None]*Pu-2*u[:,None]*P)/2
    Zy=h[:,None]*Pv-2*v[:,None]*P
    lap=(h[:,None]*Puu-4*u[:,None]*Pu-2*P)/4+h[:,None]*Pvv-4*v[:,None]*Pv-2*P
    return mons,Z,Zx,Zy,lap,P,Pu/2,Pv

def grid(nr,nt,shift=.5):
    r=(np.arange(nr)+shift)/nr
    t=(np.arange(nt)+shift)/nt*np.pi/2
    rr,tt=np.meshgrid(r,t,indexing='ij')
    return (rr*np.cos(tt)).ravel(),(rr*np.sin(tt)).ravel()
def solve(N,K):
    u,v=grid(N+5,2*N+7); mats=basis(u,v,N)
    mons,Z,Zx,Zy,L,P,Px,Py=mats;M=len(mons)
    c0=np.zeros(2*M);c0[0]=.4;c0[M]=1.
    def residual(c,m=mats):
        _,Z,X,Y,L,P,Px,Py=m;a=c[:M];b=c[M:]
        gx=X@a;gy=Y@a;lap=L@a;B=P@b
        return np.r_[-lap+K*B*(gx*gx+gy*gy)-1,-(Px@b)*gx-(Py@b)*gy-B*lap-1]
    def jac(c):
        a=c[:M];b=c[M:];gx=Zx@a;gy=Zy@a;lap=L@a;B=P@b
        A=-L+2*K*B[:,None]*(gx[:,None]*Zx+gy[:,None]*Zy)
        B1=K*(gx*gx+gy*gy)[:,None]*P
        C=-(Px@b)[:,None]*Zx-(Py@b)[:,None]*Zy-B[:,None]*L
        E=-gx[:,None]*Px-gy[:,None]*Py-lap[:,None]*P
        return np.block([[A,B1],[C,E]])
    fit=least_squares(residual,c0,jac=jac,xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=100)
    require(fit.success, 'Verification failed: verify_nonradial.py:42')
    uu,vv=grid(31,47,.37);test=basis(uu,vv,N);err=residual(fit.x,test);T=len(uu)
    z=test[1]@fit.x[:M];b=test[5]@fit.x[M:]
    # Exact first-order response in normalized coordinates x=2u,y=v.
    x=2*uu;y=vv
    W=(1-uu**2-vv**2)*(44+3*x*x+52*y*y)/1025
    zfirst=.4*(1-uu*uu-vv*vv)-K*W
    return {'degree_parameter':N,'K':K,'success':bool(fit.success),'nfev':fit.nfev,
     'heldout_points':T,'max_bed_residual':float(max(abs(err[:T]))),'max_area_residual':float(max(abs(err[T:]))),
     'min_b':float(min(b)),'min_z_interior':float(min(z)),'summit_z':float(fit.x[0]),
     'max_first_order_difference':float(max(abs(z-zfirst))),
     'coefficients':fit.x.tolist(),'basis_exponents':mons}
def main():
    start=time.time();records=[solve(N,K) for K in [.025,.05,.1,.2] for N in [2,3,4]]
    for K in [.025,.05,.1,.2]:
     r=[v for v in records if v['K']==K]
     require(r[-1]['max_bed_residual']<2e-7 and r[-1]['max_area_residual']<2e-7, r[-1])
     require(max(r[-1]['max_bed_residual'],r[-1]['max_area_residual'])<max(r[0]['max_bed_residual'],r[0]['max_area_residual']), 'Verification failed: verify_nonradial.py:59')
     require(r[-1]['min_b']>0 and r[-1]['min_z_interior']>0, 'Verification failed: verify_nonradial.py:60')
    result={'status':'PASS','method':'Even polynomial least-squares collocation on ellipse; analytic Jacobian; independent staggered residual grid','records':records,'seconds':time.time()-start,'scope':'Floating-point approximate stationary solutions; finite-grid residual tests only, no interval enclosure, global error bound or validation that selected K lies below analytical K0. Solver is not the proved continuum contraction iteration.'}
    (Path(__file__).resolve().parents[1]/'results'/'nonradial.json').write_text(json.dumps(result,indent=2)+'\n')
    for r in records:print({k:v for k,v in r.items() if k not in ['coefficients','basis_exponents']})

if __name__ == "__main__":
    main()
