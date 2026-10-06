# Targeted final mathematical and verifier review

Read-only review of `prop:smallness`, `cor:inexact`, `code/verify_global_bounds.py`, `code/verify_negative_controls.py`, and the relevant explicit-check implementation in the current package. No scripts, numerical tests or compilation were run.

## Main propositions

**No mathematical blocking error found.**

The consolidated smallness constants correctly separate interval invariance, inner contraction, multiplier Lipschitz control, Schauder self-mapping and outer C1 contraction. In particular, H_* bounds the Lipschitz norm of b^(m+1)G, C_g includes the multiplier dependence with its factor tau, and J bounds the spatial Lipschitz norm of b^mG. The conversion to a Holder seminorm via diam(Omega)^(1-alpha) is correct. All constants are independent of the selected tau below the stated upper bound.

The inexact corollary correctly retains b^k, whose exact residual is bounded by the observed approximate-map step plus delta_j. The perturbed inner recurrence gives a limiting step bound 2 delta_j/(1-eta)<=r_j/2, leaving enough room to reach the stopping rule after finitely many iterations. The multiplier-to-Poisson amplification factor and the outer error convolution are correct. The resonant theta=Q case gives j Q^(j-1). Flow truncation includes the required tau factor. Pointwise interval clipping is nonexpansive relative to the exact interval-preserving map. The text correctly assumes, rather than infers from small C1 error, that all elevations stay inside the C2,alpha invariant ball.

## Exact global polynomial bounds

The current arithmetic is mathematically correct for the supplied record schema. JSON decimal literals are parsed as strings and converted to exact rationals. The u=x/2 coordinate derivative is correctly represented by one half of the u derivative. The bed and area residuals have the correct signs and K=1/5 factor. Sum of absolute polynomial coefficients bounds the supremum on [-1,1]^2, and the constant-coefficient-minus-other-coefficients bound is valid for positivity. The stated distinction from an enclosure of an exact PDE solution is appropriate.

### Concrete input-validation gap to address

The verifier currently checks only that three K=1/5 records were processed. It does not require exactly one record for each degree parameter N=2,3,4. Therefore replacing the selected records by three copies of a valid N=2 record passes the count/positivity checks while executing none of the N=4 residual-budget checks. This is an actual false-PASS route for the intended release specification, although it does not change the arithmetic for the present frozen file.

Recommended bounded correction: require the selected degree parameters to be exactly [2,3,4] without duplication; require exactly twice as many coefficients as basis exponents; reject duplicate or malformed exponent pairs. The polynomial construction uses zip, so an incorrect coefficient count can otherwise be silently truncated. If the published elevation-factor lower bound 0.3789 is intended as a release check, enforce it alongside the existing multiplier 0.9263 and minus-Laplacian 0.8269 checks: the present code only enforces strict positivity of the elevation factor.

## Assertion hardening and negative controls

Explicit `require` functions using ordinary `if` and `raise AssertionError` remain active under Python -O; the optimization flag removes assert statements, not explicit exception raising. The inspected entry points use those explicit checks. The frozen-bound verifier and the negative-control controller use ordinary ValueError/RuntimeError checks, also unaffected by -O.

The two negative controls target a changed torsion coefficient and a changed N=4 polynomial coefficient, require nonzero exit status, and check an expected failure marker in stderr in both ordinary and optimized modes. The torsion mutation reaches its explicit algebraic check before the script's result-writing stage. This is correctly scoped to rejection of those particular corruptions, not protection against arbitrary defects in analysis or input schema.

The schema gap above could be closed with an additional duplicate/missing-degree negative control, but that extra test is optional once input validation is made explicit. No proof change is requested.

This is a targeted AI-assisted source review, not test execution, independent human peer review, or formal certification.

Release repair: the verifier now requires exactly one degree 2, 3 and 4 record and validates basis and coefficient lengths. A missing-degree corruption is rejected in normal and optimized modes. The optional .3789 elevation-factor number is not claimed by the manuscript; strict positivity is checked.
