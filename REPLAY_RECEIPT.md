# Producer replay receipt

The exact-pins normal and optimized receipts are provenance/replay-normal.json and provenance/replay-optimized.json. Each runner executes all seven verification suites in disposable copies. The negative-control suite runs both modes and now includes missing-degree coverage corruption. Code hashes in the manifest bind the checks. The original supplied audit's cross-version replay is a separate historical input, not this exact-pins run.

All 34 PDF pages were visually inspected; native compilation and two-pass exported compilation succeeded. See provenance/pdf_qa.json. The final archive is additionally checked from a fresh extraction by the external publication gate receipt, retained with release assets; that receipt binds the archive digest without circular self-hashing. These are producer checks, not unaffiliated reproduction, formal proof or external specialist review.
