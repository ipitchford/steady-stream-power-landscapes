# Main-manuscript response to the v1.2 referee audit

Edited only `manuscript/paper.tex`; version, declaration and licence text were not changed. No compilation, numerical replay or optional threshold research was performed.

## Review-to-edit mapping

### 4.1: strongest theorem and regime visibility

- Added Theorem `thm:localunique` to the coefficient-reconstruction comparison table with constant forcing, m+n>=1, strict torsion-flow margin, local small-K scope, and bounded-multiplier uniqueness class visible in its own row.
- Added a compact four-regime table: variable-forcing general-domain small-K existence; constant-forcing local uniqueness under the margin; all-positive-parameter radial steadiness; radial dynamics for n>=1.
- Added an explicit sentence preventing transfer of the uniqueness conclusion to the broader existence hypotheses.

### 4.2 and prioritised plan: inexact nesting and finite inner stopping

Added Corollary `cor:inexact`, which gives:

1. A finite inner iteration starting from b_circ, with interval-preserving approximate evaluations and a per-evaluated-iterate sup error delta_j.
2. The stopping rule ||b^(k+1)-b^k||_infinity <= r_j, with delta_j <= (1-eta)r_j/4.
3. A finite-step guarantee from ||b^k-bhat|| <= eta^k d0+delta_j/(1-eta), with d0<=B-b_circ. Any k satisfying (1+eta)eta^k(B-b_circ)<=r_j/2 suffices.
4. The exact residual bound <=r_j+delta_j, and the resulting outer perturbation xi_j=pi_j+tau C_E M_m G0(r_j+delta_j)/(1-eta).
5. The requested recurrence E_(j+1)<=Q E_j+xi_j, its convolution sum, and convergence for geometrically decreasing errors, including the equal-ratio jQ^(j-1) case.

A following paragraph separates:

- flow/trajectory error e_X,j;
- finite-integral quadrature and integrand-representation error e_I,j;
- explicit infinite-tail error tau B^(m+1)G0 exp(-lambda T_j)/lambda;
- Poisson/spatial-representation/admissibility-correction error pi_j.

Pointwise interval clipping is justified by nonexpansiveness relative to the exact interval-valued map. The evaluation error need only hold at evaluated iterates: no unrealistic universal numerical quadrature guarantee on all continuous functions is imposed.

The text explicitly retains continuum-norm stopping and invariant-set qualifications. Sampled norms do not suffice; a small C1 perturbation does not itself preserve the C2,alpha ball. No implementation or certification of this algorithm is attributed to the collocation experiment.

### 4.4 and prioritised plan: consolidate smallness and show ellipse margin

Added Proposition `prop:smallness` containing one sufficient parameter choice. It first fixes a parameter-independent preliminary upper bound for tau that ensures interval invariance, inner contraction and multiplier Lipschitz control. It then defines uniform L_b,H_*,C_b,C_g,J,G_alpha and takes the minimum of that preliminary bound, the Schauder ball-invariance bound, and the outer-contraction bound. Thus constants are not chosen circularly after tau.

Added the exact ellipse ratios L0/lambda=4/5 and (lambda-L0)/lambda=1/5. The manuscript says these verify only the torsion-flow hypothesis. It does not claim numerical values for the invariant radius or Poisson constants, an admissible numerical K_*, or a channelization threshold.

### Minor notation

Renamed the reference length in the former Remark 2.4 from L0 to R_ref, preserving L0 as the theorem's gradient Lipschitz constant.

## Internal mathematical check

- The consolidated gradient-forcing bound is C_g=B^m C_sigma+M_m G0 C_b tau_bar, directly from the product difference and multiplier stability.
- J=M_m G0 L_b+B^m G1 is the forcing Lipschitz bound. Its C0,alpha norm is bounded by B^mG0+J diam(Omega)^(1-alpha).
- The inexact-step bound has coefficient 2delta/(1-eta): (1+eta)delta/(1-eta)+delta simplifies to this value. The selected delta budget leaves at least half the stopping tolerance for the decaying transient.
- The Poisson perturbation carries the exact factor tau C_E M_m G0/(1-eta), matching the earlier continuum residual corollary.
- The tail formula is the integral of the uniform integrand bound over [T_j,infinity].
- No arbitrary-data, variable-forcing uniqueness, nonradial dynamical stability, or numerical proof claim has been added.

## Integration notes for root

The new proposition and corollary change later theorem numbering through normal LaTeX references. The expanded comparison table and added regime table need the planned PDF layout pass. This report does not claim compilation or rendered-page verification. Publication metadata remains for root to handle.
