# Steady stream-power landscapes

**Version 1.3.0-candidate · 6 October 2026 · Scholarly creator: Anonymous**

Analytical research on steady stream-power erosion coupled to diffusion and contributing-area conservation, with a separate note on wet–dry benchmarks and a constrained-channel formulation. The broader supplied research problem remains **partially resolved**. This is a research candidate, not a formally certified result or an externally refereed acceptance.

- [Main manuscript](manuscript/paper.pdf) · [editable source](manuscript/paper.tex)
- [Companion note](companion/companion.pdf) · [editable source](companion/companion.tex)
- [Claim ledger](CLAIM_LEDGER.json) · [research gates](RESEARCH_GATES.json)
- [Status](STATUS.md) · [assurance boundaries](ASSURANCE.md) · [review response](REVIEW_RESPONSE.md)
- [Evidence navigation for readers and automated systems](AI_INDEX.md)

Release identifiers: DOI [10.5281/zenodo.23178664](https://doi.org/10.5281/zenodo.23178664); repository [ipitchford/steady-stream-power-landscapes](https://github.com/ipitchford/steady-stream-power-landscapes); tag `v1.3.0-candidate`. The archive is frozen before public upload. Public availability, exact release commit and asset parity are attested separately in the release closeout, avoiding a circular archive hash.

## Results and assumptions

| Setting | Result and boundary |
|---|---|
| Smooth bounded domains; positive Hölder forcing; all positive erosion exponents | Small-erosion steady existence. General elevation uniqueness is not asserted. |
| Constant forcing; exponent sum at least one; strict torsion-flow margin; small erosion | Local uniqueness in the stated bounded continuous multiplier class, nested construction, parameter stability and continuum residual estimates. |
| Balls; constant forcing; unit rainfall; all positive parameters and exponents | Unique regular radial steady state and a universal small-diffusion classification. |
| Compatible monotone radial initial elevations; slope exponent at least one | Global radial evolution and exponential contraction. No transverse stability theorem. |

Version 1.3.0 makes the hypotheses easier to compare, consolidates the sufficient smallness inequalities, and adds an inexact nested-iteration corollary with a finite inner stopping rule and separate flow, quadrature, tail and Poisson error budgets. The ellipse has torsion ratio `L0/lambda = 4/5` and relative margin `1/5`; a numerical admissible erosion interval is not instantiated.

The companion constructs exact wet–dry and wet-up families, repairs a specified channel-profile problem, and audits boundary flux and scaling identities. Its compatibility obstruction now includes sufficient fixed-domain regularity and separate initial-time conditions. It does not settle the strictly positive infinite-support channel conjecture or general wet–dry well-posedness.

The prescribed-potential reconstruction principle is attributed to Richter's classical coefficient-recovery theory. Priority for the coupled nonlinear refinements remains provisional after bounded source comparison.

## Reproduce calculations

Verify the manifest before replay. Use a disposable extraction: verification scripts regenerate results and may record environment-dependent values. Create an isolated Python environment and install the versions in [requirements.txt](requirements.txt).

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python code/verify_manifest.py
python code/run_checks.py
python -O code/run_checks.py
```

Repeat applicable verification commands with `python -O` to check optimized-mode behavior; the negative-control script itself exercises both modes. `python code/plot_thresholds.py` regenerates the explanatory figure. `sh build.sh` uses a TeX installation to rebuild the PDFs; the supplied PDFs can be read without one. Exact tool versions, commands and outcomes belong in the retained replay receipt, not in an inferred claim that any installed environment is equivalent.

The exact-rational polynomial checker bounds residuals and positivity for frozen decimal ellipse coefficients over a containing square. It does not enclose the exact PDE solution or verify membership of the contraction ball. The collocation solver is not an implementation of the proved nested algorithm. The analytical PDE results depend on their displayed proofs, not on passing these scripts.

## Rights and attribution

Original prose, mathematical exposition, structured claims and original data are offered under CC0-1.0; original executable code is MIT. Third-party works retain their own terms. The supplied AI-assisted audit and third-party papers are not redistributed without permission. The package's licence files govern the component map.

Anonymous is the scholarly creator under the publication protocol. Ian Pitchford is repository maintainer and publisher; that role is not a claim of scholarly authorship. AI assistance was used in drafting, derivation, review and computational checking. No human research contribution, funding award, institutional affiliation or absence of competing interests is inferred from the account or audit trail. See [PROVENANCE.md](PROVENANCE.md).
