# Companion response to the v1.2 referee audit

Addressed referee request 4.3 and the companion-exponent notation point. Edited only `companion/companion.tex`. No compilation or numerical tests were run, as requested. No new broad evolution theorem, publication declarations or version changes were introduced.

## Disposition

**Regularity request: addressed.** The constraint-derivative section now supplies a concrete sufficient class on the fixed interval 0<=y<=1, with V(y,t)=v(f(t)y,t):

- f is C1 and bounded away from zero on each compact positive-time interval; lambda is continuous.
- V is continuous in time with values in C1([0,1]) and belongs to W1,1 in time with values in L1, giving absolute continuity of the pulled-back mass.
- The interior chain-rule equation is written explicitly, including the transport term (f'/f)y V_y.
- A single integrable spatial function dominates both |V^a V_yy| and V^{-1/m}|V_y|² uniformly on each such time interval.
- The zero boundary value and finite C1 edge trace force V^a V_y=0 at y=1; the origin Neumann condition gives the other zero weighted trace.

The proof now derives the moving-boundary cancellation on the fixed domain. It first proves the mass identity almost everywhere, then uses dominated convergence to show continuity of the integrated expression and obtains the positive-time C1 identity. A separate sentence distinguishes this conclusion from the almost-everywhere identity available under weaker conditional hypotheses.

**Initial-time request: addressed separately.** A new paragraph requires the corresponding hypotheses up to t=0, including C1 convergence of the pulled-back profiles, time absolute continuity, positive finite initial support, and one integrable domination function valid down to zero. The evolution equation is required only at t>0. Dominated convergence identifies the right limit of the mass derivative; integrating the absolutely continuous identity and dividing by t proves the right derivative at zero. Initial spatial integrability alone is explicitly stated not to imply these time hypotheses.

The obstruction proposition now points to this sufficient initial-time class while retaining its broader conditional wording: it excludes an evolution only when the stated right-derivative identity holds. Existing exclusions of conclusions about weak initial layers, arbitrary weak solutions, or strictly positive infinite-support data remain unchanged.

**Notation request: addressed.** At the introduction of the reduced channel equation, m is explicitly identified as its porous-medium exponent, not the contributing-area exponent in the main manuscript.

## Mathematical verification

Let a=(m-1)/m and M=f integral V. The fixed-domain equation is

    V_t=(f'/f)y V_y+m V^a(f^{-2}V_yy+lambda V).

Thus the time derivative contains

    f' integral(V+yV_y)=f'[yV]_0^1=0.

The remaining diffusion term is (m/f) integral V^a V_yy. Integration by parts on truncated intervals gives

    integral V^a V_yy=-a integral V^{-1/m}|V_y|²,

with endpoint limits justified by the C1 traces and the integrable domination. Returning to x gives exactly

    M'=-(m-1) integral v^{-1/m}v_x²
          +m lambda integral v^{2-1/m}.

The displayed coefficient chi_m and all following width/perturbation conclusions are unchanged. Continuity of V and V_y in time supplies pointwise convergence of the weighted-gradient integrand in the positive spatial interior; the uniform L1 dominator supplies convergence of its integral. No time continuity of V_yy is needed for this step, because integration by parts has already removed it.

For the initial-time conclusion, the same convergence holds down to t=0. Since M is absolutely continuous on [0,T0],

    (M(t)-M(0))/t=(1/t) integral_0^t M'(s) ds

converges to the continuous right limit, equal to the initial-profile formula by the spatial integration by parts at t=0. This does not assume the PDE itself holds at the initial time.

A simple linear zero of v yields weighted-gradient order distance^{-1/m}, integrable for every m>1. Hence the conditions permit finite positive edge flux and the singular u_x expected there; they do not silently require u to be C1 at the edge. The conditions are sufficient and restrictive, not claimed necessary or satisfied by an as-yet-unconstructed evolution.

## Scope retained

The optional research directions remain future work: a precise general weak formulation, weak existence/nonexistence, or a broader dynamical result is not claimed. Nothing here changes the unresolved status of the positive-data half-line conjecture. This response is an AI mathematical revision record, not human peer-review acceptance or formal certification.
