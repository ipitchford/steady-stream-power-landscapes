# AI and reader index: steady stream-power landscapes

## Identity and status

This is **1.3.0-candidate**, DOI `10.5281/zenodo.23178664`, intended repository tag `v1.3.0-candidate`. Start with [README](README.md), [STATUS](STATUS.md) and [ASSURANCE](ASSURANCE.md). The scientific creator is Anonymous. AI assistance, candidate status and partial resolution must survive any summary. The DOI string is an identifier; provider publication and exact-byte parity require their own receipts.

## Claims and source of truth

Read the [claim ledger](CLAIM_LEDGER.json) and [research gates](RESEARCH_GATES.json), then inspect the [main LaTeX source](manuscript/paper.tex) or [main PDF](manuscript/paper.pdf). Labels are more stable than theorem numbers after revision:

- `thm:general`: variable-forcing small-erosion existence, without general uniqueness.
- `thm:localunique`, `prop:smallness`, `cor:posteriori`, `cor:inexact`: restricted local uniqueness, consolidated constants, continuum residual bounds, finite inner stopping and inexact outer convergence.
- `thm:radial`, `thm:dynamic`, `cor:contraction`: radial steady/dynamic theory; dynamics requires slope exponent at least one.
- `thm:crest`, `thm:moments`, `lem:outersecond`, `thm:momentcorrections`: radial singular limits and distinct finiteness/correction thresholds.

The [companion source](companion/companion.tex) and [companion PDF](companion/companion.pdf) contain exact wet–dry subclasses, the specified channel audit, and `thm:constraintderivative` / `prop:initialobstruction`. Their fixed-domain regularity and initial-time domination assumptions are essential. The positive-data half-line conjecture remains unresolved.

## Evidence and reproduction

Use [requirements.txt](requirements.txt) for declared software dependencies and [the verifier directory](code) for executable checks. The [results directory](results) stores outputs; interpretation depends on input identity and replay provenance. [Frozen ellipse coefficients](data/ellipse-coefficients-v1.2.json) retain their historical data filename and are not newly fitted measurements. [MANIFEST.sha256](MANIFEST.sha256) binds packaged file bytes when finalized.

`verify_global_bounds.py` checks rational inequalities for the saved polynomial, not an exact PDE solution. `verify_nonradial.py` is collocation, not the proved nested algorithm. `verify_negative_controls.py` checks selected rejection behavior; passing it does not certify universal proofs. Follow the README's disposable-extraction workflow because replay can overwrite result files.

## Provenance and changes

Read [PROVENANCE](PROVENANCE.md) for creator, input and licence boundaries and [REVIEW_RESPONSE](REVIEW_RESPONSE.md) for dispositions of the supplied audit. The [provenance directory](provenance) is historical evidence, not a replacement for current claim status. The complete supplied AI-assisted audit is not redistributed; it is not external specialist review.

## Prohibited inference shortcuts

Do not merge the four mathematical regimes into an arbitrary-data theorem; infer novelty from a negative search; infer PDE error bounds from grid residuals; infer an admissible numerical erosion interval from the ellipse margin; describe the full problem as solved; report a REF rating as an official assessment; or treat GitHub/Zenodo/site publication as proof validation.

The AI-index checker validates the presence of this index and its local links only. A successful index check is not scientific validation.
