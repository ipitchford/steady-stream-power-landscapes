# Response to the supplied v1.2 audit

This is an original public response summary for **1.3.0-candidate**. The supplied report is AI-assisted review material, not external specialist peer review, journal acceptance or an official REF assessment. Its complete text is not redistributed because no licence was established. Recommendations were evaluated within the authorised revision; optional research was not made a publication prerequisite.

## Required revisions

| Request | Disposition and evidence |
|---|---|
| Make the strongest coupled theorem visible | Addressed. The comparison table now includes `thm:localunique`; a four-regime table separates variable-forcing existence, restricted local uniqueness, all-parameter radial steadiness and radial dynamics for n>=1. |
| Distinguish exact nesting from finite inner solves | Addressed analytically in `cor:inexact`. Approximate inner steps have a residual stopping rule and a finite-step bound; outer errors obey E_(j+1)<=Q E_j+xi_j and the stated convolution estimate. Flow, quadrature, infinite-tail and Poisson errors are separated. No numerical implementation is claimed. |
| Make companion regularity concrete | Addressed. The pulled-back profile V(y,t)=v(f(t)y,t) has stated C1 spatial continuity, L1 absolute continuity in time, an explicit chain rule and uniform integrable domination. The proof establishes weighted zero traces and positive-time mass differentiability. |
| Distinguish initial-time compatibility from positive-time identity | Addressed separately. Conditions extending to t=0 give the right derivative by dominated convergence and absolute continuity. Initial spatial integrability alone is explicitly insufficient. Weak initial layers and the positive-data half-line conjecture remain outside the obstruction. |
| Resolve notation collisions | Addressed. The reference length is R_ref; L0 remains a gradient Lipschitz constant. The companion's porous-medium exponent is explicitly distinguished from the main paper's contributing-area exponent. |
| Replace prospective publication placeholders without invented authorship | Addressed by the standing Anonymous scholarly creator and a component licence map: original prose/data CC0-1.0, original code MIT. Maintainer/publisher identity is separate. No human contribution, funding or competing-interest declaration is invented. Final metadata consistency is a release gate. |

## Usability and computational recommendations

| Recommendation | Disposition and limit |
|---|---|
| Consolidate smallness inequalities | Addressed in `prop:smallness`. A preliminary tau bound is fixed first, then uniform constants, ball invariance and outer contraction are bounded without circular dependence. |
| Show a checkable nonradial margin | Addressed for x²/4+y²<1: L0/lambda=4/5 and relative margin 1/5. This is not an instantiated K_* or channelization threshold. |
| Give a finite inner-stopping rule | Addressed. Require delta_j<=(1-eta)r_j/4 and stop on the continuum sup norm of the inner step. The exact residual is at most r_j+delta_j. Certified norm bounds and membership of every elevation in the invariant C2,alpha ball remain necessary. |
| Harden Python checks against optimisation | Revised entry points use explicit failure logic rather than relying on removable assertions. The normal/optimized gate and selected negative controls are part of the final replay obligations; their final-byte status is recorded separately. |
| Separate exact-pins replay from the audit's cross-version replay | Required and retained as a distinct gate. The supplied cross-version report is historical evidence only; this response does not assert a final exact-pins replay before its receipt exists. |
| Retain whole-domain rational checks | Added a checker for frozen decimal ellipse polynomials, with residual and positivity bounds over a containing square. It does not enclose the exact PDE solution, verify invariant-ball membership, or certify the selected K. |
| Integrate the threshold figure | The separate explanatory figure and generation route are retained; it has not been inserted into the main manuscript in this bounded revision. The compact regime table was added. Figure placement was a suggestion, not a condition for the stated theorems. |
| Keep model/solution-class boundaries clear | Retained throughout the manuscripts, README, assurance notes and claim ledger. General stream-power dynamics, three-field wet–dry evolution and the channel conjecture are not conflated. |

## Optional research directions

The request for a usable explicit nonradial admissible parameter interval and a continuum enclosure remains **future work**. This revision supplies consolidated symbolic constants and the exact ellipse margin, but not numerical elliptic constants, a verified invariant radius or a certified branch.

Broader nonradial stability or continuation beyond small erosion, and a general weak existence/nonexistence theorem for the channel model, also remain future work. They were not required to make the present restricted proofs publishable. No claim of a four-star output follows from these revisions, extra identities or additional AI review.

## Preserved corrections and limitations

The prescribed-potential sufficiency mechanism is attributed to Richter, not claimed new. Bounded search does not prove priority for the nonlinear refinements. The corrected channel profile does not solve the fixed-coefficient conjecture, and time-dependent normalization still requires its additional terms. The polynomial experiment is collocation, not the nested contraction algorithm. Full problem resolution, human specialist acceptance, formal verification and empirical landscape validation are not asserted.

## Verification disposition

The revised source arguments and code changes are concrete deliverables. Clean frozen-package replay, optimized-mode behavior, negative controls, exact runtime identity, hash coverage, every-page PDF inspection, CI and public readback are separate obligations in [RESEARCH_GATES.json](RESEARCH_GATES.json). This response intentionally does not convert a requested or development-stage check into a completed release gate.
