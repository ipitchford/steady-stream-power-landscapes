# Assurance and trust boundaries

Version: **1.3.0-candidate**. This document separates kinds of evidence rather than treating publication or a test pass as a universal assurance label.

| Dimension | Evidence and limit |
|---|---|
| Analytical arguments | Full proofs are displayed in the two manuscript sources and PDFs. Hypotheses and exclusions are recorded in the claim ledger. No proof-assistant certificate is supplied. |
| AI-assisted review | Supplied audits and additional targeted internal proof checks informed revisions. They are not external specialist peer review or human referee acceptance. |
| Source positioning | Bounded comparisons acknowledge Richter's classical reconstruction principle and known one-dimensional formulas/scalings. No exhaustive priority certificate is asserted. |
| Exact symbolic checks | Polynomial identities and coefficient cancellations are checked algebraically. They do not prove the compactness, regularity, continuation or contraction theorems. |
| Exact rational bounds | Frozen decimal ellipse coefficients are interpreted as rational numbers. Coefficient bounds cover a containing square and establish specified residual/positivity inequalities for those polynomials only. |
| Floating-point calculations | ODE, quadrature and collocation checks test sampled consequences. Tolerance refinement is consistency evidence, not a rigorous error enclosure. Second-tail numerical coefficients remain diagnostic where labeled so. |
| Inexact algorithm | A theorem gives error budgets and finite stopping under continuum error bounds and invariant-set membership. The collocation experiment is not that algorithm; no verified implementation is asserted. |
| Negative controls | Deliberate torsion, ellipse-coefficient and missing-degree corruptions test rejection of those failure modes in ordinary and optimized Python. They do not test arbitrary errors in prose proofs. |
| Physical validity | No real landscape observations are fitted or used to validate the model. Mathematical existence is not empirical model validation. |
| Publication | DOI, tag, CI, provider digests and live page readback establish different publication facts. None substitutes for scientific review. |

## Replay obligations for this release

The final package must retain evidence for a clean extraction replay, installed software identity, ordinary and optimized verification, semantic negative controls, the final hash manifest, source/PDF correspondence, and visual inspection of every PDF page. The [research gates](RESEARCH_GATES.json) distinguish pending gates from recorded results. The exact-pins development receipts and PDF QA are now retained. The final archive digest and clean-extraction gate receipt are external release assets; public-provider states are recorded after upload.

Existing result files may be useful evidence, but their PASS fields must be bound to the checked inputs and runtime. Do not treat a historical or development run as a fresh reproduction of a revised release. Scripts may overwrite result files; verify archived hashes before replay and retain replay output separately.

## Numerical interpretation

The nonradial experiment gives residuals of approximate polynomials, not errors against a known exact landscape. Whole-domain rational residual bounds are stronger than finite-grid checks, but still do not prove the approximation lies in the theorem's invariant ball or that the chosen erosion parameter is admissible. The continuum residual corollary requires its own norms and constants.

For the companion perturbation, the absolute analytical remainder estimate is distinct from QUADPACK's estimated quadrature error. The latter is not interval arithmetic. Positive sample values illustrate the analytical sign proof; they do not replace it or support arbitrary-data nonexistence.

## Rights and review provenance

The supplied review report is an AI-assisted input. Its complete text is not included because redistribution terms were not established. Original response summaries and the manuscripts' corrections may be distributed under the stated original-content licence. Cited papers and source excerpts do not become CC0 merely by being referenced.
