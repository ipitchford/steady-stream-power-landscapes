**Archive DOI:** <https://doi.org/10.5281/zenodo.23178664>. Version 1.3.0-candidate.

**Status.** Prospective Evidence Press research manuscript. Version 1.3 revises the supplied manuscript and AI-assisted referee audit, with additional AI-assisted analytical review and new proofs. No human referee acceptance or proof-assistant verification is claimed. Originality is provisional: known one-dimensional formulas and earlier vanishing-diffusion work are explicitly acknowledged.

# Model, solution convention, and scope

Let $`\Omega\subset\mathbb R^d`$ be a bounded connected domain. Elevation $`z`$, specific contributing area $`a`$, and downhill water flux $`q`$ obey
``` math
\begin{align}
 z_t&=D\Delta z-Ka^m|\nabla z|^n+U,\label{eq:sp}\\
 \operatorname{div}q&=\rho,\qquad q=-a\frac{\nabla z}{|\nabla z|},\qquad z|_{\partial\Omega}=0.\label{eq:area}
\end{align}
```
Here $`D>0`$, $`K\geq0`$, $`m,n>0`$, and the rainfall normalization is $`\rho=1`$ unless stated otherwise. For $`\rho=1`$, the variable $`a`$ is specific contributing area, not total upstream drainage area. With variable $`\rho`$, it is the corresponding rainfall-weighted specific discharge in the chosen normalization; this is an explicit extension of the constant-rainfall model. Equations <a href="#eq:sp" data-reference-type="eqref" data-reference="eq:sp">[eq:sp]</a>–<a href="#eq:area" data-reference-type="eqref" data-reference="eq:area">[eq:area]</a> are the continuum model studied by Bonetti et al. ; the conservation-law formulation of contributing area and its critical points is developed in .

The normalized direction in <a href="#eq:area" data-reference-type="eqref" data-reference="eq:area">[eq:area]</a> is undefined where $`\nabla z=0`$. Throughout, the primary object is the flux $`q`$: its divergence equation holds on the entire domain in distributions, without additional point sources. On the noncritical set the displayed direction identity must hold. The solutions constructed below have $`q=0`$ and $`a=0`$ on the critical set, so this convention does not conceal a singular source.

<div class="definition">

**Definition 1** (Classical-elevation, conservative-flux steady state). A steady solution is a pair $`z\in C^{2,\alpha}(\overline\Omega)`$, $`q\in C^{0,\alpha}(\overline\Omega;\mathbb R^d)`$, with $`a=|q|\geq0`$, for which the steady equation <a href="#eq:sp" data-reference-type="eqref" data-reference="eq:sp">[eq:sp]</a> holds pointwise, $`z=0`$ on the boundary, $`\operatorname{div}q=\rho`$ in distributions, and $`q=-a\nabla z/|\nabla z|`$ wherever $`\nabla z\ne0`$.

</div>

The distinction between models matters. Binard, Degond and Noble  prove short-time well-posedness for a coupled water–bed–sediment system under strictly positive water depth. Birnir and Landry  establish global weak existence for a different, transport-limited sediment equation with prescribed water depth. Neither result is an existence theorem for <a href="#eq:sp" data-reference-type="eqref" data-reference="eq:sp">[eq:sp]</a>–<a href="#eq:area" data-reference-type="eqref" data-reference="eq:area">[eq:area]</a>. Hooshyar et al.  study variational formulations; Anand et al.  investigate self-similarity and vanishing diffusion, including explicit one-dimensional cases. Litwin et al.  give an all-exponent dimensional scaling of the specific-area model and examine its channel–hillslope coupling. We do not claim that one-dimensional hillslope formulas, dimensional scales, the logarithmic $`m=n=1`$ limit, or the general idea of drainage characteristics originate here.

The main candidate contributions concern the nonlinear coupling: general-domain small-erosion existence, a constructive locally unique branch under the additional assumptions stated below, and the quantitative radial theory. The underlying prescribed-potential solvability principle is classical: Richter already allows critical points and positive forcing. We provide the explicit Hölder estimates and distributional formulation required by the coupled construction, rather than claiming a new linear existence criterion. The proofs below are complete at the level of standard elliptic and parabolic analysis, whose classical ingredients are specified where used.

## Comparison with coefficient reconstruction

The coefficient-reconstruction ancestry is directly relevant to the linear drainage step, and must be separated from solving for the unknown landscape itself. Table <a href="#tab:prior" data-reference-type="ref" data-reference="tab:prior">1</a> records only conclusions supported by the sources inspected; an unavailable theorem is not treated as excluded prior art.

<div id="tab:prior">

| Source and locator | Prescribed data and setting | Result and distinction |
|:---|:---|:---|
| Briane , Theorem 2.1 and Remark 2.2 | Source-free $`\operatorname{div}(\sigma\nabla u)=0`$; prescribed $`u`$; local nondegenerate saddle in $`d=2,3`$, with additional trajectory hypotheses | Bounded positive conductivity and reciprocal via an integrated-Laplacian condition; no positive-source coupled erosion equation. |
| Briane , Theorem 2.1 | $`u\in W^{2,1}_{\rm loc}`$; uniformly continuous nonvanishing gradient; bounded Laplacian on $`\mathbb R^d`$ | Positive locally bounded conductivity and reciprocal for the source-free equation; rough-field reconstruction, not the coupled problem. |
| Richter , Theorem 1, pp. 216–217 | Prescribed $`u`$; $`|\nabla u|\geq k_1`$ or $`\Delta u\geq k_2>0`$; bounded characteristic solutions | Existence, uniqueness and sup bounds with inflow data. With $`u=-z`$ and empty inflow this already covers the linear sufficiency principle used here. |
| Theorem <a href="#thm:criticalcriterion" data-reference-type="ref" data-reference="thm:criticalcriterion">3</a> here | Positive source; bounded smooth domain; inward uphill flow; arbitrary compact critical set | Explicit Hölder and distributional refinement of the classical solvability condition; necessity in the continuous nonnegative multiplier class is included. |
| Theorem <a href="#thm:general" data-reference-type="ref" data-reference="thm:general">4</a> here | Same flux convention; unknown $`z`$ coupled to erosion; positive forcing and zero elevation on the entire boundary | Small-$`K`$ existence via compact fixed point, with Hölder flux and classical elevation; no elevation uniqueness claim. |
| Theorem <a href="#thm:localunique" data-reference-type="ref" data-reference="thm:localunique">6</a> here | Unknown coupled landscape; constant positive forcing; $`m+n\geq1`$; torsion-flow margin $`L_0<U/D`$ | Locally unique small-$`K`$ branch in the bounded continuous multiplier class, with a convergent construction and continuum error bounds. |

A bounded comparison of mathematical settings, not an exhaustive novelty certificate.

</div>

The hypotheses of these conclusions are separate. In particular, the general existence theorem does not inherit the stronger theorem’s uniqueness conclusion.

<div id="tab:regimes">

| Regime | Additional hypotheses | Conclusion |
|:---|:---|:---|
| General-domain existence, Theorem <a href="#thm:general" data-reference-type="ref" data-reference="thm:general">4</a> | Positive Hölder forcing; $`m,n>0`$; sufficiently small $`K`$ | Classical elevation and conservative Hölder flux; uniqueness not asserted. |
| Local uniqueness, Theorem <a href="#thm:localunique" data-reference-type="ref" data-reference="thm:localunique">6</a> | Constant forcing; $`m+n\geq1`$; $`L_0<U/D`$; small $`K`$ and a fixed torsion neighborhood | Unique branch in the stated bounded-multiplier class. |
| Radial steadiness, Theorem <a href="#thm:radial" data-reference-type="ref" data-reference="thm:radial">12</a> | Ball; constant forcing and unit rainfall; $`m,n>0`$ | Unique regular radial steady state for every positive parameter value. |
| Radial dynamics, Theorem <a href="#thm:dynamic" data-reference-type="ref" data-reference="thm:dynamic">14</a> | Same radial setting; compatible monotone initial data; $`n\geq1`$ | Global evolution and exponential radial contraction. |

Four regimes for the coupled model; uniqueness and dynamics are restricted to the classes displayed.

</div>

The landscape-specific comparisons are also equation-level: Anand et al.  already analyze one-dimensional vanishing diffusion and explicit profiles; Litwin et al.  give the relevant dimensional scale. Binard et al.  instead treat a three-field positive-depth Cauchy problem on $`\mathbb R^2`$, under additional exponent and Sobolev assumptions. None of these inspected statements is the general-domain coupled steady theorem above. Priority for the full theorem package remains provisional. The supplied full Richter paper has now been compared: its Theorem 1 covers the prescribed-potential sufficiency principle, and its Theorem 2 (p. 219) gives a positive-source, zero-boundary inverse setting with no Cauchy data. Neither theorem solves the present nonlinear erosion coupling.

# Steady existence on arbitrary smooth domains

## The damped drainage resolvent

Write
``` math
\begin{equation}
 a=b|\nabla z|,\qquad q=-b\nabla z.\label{eq:bchange}
\end{equation}
```
The area equation becomes the nonsingular transport equation
``` math
\begin{equation}
 v\cdot\nabla b+\delta b=\rho,\qquad v=-\nabla z,\quad \delta=\operatorname{div}v=-\Delta z.\label{eq:transport}
\end{equation}
```
No division by $`|\nabla z|`$ occurs in this equation.

<div id="lem:resolvent" class="lemma">

**Lemma 2** (Resolvent with critical points). *Suppose $`z\in C^{2,\alpha}(\overline\Omega)`$, $`\partial_\nu z<0`$ on $`\partial\Omega`$, and
``` math
0<\kappa\leq\delta=-\Delta z\leq A.
```
Let $`L`$ be a Lipschitz constant for $`\nabla z`$ on $`\overline\Omega`$, and assume $`\alpha L<\kappa`$. Let $`0<\rho_-\leq\rho\leq\rho_+`$ with $`\rho\in C^{0,\alpha}`$. Define the backward downhill flow by
``` math
\partial_t X(t,x)=\nabla z(X(t,x)),\qquad X(0,x)=x,
```
and set
``` math
\begin{equation}
 b_z(x)=\int_0^\infty
 \exp\!\left[-\int_0^t\delta(X(s,x))\,\mathrm ds\right]\rho(X(t,x))\,\mathrm dt.\label{eq:resolvent}
\end{equation}
```
Then $`b_z\in C^{0,\alpha}`$, $`\rho_-/A\leq b_z\leq\rho_+/\kappa`$, and
``` math
\begin{equation}
 [b_z]_\alpha\leq
 \frac{[\rho]_\alpha}{\kappa-\alpha L}
 +\frac{\rho_+[\delta]_\alpha}{\kappa(\kappa-\alpha L)}.\label{eq:holderb}
\end{equation}
```
The flux $`-b_z\nabla z`$ has divergence $`\rho`$ in distributions. This is the unique bounded continuous solution of <a href="#eq:transport" data-reference-type="eqref" data-reference="eq:transport">[eq:transport]</a> along characteristics. At every critical point $`x_*`$,
``` math
\begin{equation}
 b_z(x_*)=\rho(x_*)/\delta(x_*).\label{eq:criticalb}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* The vector field $`\nabla z`$ points strictly inward at the boundary. Its flow therefore exists in $`\overline\Omega`$ for every $`t\geq0`$. There is no need to assume that each trajectory converges to a unique maximum. The exponential in <a href="#eq:resolvent" data-reference-type="eqref" data-reference="eq:resolvent">[eq:resolvent]</a> lies between $`e^{-At}`$ and $`e^{-\kappa t}`$, which proves convergence and the two pointwise bounds.

Gronwall’s inequality gives $`|X(t,x)-X(t,y)|\leq e^{Lt}|x-y|`$. The difference of the two integrands is bounded by the sum of
``` math
e^{-\kappa t}[\rho]_\alpha e^{\alpha Lt}|x-y|^\alpha
```
and
``` math
\rho_+e^{-\kappa t}[\delta]_\alpha
 \int_0^t e^{\alpha Ls}\,\mathrm ds\,|x-y|^\alpha.
```
Integrating, and reversing the order of the latter integral, proves <a href="#eq:holderb" data-reference-type="eqref" data-reference="eq:holderb">[eq:holderb]</a>.

For completeness, the distributional equation follows without assuming spatial differentiability of $`b_z`$. Put
``` math
T_tf(x)=\exp\!\left[-\int_0^t\delta(X(s,x))\,\mathrm ds\right]f(X(t,x)).
```
This is the characteristic semigroup for the operator $`-(v\cdot\nabla+\delta)=-\operatorname{div}(v\,\cdot)`$. The exponential weight is the Jacobian determinant of the backward flow. For smooth coefficients the generator identity follows by differentiation and change of variables against a compactly supported test function. Approximation of the $`C^1`$ vector field in $`C^1`$, followed by uniform convergence of the flow and its Jacobian on finite time intervals, gives the same distributional identity here. Continuous $`f`$ is then obtained by uniform approximation. Thus, for $`b_T=\int_0^T T_t\rho\,\mathrm dt`$,
``` math
\operatorname{div}(vb_T)=\rho-T_T\rho
```
in distributions. Uniform convergence $`b_T\to b_z`$ and $`T_T\rho\to0`$ gives the assertion. Equivalently, integrating <a href="#eq:transport" data-reference-type="eqref" data-reference="eq:transport">[eq:transport]</a> along a characteristic gives the same formula with a terminal term $`T_Tb(x)`$, of absolute value at most $`e^{-\kappa T}\|b\|_\infty`$; its limit is zero. This proves uniqueness in the stated characteristic class. At a critical point the flow is constant, and <a href="#eq:criticalb" data-reference-type="eqref" data-reference="eq:criticalb">[eq:criticalb]</a> is immediate. ◻

</div>

## A sharper criterion for a prescribed landscape

The strict superharmonicity in Lemma <a href="#lem:resolvent" data-reference-type="ref" data-reference="lem:resolvent">2</a> is convenient for the nonlinear fixed point, but stronger than necessary for the linear drainage problem.

Richter’s positive-source reconstruction theory is the closest antecedent, not only the source-free conductivity literature. Set $`u=-z`$. His equation $`L(b;u)=\nabla b\cdot\nabla u+b\Delta u=\rho`$ is exactly <a href="#eq:transport" data-reference-type="eqref" data-reference="eq:transport">[eq:transport]</a>. Under our compactness and boundary assumptions, positivity of $`\Delta u`$ at critical points is equivalent to the existence of $`k_1,k_2>0`$ such that $`|\nabla u|\geq k_1`$ or $`\Delta u\geq k_2`$ everywhere. This is the partition hypothesis of . Moreover $`\partial_\nu u>0`$, so the inflow boundary is empty. Richter defines bounded solutions along characteristics (p. 213) and proves existence, uniqueness and sup estimates. Thus the sufficiency principle below is not new. Our self-contained proof records a quantitative Hölder estimate, proves conservation distributionally across critical sets, and establishes necessity for a continuous nonnegative multiplier. These are the versions used by the coupled fixed point. Briane’s source-free reconstructions provide related but different regularity theory.

<div id="thm:criticalcriterion" class="theorem">

**Theorem 3** (Classical critical-set solvability with a Hölder refinement). *Let $`\Omega`$ be a bounded $`C^{2,\alpha_0}`$ domain. Let $`z\in C^{2,\alpha_0}(\overline\Omega)`$ have zero boundary values and $`\partial_\nu z<0`$ on the boundary. Let $`\rho\in C^{0,\alpha_0}`$ be strictly positive. A bounded nonnegative continuous multiplier $`b`$ with
``` math
\operatorname{div}(-b\nabla z)=\rho
```
exists if and only if
``` math
\begin{equation}
 -\Delta z(x)>0\qquad\text{at every }x\text{ with }\nabla z(x)=0.\label{eq:criticalcriterion}
\end{equation}
```
When this holds, the resolvent <a href="#eq:resolvent" data-reference-type="eqref" data-reference="eq:resolvent">[eq:resolvent]</a> constructs such a multiplier, which is strictly positive and $`C^{0,\alpha}`$ for some $`\alpha>0`$. It is unique among bounded continuous characteristic solutions. The assertion concerns the multiplier class $`q=-b\nabla z`$ with bounded continuous $`b`$, not every possible continuous contributing-area flux.*

</div>

<div class="proof">

*Proof.* For necessity fix a critical point $`x_*`$, write $`H=D^2z(x_*)`$, and rescale
``` math
q_r(y)=\frac{-b(x_*+ry)\nabla z(x_*+ry)}r.
```
Continuity of $`b`$ and differentiability of $`\nabla z`$ give $`q_r\to-b(x_*)Hy`$ uniformly on each bounded set. Meanwhile $`\div_y q_r=\rho(x_*+ry)`$ in distributions. Passing to the limit gives
``` math
\rho(x_*)=-b(x_*)\operatorname{tr}H=b(x_*)\delta(x_*).
```
The positive left side and nonnegative finite $`b(x_*)`$ force $`\delta(x_*)>0`$.

For sufficiency, the critical set is compact and lies away from the boundary. By <a href="#eq:criticalcriterion" data-reference-type="eqref" data-reference="eq:criticalcriterion">[eq:criticalcriterion]</a>, choose $`\kappa,\varepsilon>0`$ such that $`\delta\geq\kappa`$ wherever $`|\nabla z|\leq\varepsilon`$. Let $`|\delta|\leq A`$ globally. Along the backward flow,
``` math
\frac{\mathrm d}{\mathrm dt}z(X(t,x))=|\nabla z(X(t,x))|^2.
```
Therefore the total time a trajectory can spend where $`|\nabla z|>\varepsilon`$ is at most $`\operatorname{osc}(z)/\varepsilon^2`$, uniformly in its starting point and its time horizon. Consequently
``` math
\begin{equation}
 \int_0^t\delta(X(s,x))\,\mathrm ds
 \geq\kappa t-C_*,\qquad
 C_*=(A+\kappa)\operatorname{osc}(z)/\varepsilon^2.\label{eq:averagedamping}
\end{equation}
```
The integrand in <a href="#eq:resolvent" data-reference-type="eqref" data-reference="eq:resolvent">[eq:resolvent]</a> is thus bounded by $`\rho_+e^{C_*}e^{-\kappa t}`$. It follows that $`b`$ is finite and strictly positive, with
``` math
\rho_-/A\leq b\leq\rho_+e^{C_*}/\kappa.
```
Choose $`\alpha<\min(\alpha_0,\kappa/L)`$. The same difference estimate as in Lemma <a href="#lem:resolvent" data-reference-type="ref" data-reference="lem:resolvent">2</a>, now with the prefactor $`e^{C_*}`$, proves Hölder continuity. Indeed both exponential weights are at most $`e^{C_*}e^{-\kappa t}`$, and their difference is bounded by that quantity times the difference of their integrated exponents. The semigroup proof gives the distributional equation. The terminal term of any bounded characteristic solution tends to zero by <a href="#eq:averagedamping" data-reference-type="eqref" data-reference="eq:averagedamping">[eq:averagedamping]</a>, proving the stated uniqueness. ◻

</div>

The criterion allows regions where $`\Delta z>0`$, provided the Laplacian has the required sign at every critical point. At a steady solution of the erosion equation that sign is automatic, since $`-D\Delta z=U`$ at a critical point. This observation does not supply the missing a priori estimates for an arbitrary-$`K`$ nonlinear fixed point. It does explain why the drainage construction itself is not restricted to globally superharmonic topographies. For example, a flat maximum can admit a continuous flux while requiring an unbounded multiplier; such a case lies outside the criterion’s stated class.

#### Two examples that separate the hypotheses.

On $`(-1,1)`$ with $`\rho=1`$, let
``` math
z=2-3x^2+x^4,\qquad b=(6-4x^2)^{-1},\qquad q=x.
```
Then $`z(\pm1)=0`$, its outward derivative is negative, and $`-bz'=q`$. The only interior critical point is zero, where $`-z''=6>0`$; near the boundary $`-z''=6-12x^2<0`$. Thus the critical-set theorem applies although global superharmonicity fails. In contrast, $`z=1-x^4`$ and $`q=x`$ also give continuous downhill drainage with $`q'=1`$, but $`b=1/(4x^2)`$ off zero is unbounded. This is outside the multiplier theorem, not a counterexample to it. Neither example is asserted to solve the coupled steady erosion equation with positive constant uplift.

## A compact fixed point

<div id="thm:general" class="theorem">

**Theorem 4** (General-domain steady existence). *Let $`\Omega`$ be bounded, connected and $`C^{2,\alpha_0}`$, $`0<\alpha_0<1`$. Suppose $`D>0`$, $`m,n>0`$, and $`U,\rho\in C^{0,\alpha_0}(\overline\Omega)`$ have strictly positive lower bounds. There exist $`K_0>0`$ and $`\alpha\in(0,\alpha_0)`$ such that every $`K\in[0,K_0]`$ admits a steady solution in the sense of Definition 1.1. In fact
``` math
q=-b\nabla z,\quad a=b|\nabla z|,\quad b\in C^{0,\alpha},\quad 0<b_-\leq b\leq b_+.
```
If $`z_0`$ solves $`-D\Delta z_0=U`$, $`z_0|_{\partial\Omega}=0`$, then $`K_0`$ may be chosen so that
``` math
\begin{equation}
 \tfrac12z_0\leq z\leq z_0,\qquad
 \|z-z_0\|_{C^{2,\alpha}}\leq C K.\label{eq:smallbounds}
\end{equation}
```
At every critical point of $`z`$,
``` math
\begin{equation}
 b(x_*)=\frac{D\rho(x_*)}{U(x_*)},\qquad
 \mathrm D_xq(x_*)=-\frac{D\rho(x_*)}{U(x_*)}\,D^2z(x_*).\label{eq:criticalflux}
\end{equation}
```
No convexity, radiality, or nondegeneracy of critical points is assumed. Uniqueness of $`z`$ is not asserted.*

</div>

<div class="proof">

*Proof.* The classical Dirichlet Poisson theorem, maximum principle and Hopf lemma give $`z_0\in C^{2,\alpha_0}`$, $`z_0>0`$ in $`\Omega`$, and $`\partial_\nu z_0\leq-\eta<0`$ on its compact boundary; see . These are the only domain-regularity facts needed.

Choose a sufficiently small $`C^2`$ neighborhood of $`z_0`$ in the zero-boundary affine space. Every function in it satisfies
``` math
-\Delta z\geq\kappa:=\frac{\min U}{2D},\qquad
 -\Delta z\leq A,\qquad \partial_\nu z\leq-\eta/2,
```
with common constants $`A`$ and $`L`$ bounding $`-\Delta z`$ and the Lipschitz constant of $`\nabla z`$. A fixed extension operator on the smooth domain supplies a common global Lipschitz bound when $`\Omega`$ is nonconvex. Choose
``` math
0<\alpha<\min\{\alpha_0,1,m+n,\kappa/(2L)\}.
```
If $`L=0`$ the last restriction is omitted. Fix a sufficiently small $`\varepsilon>0`$ and put
``` math
\mathcal C=\{z:z|_{\partial\Omega}=0,\quad
 \|z-z_0\|_{C^{2,\alpha}}\leq\varepsilon\}.
```
Regarded as a subset of $`C^{2,\beta}`$ for a fixed $`0<\beta<\alpha`$, this set is convex and compact. It is closed in that topology because the $`\alpha`$-Hölder seminorm is lower semicontinuous under uniform convergence of second derivatives.

For each $`z\in\mathcal C`$ construct $`b_z`$ by Lemma <a href="#lem:resolvent" data-reference-type="ref" data-reference="lem:resolvent">2</a>, and let
``` math
g_z=b_z^m|\nabla z|^{m+n}.
```
The positive upper and lower bounds on $`b_z`$, its uniform $`C^{0,\alpha}`$ norm, and $`\alpha<\min(1,m+n)`$ imply a common bound $`\|g_z\|_{C^{0,\alpha}}\leq G`$. Let $`P=(-\Delta_D)^{-1}`$ be the zero-boundary Poisson inverse, with Schauder bound $`\|Pf\|_{C^{2,\alpha}}\leq C_P\|f\|_{C^{0,\alpha}}`$. Define
``` math
\begin{equation}
 \mathcal F_K(z)=z_0-\frac K D P g_z.\label{eq:fixedmap}
\end{equation}
```
For $`K\leq D\varepsilon/(C_PG)`$ this map preserves $`\mathcal C`$.

We check the continuity needed for the fixed-point theorem rather than assume differentiability of the drainage map. If $`z_j\to z`$ in $`C^{2,\beta}`$ inside $`\mathcal C`$, their flows converge uniformly on finite time intervals. The integrands in <a href="#eq:resolvent" data-reference-type="eqref" data-reference="eq:resolvent">[eq:resolvent]</a> therefore converge uniformly there; their tails are uniformly exponentially small. Hence $`b_{z_j}\to b_z`$ uniformly. Uniform $`C^{0,\alpha}`$ bounds improve this to convergence in $`C^{0,\beta}`$. The same argument applies to $`g_{z_j}`$, including noninteger powers at $`\nabla z=0`$. The Poisson estimate at exponent $`\beta`$ proves continuity of $`\mathcal F_K`$ in $`C^{2,\beta}`$. Schauder’s compact-convex fixed-point theorem now gives $`z=\mathcal F_K(z)`$.

The fixed-point equation is exactly
``` math
-D\Delta z+K b_z^m|\nabla z|^{m+n}=U.
```
Lemma <a href="#lem:resolvent" data-reference-type="ref" data-reference="lem:resolvent">2</a> gives the global flux equation. Restricting $`K_0`$ further to $`K_0G\leq\min U/2`$ gives $`U/2\leq-D\Delta z\leq U`$; comparison with the Poisson solution proves <a href="#eq:smallbounds" data-reference-type="eqref" data-reference="eq:smallbounds">[eq:smallbounds]</a>. The norm estimate follows from <a href="#eq:fixedmap" data-reference-type="eqref" data-reference="eq:fixedmap">[eq:fixedmap]</a>. At a critical point erosion vanishes, so $`\delta=U/D`$ and <a href="#eq:criticalb" data-reference-type="eqref" data-reference="eq:criticalb">[eq:criticalb]</a> proves the first identity in <a href="#eq:criticalflux" data-reference-type="eqref" data-reference="eq:criticalflux">[eq:criticalflux]</a>. Since $`b`$ is continuous and $`\nabla z(x_*)=0`$, Taylor expansion of $`\nabla z`$ proves the derivative formula for $`q`$. This derivative exists at the critical point even though only Hölder regularity is asserted for the flux globally. ◻

</div>

<div class="remark">

*Remark 5* (What smallness means). The proof gives a positive threshold in terms of a Poisson Schauder constant, a flow Lipschitz bound, and the displayed Hölder estimates. It is an existence threshold, not a calibrated numerical channelization threshold. On a fixed rescaled domain with constant forcing, the natural erosion parameter is $`K U^{n-1}R_{\rm ref}^{m+n}/D^n`$, where $`R_{\rm ref}`$ is the chosen length scale. No claim about all values of this parameter on arbitrary domains is made.

</div>

## A constructive locally unique nonradial branch

Constant forcing permits a different resolvent that removes the Laplacian from the multiplier’s dependence on the trial elevation. This is useful because the original resolvent gives continuity but need not give a contraction in the norms used by the Poisson inverse.

<div id="thm:localunique" class="theorem">

**Theorem 6** (Local uniqueness and convergent construction). *Let $`D,U,\rho>0`$ be constants, $`m,n>0`$, $`\sigma=m+n\geq1`$, and let $`\Omega`$ be a bounded connected $`C^{2,\alpha}`$ domain, $`0<\alpha<1`$. Put $`\lambda=U/D`$, $`b_\circ=\rho/\lambda`$, and let $`-\Delta z_0=\lambda`$ with $`z_0|_{\partial\Omega}=0`$. Suppose $`\nabla z_0`$ has a global Euclidean Lipschitz constant $`L_0<\lambda`$ on $`\overline\Omega`$. There exist $`\varepsilon,K_*>0`$ such that for $`0\leq K\leq K_*`$ there is exactly one steady state in the class
``` math
\|z-z_0\|_{C^{2,\alpha}}\leq\varepsilon,\qquad
 q=-b\nabla z,\qquad b\text{ bounded, nonnegative and continuous}.
```
Here the boundary and distributional conventions are those of Definition 1.1. The multiplier is Lipschitz, $`b_\circ\leq b\leq2b_\circ`$, with $`\operatorname{Lip}(b)=O(K)`$. A nested multiplier/Poisson iteration converges to this solution, with outer contraction in $`C^1`$. The solution depends Lipschitz-continuously on $`K`$ in $`C^1`$ for $`z`$ and $`C^0`$ for $`b`$. This is local uniqueness in the stated multiplier class, not uniqueness among arbitrary conservative fluxes or at arbitrary erosion intensity.*

</div>

<div class="proof">

*Proof.* Write $`\tau=K/D`$ and $`B=2b_\circ`$. Choose a small closed zero-boundary $`C^{2,\alpha}`$ ball $`\mathcal C`$ about $`z_0`$ such that, uniformly on it,
``` math
-\Delta z\geq\lambda/2,\quad \partial_\nu z<0,\quad
 \operatorname{Lip}(\nabla z)\leq L<\lambda,\quad
 \|\nabla z\|_\infty\leq M.
```
A bounded extension operator controls global Lipschitz differences on nonconvex domains, so the strict $`L_0`$ margin persists in a sufficiently small ball. The set $`\mathcal C`$ is complete in the $`C^1`$ metric: its boundedness in $`C^{2,\alpha}`$ gives subsequential convergence in $`C^{2,\beta}`$, $`\beta<\alpha`$, and lower semicontinuity of the $`\alpha`$ seminorm puts the $`C^1`$ limit back in the ball. For $`G_z=|\nabla z|^\sigma`$ there are uniform constants
``` math
\|G_z\|_\infty\leq G_0=M^\sigma,\qquad
 \operatorname{Lip}(G_z)\leq G_1=\sigma M^{\sigma-1}L,\qquad
 \|G_z-G_w\|_\infty\leq C_\sigma\|\nabla z-\nabla w\|_\infty,
```
where $`C_\sigma=\sigma M^{\sigma-1}`$. Enlarge $`M`$ if necessary so $`M>0`$. These estimates include $`\sigma=1`$.

*Multiplier contraction.* For each $`z\in\mathcal C`$ let $`X_z`$ be its uphill flow and define, on continuous $`b_\circ\leq b\leq B`$,
``` math
\begin{equation}
 \mathcal T_{\tau,z}b(x)=b_\circ+\tau\int_0^\infty e^{-\lambda t}
 b(X_z(t,x))^{m+1}G_z(X_z(t,x))\,\mathrm dt.\label{eq:nonlinearresolvent}
\end{equation}
```
Put $`A=(m+1)B^mG_0`$. The map preserves this interval if $`\tau B^{m+1}G_0/\lambda\leq b_\circ`$, and contracts in the supremum norm with factor $`\eta=\tau A/\lambda`$. Impose $`\eta\leq1/2`$. Its unique fixed point, denoted $`\widehat b_{\tau,z}`$, is Lipschitz: iteration from the constant $`b_\circ`$, using flow separation $`e^{Lt}`$, gives
``` math
\operatorname{Lip}(\mathcal T_{\tau,z}b)
 \leq\frac{\tau}{\lambda-L}
       \{A\operatorname{Lip}(b)+B^{m+1}G_1\}.
```
Imposing also $`\tau A/(\lambda-L)\leq1/2`$ gives
``` math
\begin{equation}
 \operatorname{Lip}(\widehat b_{\tau,z})
 \leq\frac{2\tau B^{m+1}G_1}{\lambda-L}.\label{eq:blip}
\end{equation}
```
Uniform convergence of the iterates preserves this bound.

*Dependence on elevation.* For $`e=\|\nabla z-\nabla w\|_\infty`$, Gronwall gives $`|X_z(t,x)-X_w(t,x)|\leq e\int_0^t e^{L(t-s)}\,\mathrm ds`$. Let $`H_*`$ be a uniform Lipschitz bound for $`\widehat b_{\tau,w}^{m+1}G_w`$ on the selected small $`\tau`$ interval; <a href="#eq:blip" data-reference-type="eqref" data-reference="eq:blip">[eq:blip]</a> supplies one. Splitting the fixed-point difference into multiplier, gradient and trajectory differences yields
``` math
(1-\eta)\|\widehat b_{\tau,z}-\widehat b_{\tau,w}\|_\infty
 \leq\tau\left\{\frac{B^{m+1}C_\sigma}{\lambda}
            +\frac{H_*}{\lambda(\lambda-L)}\right\}e.
```
Here the second denominator follows by integrating $`e^{-\lambda t}\int_0^t e^{L(t-s)}\,\mathrm ds`$ over $`t>0`$. Consequently
``` math
\begin{equation}
 \|\widehat b_{\tau,z}-\widehat b_{\tau,w}\|_\infty
 \leq C_b\tau\|z-w\|_{C^1}.\label{eq:bstability}
\end{equation}
```
Since $`b\mapsto b^m`$ is Lipschitz on $`[b_\circ,B]`$, including when $`m<1`$, $`g_{\tau,z}=\widehat b_{\tau,z}^{m}G_z`$ satisfies $`\|g_{\tau,z}-g_{\tau,w}\|_\infty\leq C_g\|z-w\|_{C^1}`$ with $`C_g`$ uniform for small $`\tau`$. It also has a uniform Lipschitz norm.

*Poisson contraction.* Define
``` math
\begin{equation}
 \widehat{\mathcal F}_{\tau}(z)=z_0-\tau P g_{\tau,z}.
 \label{eq:contractivepoisson}
\end{equation}
```
Uniform $`C^{0,\alpha}`$ bounds on $`g`$ and the Schauder estimate make this a self-map of $`\mathcal C`$ for small $`\tau`$. The estimate $`\|Pf\|_{C^1}\leq C_E\|f\|_\infty`$ follows from Dirichlet $`W^{2,p}`$ regularity with a finite $`p>d`$ and Sobolev embedding. Thus the map contracts in $`C^1`$ with $`Q=\tau C_EC_g`$; reduce $`\tau`$ so $`Q\leq1/2`$. Banach’s theorem proves existence and convergence of the outer iteration on the complete metric space $`\mathcal C`$.

*Equivalence and uniqueness.* The multiplier identity implies, along characteristics,
``` math
-\nabla z\cdot\nabla b+\lambda b=\rho+\tau b^{m+1}G_z.
```
At the Poisson fixed point $`-\Delta z=\lambda-\tau b^mG_z`$. Combining these equations gives $`\operatorname{div}(-b\nabla z)=\rho`$ in distributions, and the Poisson equation is exactly the steady erosion equation. The constructed Lipschitz multiplier justifies this calculation almost everywhere.

Conversely, any pair in the stated class obeys the characteristic identity. Indeed, away from zeros of the $`C^1`$ vector field, a flow-box change of variables turns the distributional transport equation into a one-dimensional equation with continuous right side, including the flow Jacobian. Integration first for almost every transverse coordinate, then continuity, gives the identity on every trajectory. At zeros the critical-point rescaling argument gives $`(-\Delta z)b=\rho`$. The original resolvent and $`-\Delta z\geq\lambda/2`$ imply $`b\leq B`$. The steady equation also gives $`-\Delta z\leq\lambda`$, so $`b\geq b_\circ`$. Rewriting the transport equation with constant damping $`\lambda`$ and letting its bounded terminal term tend to zero gives <a href="#eq:nonlinearresolvent" data-reference-type="eqref" data-reference="eq:nonlinearresolvent">[eq:nonlinearresolvent]</a>. Hence its multiplier and elevation are precisely the two unique fixed points.

*Parameter dependence.* For fixed $`z`$, subtraction of the multiplier fixed-point equations at $`\tau,\tau'`$ and absorption of $`\eta`$ give $`\|\widehat b_{\tau,z}-\widehat b_{\tau',z}\|_\infty\leq C|\tau-\tau'|`$. The same bound holds for the Poisson maps in $`C^1`$. Absorbing their uniform contraction factor $`Q`$ proves Lipschitz dependence of the fixed elevation; <a href="#eq:bstability" data-reference-type="eqref" data-reference="eq:bstability">[eq:bstability]</a> then proves it for the multiplier. Since $`D`$ is fixed, these are also Lipschitz bounds in $`K`$. ◻

</div>

<div class="remark">

*Remark 7* (A checkable nonradial geometry). For the ellipsoid $`\sum_i x_i^2/A_i^2<1`$,
``` math
z_0=\frac{\lambda(1-\sum_i x_i^2/A_i^2)}{2\sum_i A_i^{-2}},\qquad
 L_0=\lambda\frac{\max_i A_i^{-2}}{\sum_i A_i^{-2}}<\lambda\quad(d\geq2).
```
Thus all such ellipsoids satisfy the hypothesis. Elongation can make the margin small; no uniform threshold over all aspect ratios is claimed. For the ellipse $`x^2/4+y^2<1`$ used below, $`L_0/\lambda=4/5`$ and $`(\lambda-L_0)/\lambda=1/5`$. These ratios verify the torsion-flow hypothesis only; they do not instantiate the invariant-ball radius, the Poisson constants or an admissible numerical $`K_*`$. On a convex domain the trajectory estimates and their integrability denominators can instead use a uniform one-sided flow-growth rate $`\mu<\lambda`$, while the spatial Lipschitz bounds for $`G_z`$ retain an ordinary Lipschitz constant for $`\nabla z`$. Such a growth rate follows, for example, from $`D^2z\leq\mu I`$ throughout the invariant ball. Strict concavity of $`z_0`$ therefore suffices, including on an interval. On a nonconvex domain that pointwise Hessian inequality alone does not give the required global pairwise trajectory estimate.

</div>

<div id="prop:smallness" class="proposition">

**Proposition 8** (A consolidated sufficient smallness choice). *Fix the invariant ball $`\mathcal C`$ of radius $`\varepsilon`$ and its constants from Theorem <a href="#thm:localunique" data-reference-type="ref" data-reference="thm:localunique">6</a>. Let $`C_S`$ satisfy $`\|Pf\|_{C^{2,\alpha}}\leq C_S\|f\|_{C^{0,\alpha}}`$, and put
``` math
\overline\tau=\min\left\{
 \frac{\lambda b_\circ}{B^{m+1}G_0},\frac{\lambda}{2A},
 \frac{\lambda-L}{2A}\right\},\qquad
 M_m=m\max(b_\circ^{m-1},B^{m-1}).
```
Define the following constants independently of $`0\leq\tau\leq\overline\tau`$:
``` math
\begin{align*}
 L_b&=\frac{2\overline\tau B^{m+1}G_1}{\lambda-L},&
 H_*&=A L_b+B^{m+1}G_1,\\
 C_b&=2\left\{\frac{B^{m+1}C_\sigma}{\lambda}
             +\frac{H_*}{\lambda(\lambda-L)}\right\},&
 C_g&=B^mC_\sigma+M_mG_0C_b\overline\tau,\\
 J&=M_mG_0L_b+B^mG_1,&
 G_\alpha&=B^mG_0+J\operatorname{diam}(\Omega)^{1-\alpha}.
\end{align*}
```
Then a sufficient choice is
``` math
0\leq K\leq D\min\left\{\overline\tau,
       \frac{\varepsilon}{C_SG_\alpha},\frac1{2C_EC_g}\right\}.
```*

</div>

<div class="proof">

*Proof.* The three bounds defining $`\overline\tau`$ give multiplier-interval invariance, $`\eta\leq1/2`$, and the Lipschitz-iteration bound, respectively. Equation <a href="#eq:blip" data-reference-type="eqref" data-reference="eq:blip">[eq:blip]</a> gives $`L_b`$; the elevation-difference estimate then gives the displayed $`C_b,C_g`$. The forcing has supremum norm at most $`B^mG_0`$ and Lipschitz constant at most $`J`$, hence Hölder norm at most $`G_\alpha`$. The last two smallness bounds make the Poisson map preserve $`\mathcal C`$ and give $`Q\leq1/2`$. ◻

</div>

This consolidates sufficient analytical inequalities; it is not a numerical instantiation of their domain-dependent constants or a channelization threshold.

<div id="cor:posteriori" class="corollary">

**Corollary 9** (Continuum residual bounds). *Use the constants $`\eta,Q<1`$ and $`C_b,C_E`$ from the preceding proof. For an approximate $`z\in\mathcal C`$ and continuous $`b_\circ\leq b\leq B`$, put
``` math
e_b=\|b-\mathcal T_{\tau,z}b\|_\infty,\qquad
 e_z=\|z-z_0+\tau P(b^mG_z)\|_{C^1},\qquad
 M_m=m\max(b_\circ^{m-1},B^{m-1}).
```
The unique exact pair $`(z_*,b_*)`$ satisfies
``` math
\|z-z_*\|_{C^1}\leq
 \frac{e_z+\tau C_E M_mG_0 e_b/(1-\eta)}{1-Q},\qquad
 \|b-b_*\|_\infty\leq\frac{e_b}{1-\eta}+C_b\tau\|z-z_*\|_{C^1}.
```*

</div>

<div class="proof">

*Proof.* The inner contraction gives $`\|b-\widehat b_{\tau,z}\|_\infty\leq e_b/(1-\eta)`$. Replacing $`b`$ by $`\widehat b_{\tau,z}`$ changes the Poisson term by at most $`\tau C_EM_mG_0e_b/(1-\eta)`$. Apply the outer contraction residual estimate, then <a href="#eq:bstability" data-reference-type="eqref" data-reference="eq:bstability">[eq:bstability]</a>. ◻

</div>

These are continuum norms. A numerical certificate additionally requires bounds for discretization, flow integration, the infinite tail, and membership in the invariant set. Finite-grid residuals alone do not meet those requirements.

<div id="cor:inexact" class="corollary">

**Corollary 10** (Inexact nesting and a finite inner stopping rule). *Fix $`\tau>0`$ in the preceding range and let $`\eta,Q<1`$ be uniform contraction factors. Suppose each approximate elevation $`z_j`$ belongs to $`\mathcal C`$. For its inner solve, use an interval-preserving approximation $`\widetilde{\mathcal T}_j`$ to $`\mathcal T_{\tau,z_j}`$, with error at most $`\delta_j`$ at every evaluated inner iterate. Given $`r_j>0`$, require
``` math
\delta_j\leq(1-\eta)r_j/4.
```
Starting from $`b^0=b_\circ`$, iterate $`b^{k+1}=\widetilde{\mathcal T}_jb^k`$ and stop when $`\|b^{k+1}-b^k\|_\infty\leq r_j`$; retain $`b_j=b^k`$. This stopping condition is reached after finitely many steps. If
``` math
\pi_j\geq\|z_{j+1}-z_0+\tau P(b_j^mG_{z_j})\|_{C^1},\qquad
 \xi_j=\pi_j+\frac{\tau C_EM_mG_0}{1-\eta}(r_j+\delta_j),
```
then, for $`E_j=\|z_j-z_*\|_{C^1}`$,
``` math
E_{j+1}\leq QE_j+\xi_j,\qquad
 E_j\leq Q^jE_0+\sum_{i=0}^{j-1}Q^{j-1-i}\xi_i.
```
In particular, $`\xi_j\leq C\theta^j`$ with $`0<\theta<1`$ gives convergence; when $`\theta=Q`$ the sum is at most $`CjQ^{j-1}`$.*

</div>

<div class="proof">

*Proof.* Writing $`d_k=\|b^k-\widehat b_{\tau,z_j}\|_\infty`$ gives $`d_k\leq\eta^kd_0+\delta_j/(1-\eta)`$. Hence
``` math
\|b^{k+1}-b^k\|_\infty
 \leq(1+\eta)\eta^kd_0+\frac{2\delta_j}{1-\eta}
 \leq(1+\eta)\eta^kd_0+r_j/2.
```
Here $`d_0\leq B-b_\circ`$, so any $`k`$ with $`(1+\eta)\eta^k(B-b_\circ)\leq r_j/2`$ guarantees the stopping test. At stopping, the exact inner residual is at most $`r_j+\delta_j`$. The inner contraction and the Poisson bound therefore give $`\|z_{j+1}-\widehat{\mathcal F}_\tau(z_j)\|_{C^1}\leq\xi_j`$. The outer contraction proves the recurrence; induction proves its sum. For $`\tau=0`$ the exact solution is already $`z_0,b_\circ`$. ◻

</div>

The inner error can be budgeted without conflating its sources. For a truncated flow integral at time $`T_j`$, let $`e_{X,j}`$ bound the error from approximate trajectories and $`e_{I,j}`$ the quadrature and integrand-representation error, both in the supremum norm of the multiplier map and including its factor $`\tau`$. Then one may use
``` math
\delta_j=e_{X,j}+e_{I,j}
       +\frac{\tau B^{m+1}G_0}{\lambda}e^{-\lambda T_j}.
```
Pointwise clipping of the computed map to $`[b_\circ,B]`$ preserves this error bound, since the exact map takes values in that interval. The distinct error $`\pi_j`$ covers the Poisson solve, spatial representation and any subsequent modification of the elevation. Thus geometrically decreasing $`r_j,\delta_j`$ and $`\pi_j`$, subject to the displayed inner-error inequality, give the stated convergent finite-tolerance construction. An implementation must bound the continuum norms used in its stopping test; sampled norms alone are insufficient. It must also keep every $`z_j`$ in $`\mathcal C`$: small $`C^1`$ errors do not by themselves ensure membership of a $`C^{2,\alpha}`$ ball. Any admissibility correction must be accounted for in $`\pi_j`$. No such verified implementation or instantiated error budget is claimed for the collocation experiment below.

# Response at zero erosion and a nonradial exact check

<div id="cor:response" class="corollary">

**Corollary 11** (First-order elevation response). *For any family of the solutions furnished by Theorem <a href="#thm:general" data-reference-type="ref" data-reference="thm:general">4</a>, as $`K\downarrow0`$,
``` math
\begin{equation}
 z_K=z_0-\frac K D P\big(b_0^m|\nabla z_0|^{m+n}\big)+o(K)
 \quad\text{in }C^{2,\beta},\quad 0<\beta<\alpha,\label{eq:response}
\end{equation}
```
where $`b_0`$ is the resolvent <a href="#eq:resolvent" data-reference-type="eqref" data-reference="eq:resolvent">[eq:resolvent]</a> for $`z_0`$. The first-order coefficient is independent of which small-$`K`$ steady solution is selected.*

</div>

<div class="proof">

*Proof.* The norm estimate gives $`z_K\to z_0`$. The continuity proved above gives $`g_{z_K}\to g_{z_0}`$ in $`C^{0,\beta}`$. Divide <a href="#eq:fixedmap" data-reference-type="eqref" data-reference="eq:fixedmap">[eq:fixedmap]</a> by $`K`$ and use the continuous Poisson inverse. ◻

</div>

For $`D=U=\rho=1`$ one has $`-\Delta z_0=1`$ and $`b_0=1`$. With $`p_0=m+n`$, the spatial shape of the first correction is $`P(|\nabla z_0|^{p_0})`$. Moreover,
``` math
\begin{equation}
 b_K=1+K b_1+o(K),\qquad
 b_1(x)=\int_0^\infty e^{-t}|\nabla z_0(X_0(t,x))|^{p_0}\,\mathrm dt,\label{eq:bresponse}
\end{equation}
```
in $`C^{0,\beta}`$. Indeed, $`\delta_K=1-Kg_{z_K}`$ in <a href="#eq:resolvent" data-reference-type="eqref" data-reference="eq:resolvent">[eq:resolvent]</a>; expanding its exponential proves the formula uniformly. The bounds for $`(b_K-1)/K`$ in $`C^{0,\alpha}`$ follow from <a href="#eq:holderb" data-reference-type="eqref" data-reference="eq:holderb">[eq:holderb]</a> and $`\delta_K-1=-Kg_{z_K}`$, and interpolation gives the stated topology.

As an exactly checkable nonradial example, take $`\Omega=\{x^2/4+y^2<1\}`$, $`D=U=\rho=1`$ and $`m=n=1`$. Then
``` math
\begin{align}
 z_0&=\frac25-\frac{x^2}{10}-\frac{2y^2}{5},\qquad
 g_0=\frac{x^2+16y^2}{25},\nonumber\\
 W&=\frac{(1-x^2/4-y^2)(44+3x^2+52y^2)}{1025},\label{eq:ellipse}\\
 b_1&=\frac{x^2}{35}+\frac{16y^2}{65}.\nonumber
\end{align}
```
Direct differentiation gives $`-\Delta W=g_0`$, $`W|_{\partial\Omega}=0`$, and $`-\nabla z_0\cdot\nabla b_1+b_1=g_0`$. Thus $`z=z_0-KW+o(K)`$ and $`b=1+Kb_1+o(K)`$. Substitution of the truncated pair into both coupled equations has zero coefficients at orders $`K^0`$ and $`K^1`$. The supplied script checks these rational polynomial identities exactly. This is not an exact finite-$`K`$ landscape; the truncation has a generally nonzero $`K^2`$ residual.

## Finite-erosion numerical refinement

For the same ellipse, write $`x=2u`$, $`y=v`$ and approximate $`z=(1-u^2-v^2)\sum_{i+j\leq N}a_{ij}u^{2i}v^{2j}`$ and $`b=\sum_{i+j\leq N}b_{ij}u^{2i}v^{2j}`$. The boundary elevation vanishes exactly. An analytic-Jacobian least-squares solve enforces the two stationary equations on a collocation grid. Table <a href="#tab:nonradial" data-reference-type="ref" data-reference="tab:nonradial">3</a> reports maximum absolute residuals on a separate staggered grid of 1,457 interior points, at $`K=0.2`$. The supplied code also checks $`K=0.025,0.05,0.1`$.

<div id="tab:nonradial">

| $`N`$ |           Bed residual |          Area residual |
|:-----:|-----------------------:|-----------------------:|
|   2   |  $`1.49\times10^{-5}`$ |  $`1.39\times10^{-5}`$ |
|   3   |  $`1.17\times10^{-7}`$ |  $`9.57\times10^{-8}`$ |
|   4   | $`7.83\times10^{-10}`$ | $`9.56\times10^{-10}`$ |

Independent-grid residual refinement for an approximate nonradial steady state. Values are rounded upward.

</div>

The $`N=4`$ summit is approximately $`0.39155525`$, compared with the zero-erosion value $`0.4`$. Its discrepancy from the exact first-order response on the test grid is $`1.45\times10^{-4}`$; at $`K=0.1`$ it is $`3.65\times10^{-5}`$, consistent with a quadratic correction. Separately, treating the saved version 1.2 decimal coefficient strings as exact rationals, the coefficient $`\ell^1`$ bound on $`[-1,1]^2`$ proves whole-ellipse bounds for the $`N=4`$, $`K=0.2`$ polynomial:
``` math
\|R_{\rm bed}\|_\infty<2.81\times10^{-6},\quad
 \|R_{\rm area}\|_\infty<2.76\times10^{-6},\quad
 b>0.9263,\quad-\Delta z>0.8269.
```
The boundary factor of $`z`$ is positive, and its boundary value is exactly zero. The bounds follow by summing absolute nonconstant coefficients, using $`|u|,|v|\leq1`$; the accompanying exact-rational checker reproduces them. They bound the specified polynomial residuals, not its error from a true solution or membership in the contraction ball.

These are floating-point, finite-grid diagnostics. They neither verify membership in the theorem’s invariant ball nor show that the selected parameters lie below $`K_*`$. The solver is not the proved contraction iteration, and these residuals do not supply the continuum norms required by Corollary <a href="#cor:posteriori" data-reference-type="ref" data-reference="cor:posteriori">9</a>.

# All-parameter radial steady states

Here $`\Omega=B_R`$, $`U>0`$ is constant and $`\rho=1`$. Write $`r=|x|`$ and seek a strictly downhill radial elevation, with slope $`s=-z'(r)>0`$.

<div id="thm:radial" class="theorem">

**Theorem 12** (Radial existence, uniqueness and summit regularity). *For every $`d\geq1`$, $`R,D,K,U>0`$, and $`m,n>0`$, there is exactly one regular downhill radial steady solution without an interior point source. It has
``` math
\begin{equation}
 a(r)=r/d,\quad q(x)=x/d,\quad
 z(r)=\int_r^R s(t)\,\mathrm dt,\label{eq:radialflux}
\end{equation}
```
where $`s`$ is the positive solution of
``` math
\begin{equation}
 D\left(s'+\frac{d-1}{r}s\right)+\frac K{d^m}r^m s^n=U,\qquad s(0)=0.\label{eq:slope}
\end{equation}
```
Put $`A=U/(dD)`$ and $`\sigma=m+n`$. Then
``` math
\begin{align}
 0<s(r)&\leq Ar,\qquad
 0\leq z(r)\leq\frac{U}{2dD}(R^2-r^2),\label{eq:radialbounds}\\
 s(r)&=Ar-Br^{\sigma+1}+o(r^{\sigma+1}),\qquad
 B=\frac{KA^n}{Dd^m(d+m+n)}.\label{eq:summit}
\end{align}
```
The elevation is strictly positive for $`r<R`$. In particular, $`z\in C^{2,\gamma}(\overline B_R)`$ for every $`0<\gamma<\min\{1,m+n\}`$, and is smooth away from the summit. The steady slope and elevation increase with $`U`$ and decrease with $`K`$.*

</div>

<div class="proof">

*Proof.* The flux conservation law gives $`(r^{d-1}a)'=r^{d-1}`$. Its integration constant is zero: a nonzero constant is a point flux at the origin (or a nonzero central flux in the one-dimensional symmetric formulation). Hence $`a=r/d`$ and $`q=x/d`$. The elevation equation is <a href="#eq:slope" data-reference-type="eqref" data-reference="eq:slope">[eq:slope]</a>.

Set $`c_0=K/(Dd^m)`$ and $`s=rw`$. The integral equation is
``` math
\begin{equation}
 w(r)=A-c_0r^{-d}\int_0^r t^{d+m+n-1}w(t)^n\,\mathrm dt.\label{eq:volterra}
\end{equation}
```
On a sufficiently short interval this is a contraction on continuous functions with $`A/2\leq w\leq3A/2`$. The power function is Lipschitz on this positive interval, even when $`n<1`$, and the contraction factor is $`O(r^{m+n})`$. It follows that $`s>0`$ near zero. A first zero at positive $`r`$ is impossible because the ODE would give $`s'=U/D>0`$. Integrating the ODE after multiplication by $`r^{d-1}`$ proves $`s\leq Ar`$. Standard ODE continuation on intervals bounded away from zero now extends the solution to every finite radius.

For two positive regular solutions, $`\delta_s=s_1-s_2`$ satisfies
``` math
\frac{\mathrm d}{\mathrm dr}\left(\tfrac12r^{2(d-1)}\delta_s^2\right)
 =-c_0r^{2(d-1)+m}\delta_s(s_1^n-s_2^n)\leq0.
```
The expression tends to zero at the origin, proving uniqueness. Substitution of $`w\to A`$ in <a href="#eq:volterra" data-reference-type="eqref" data-reference="eq:volterra">[eq:volterra]</a> gives <a href="#eq:summit" data-reference-type="eqref" data-reference="eq:summit">[eq:summit]</a>. More explicitly, the integral equation and its differentiated ODE give $`w-A=O(r^\sigma)`$, $`w'=O(r^{\sigma-1})`$ and $`w''=O(r^{\sigma-2})`$. The elevation Hessian is $`-wI-(w'/r)xx^T`$: its difference from $`-AI`$ is $`O(r^\sigma)`$ and its spatial derivative away from zero is $`O(r^{\sigma-1})`$. Splitting pairs of points according to whether their separation is smaller than their distance from zero proves the asserted $`C^{2,\gamma}`$ regularity for every $`\gamma<\min(1,\sigma)`$. Integrating the slope gives <a href="#eq:radialbounds" data-reference-type="eqref" data-reference="eq:radialbounds">[eq:radialbounds]</a>. Scalar first-crossing comparison in <a href="#eq:slope" data-reference-type="eqref" data-reference="eq:slope">[eq:slope]</a>, using the leading term or <a href="#eq:summit" data-reference-type="eqref" data-reference="eq:summit">[eq:summit]</a> at the origin, proves parameter monotonicity. ◻

</div>

<div class="remark">

*Remark 13* (No hidden radial minima). In the regular radial class with finite continuous area and no point flux, the summit Hessian is $`-U/(dD)`$ times the identity. If a downhill derivative first returned to zero at $`r>0`$, the steady elevation equation there would force $`z''=-U/D<0`$, contradicting that first return. Thus regular radial states in this class are downhill; the theorem is not merely uniqueness under an arbitrary prescribed slope sign. It says nothing about uniqueness among nonradial states.

</div>

For $`n=1`$ there is a useful closed quadrature:
``` math
\begin{equation}
 s(r)=\frac UD\frac{\displaystyle\int_0^r t^{d-1}
 \exp\!\left(\frac{Kt^{m+1}}{Dd^m(m+1)}\right)\,\mathrm dt}
 {\displaystyle r^{d-1}\exp\!\left(\frac{Kr^{m+1}}{Dd^m(m+1)}\right)}.\label{eq:quadrature}
\end{equation}
```
The $`d=1`$, $`m=n=1`$ member is the familiar Dawson-function hillslope, not a new special case; compare .

# Global evolution and relaxation in the radial class

<div id="thm:dynamic" class="theorem">

**Theorem 14** (Global monotone radial evolution). *Assume $`m>0`$, $`n\geq1`$, and $`D,K,U,R>0`$. Let $`z_{\rm in}`$ be a nonincreasing radial $`C^{2,\alpha}`$ function on $`\overline B_R`$, with $`z_{\rm in}(R)=0`$, regular center, and the classical compatibility condition
``` math
D\left(z_{\rm in}''(R)+\frac{d-1}{R}z_{\rm in}'(R)\right)
 -K(R/d)^m|z_{\rm in}'(R)|^n+U=0.
```
Here $`\alpha>0`$ may be decreased below $`\min(1,m)`$. Then the radial equation
``` math
\begin{equation}
 z_t=D\left(z_{rr}+\frac{d-1}{r}z_r\right)-k(r)|z_r|^n+U,
 \qquad k(r)=K(r/d)^m,\label{eq:radialtime}
\end{equation}
```
has a unique global solution, classical for positive time and continuous with the initial data. It is strictly downhill for $`0<r\leq R`$, $`t>0`$, and therefore solves the coupled system with $`a=r/d`$, $`q=x/d`$.*

*Let $`s_{\rm in}=-z_{\rm in}'`$, $`c=\sup_{0<r\leq R}s_{\rm in}(r)/r`$, and choose
``` math
\begin{equation}
 \overline U>\max\{U,\ dDc+(K/d^m)c^nR^{m+n}\}.\label{eq:Ubar}
\end{equation}
```
If $`S`$ is the steady slope in Theorem <a href="#thm:radial" data-reference-type="ref" data-reference="thm:radial">12</a> with uplift $`\overline U`$, then
``` math
\begin{equation}
 0\leq -z_r(t,r)\leq S(r)\leq\frac{\overline U}{dD}r\qquad(t\geq0).\label{eq:globalgrad}
\end{equation}
```
Writing $`z_*`$ for the steady state with the actual uplift $`U`$,
``` math
\begin{equation}
 |z(t,r)-z_*(r)|\leq C_{\rm in}e^{-2dDt/R^2}(R^2-r^2),\label{eq:rate}
\end{equation}
```
where $`C_{\rm in}=\sup_{r<R}|z_{\rm in}(r)-z_*(r)|/(R^2-r^2)<\infty`$.*

</div>

<div class="proof">

*Proof.* *Local solution and positivity.* Work first on the Cartesian ball, with $`k(x)=K(|x|/d)^m`$ and $`F(x,p)=U-k(x)|p|^n`$. Let $`E=\{u\in C^1(\overline B_R):u|_{\partial B_R}=0\}`$ with its $`C^1`$ norm. On each bounded subset of $`E`$, $`F(x,\nabla u)`$ is Lipschitz in $`u`$ as a map into $`C(\overline B_R)`$, including $`n=1`$. If $`S_D(t)`$ is the Dirichlet heat semigroup, its estimates
``` math
\|S_D(t)f\|_\infty\leq C\|f\|_\infty,\qquad
 \|\nabla S_D(t)f\|_\infty\leq C t^{-1/2}\|f\|_\infty
 \quad(0<t\leq1)
```
make the Duhamel map a contraction on a ball in $`C([0,T];E)`$: its Lipschitz constant is at most $`C_M(T+2\sqrt T)`$. The homogeneous heat evolution is bounded in $`E`$ for initial data in $`E`$. Thus the existence time is bounded below on bounded $`C^1`$ sets, and a finite maximal time requires an unbounded $`C^1`$ norm. This is the concrete heat-semigroup implementation of the local and continuation framework of .

For clarity, regularity precedes differentiation of the slope equation. On a compact positive-time interval the bounded forcing and heat smoothing first give spatial and temporal Hölder regularity of $`\nabla z`$ with some exponent $`\theta>0`$. Since $`k`$ is $`C^{0,\alpha}`$ for $`\alpha<\min(1,m)`$ and $`|p|^n`$ is locally Lipschitz, the composed forcing is parabolically Hölder after reducing the exponent. Interior and Dirichlet boundary Schauder regularity then give $`z\in C^{2+\theta,1+\theta/2}`$ on smaller positive-time cylinders. The stated initial compatibility and $`C^{2,\alpha}`$ data give the corresponding regularity through $`t=0`$ locally. In particular a bounded Hessian and radial symmetry imply $`z_r(t,0)=0`$ and $`s(t,r)=O(r)`$ uniformly on compact local-existence time intervals. After strict decrease is established, $`s>0`$ on every closed annulus; there $`k`$ and $`s^n`$ are smooth and parabolic bootstrapping justifies the classical differentiated equation below. No differentiation of $`|p|`$ at $`p=0`$ is used for $`n=1`$. Positivity follows by the maximum principle, since the gradient term vanishes at an interior minimum and $`U>0`$.

*Preservation and strictness of radial decrease.* Rotation invariance and uniqueness preserve radial symmetry. Reflect an outer spherical cap $`\{x_1>\lambda\}\cap B_R`$, $`\lambda>0`$, across $`x_1=\lambda`$. The reflected point has smaller radius, so its $`k`$ is no larger. The difference “inner reflected elevation minus outer elevation” satisfies a linear parabolic inequality with bounded drift and nonnegative forcing, obtained by the Lipschitz difference of the gradient nonlinearities. Its initial and parabolic boundary values are nonnegative. The maximum principle preserves their ordering. Strong comparison and the boundary point lemma on the reflection plane give $`z_r<0`$ at every positive interior radius and positive time. The boundary point lemma for $`z`$ gives the same conclusion at $`R`$. These arguments are applied on finite local-existence intervals, where the gradient is bounded.

*A stationary upper envelope for the slope.* Set $`s=-z_r`$. On $`r>0`$, strict positivity permits differentiation, giving the important sign convention
``` math
\begin{equation}
 s_t=D\left(s_{rr}+\frac{d-1}{r}s_r-\frac{d-1}{r^2}s\right)
       +k's^n+nk s^{n-1}s_r.\label{eq:slopetime}
\end{equation}
```
Both nonlinear terms have a plus sign. A naive assertion that a positive interior slope maximum can never grow would therefore be false. At $`R`$, the fixed elevation yields
``` math
\begin{equation}
 D\left(s_r+\frac{d-1}{R}s\right)+k(R)s^n=U.\label{eq:slopeboundary}
\end{equation}
```
The stationary slope $`S`$ for $`\overline U`$ solves the same interior equation <a href="#eq:slopetime" data-reference-type="eqref" data-reference="eq:slopetime">[eq:slopetime]</a> and has the right side $`\overline U`$ in <a href="#eq:slopeboundary" data-reference-type="eqref" data-reference="eq:slopeboundary">[eq:slopeboundary]</a>. Condition <a href="#eq:Ubar" data-reference-type="eqref" data-reference="eq:Ubar">[eq:Ubar]</a> and a first-crossing comparison with $`cr`$ in its first-order ODE give $`S\geq cr\geq s_{\rm in}`$.

Here is a center-safe comparison proof for $`s\leq S`$, including $`m+n<2`$. On any compact local-existence time interval, $`s=O(r)`$, $`S\asymp r`$. The difference $`e=s-S`$ solves
``` math
e_t=D\mathcal L e+B(t,r)e_r+C(t,r)e,
 \quad\mathcal L=\partial_{rr}+\frac{d-1}{r}\partial_r-\frac{d-1}{r^2},
```
where, near zero,
``` math
|B(t,r)|\leq C_T r^{m+n-1},\qquad
 |C(t,r)|\leq C_T r^{m+n-2}.
```
These bounds follow from secants of $`s^n`$ and $`s^{n-1}`$; the latter secant is taken against the strictly positive $`S\asymp r`$. They remain valid for $`1<n<2`$. Indeed, write $`s=ra`$ and $`S=rb`$, where $`a`$ is bounded and nonnegative and $`b`$ is bounded above and below by positive constants. The divided difference of $`u^{n-1}`$ between $`a`$ and $`b`$ is bounded on this set, even if $`a=0`$. For $`n=1`$ that divided difference is zero. At $`R`$, $`De_r+\beta(t)e=U-\overline U<0`$, where $`\beta(t)\geq0`$. Choose $`0<\gamma<1`$ and $`\psi(r)=r^\gamma`$. Then
``` math
\frac{D\mathcal L\psi+B\psi'+C\psi}{\psi}
 =\frac{D(\gamma-1)(\gamma+d-1)}{r^2}+O(r^{m+n-2})
```
is bounded above: its leading singular term is negative. Thus $`\varepsilon e^{Mt}\psi`$ is a strict supersolution for sufficiently large $`M`$, and it satisfies the positive Robin inequality at $`R`$. Since $`e=O(r)`$, $`e/\psi\to0`$ at the center uniformly on the time interval. First-contact comparison therefore occurs neither at the center nor at the outer boundary, and the interior maximum principle gives $`e\leq\varepsilon e^{Mt}\psi`$. Letting $`\varepsilon\downarrow0`$ proves $`s\leq S`$. Theorem <a href="#thm:radial" data-reference-type="ref" data-reference="thm:radial">12</a> now gives <a href="#eq:globalgrad" data-reference-type="eqref" data-reference="eq:globalgrad">[eq:globalgrad]</a>.

*Continuation.* Integrating the bounded slope from $`R`$ also bounds the elevation. The local semilinear continuation criterion excludes a finite maximal time. This proves global existence; uniqueness is inherited from local comparison.

*Relaxation.* Let $`w=z-z_*`$. Since both slopes are nonnegative,
``` math
w_t=D\Delta_rw+B_*(t,r)w_r,\qquad
 B_*=k(r)\frac{s^n-s_*^n}{s-s_*}\geq0.
```
Use the continuous secant at equality. The coefficient is bounded by <a href="#eq:globalgrad" data-reference-type="eqref" data-reference="eq:globalgrad">[eq:globalgrad]</a> and $`n\geq1`$. For $`\phi=R^2-r^2`$,
``` math
(D\Delta_r+B_*\partial_r)\phi=-2dD-2B_*r
 \leq-\frac{2dD}{R^2}\phi.
```
Comparison with $`\pm C_{\rm in}e^{-2dDt/R^2}\phi`$ proves <a href="#eq:rate" data-reference-type="eqref" data-reference="eq:rate">[eq:rate]</a>. The boundary quotient in $`C_{\rm in}`$ is finite because the initial and steady elevations vanish at $`R`$ and have bounded slopes. ◻

</div>

<div class="remark">

*Remark 15* (Stability is radial only). The theorem does not suppress transverse channelization. The contributing area stays $`r/d`$ because the flow geometry is held within the invariant radial class. The general nonradial evolution is not reduced to <a href="#eq:radialtime" data-reference-type="eqref" data-reference="eq:radialtime">[eq:radialtime]</a>. Nor is the theorem stated for $`0<n<1`$, where the gradient Hamiltonian is not locally Lipschitz at zero. The displayed decay exponent tends to zero as $`D\downarrow0`$; the estimate is not uniform in vanishing diffusion and does not justify exchanging the long-time and zero-diffusion limits.

</div>

<div id="cor:contraction" class="corollary">

**Corollary 16** (Contraction between radial solutions). *Let $`\lambda_1`$ and $`\Phi`$ be the first Dirichlet eigenvalue and positive radial eigenfunction of $`-\Delta`$ on $`B_R`$, with $`\Phi(0)=1`$. For any two solutions of Theorem <a href="#thm:dynamic" data-reference-type="ref" data-reference="thm:dynamic">14</a> with the same parameters,
``` math
\sup_{0\leq r<R}\frac{|z_1(t,r)-z_2(t,r)|}{\Phi(r)}
 \leq e^{-D\lambda_1t}
 \sup_{0\leq r<R}\frac{|z_1(0,r)-z_2(0,r)|}{\Phi(r)}.
```
Taking $`z_2=z_*`$ gives relaxation at rate $`D\lambda_1>2dD/R^2`$. The weighted initial constant is the displayed quotient, not $`C_{\rm in}`$ from the quadratic-weight estimate.*

</div>

<div class="proof">

*Proof.* The difference satisfies $`w_t=D\Delta_rw+B w_r`$, where $`B=k(s_1^n-s_2^n)/(s_1-s_2)\geq0`$ is bounded, using the continuous secant at equality. Near zero $`B=O(r^{m+n-1})\to0`$, so the Cartesian radial drift extends continuously at the centre. The eigenfunction equation gives $`(r^{d-1}\Phi')'=-\lambda_1r^{d-1}\Phi`$, hence $`\Phi'<0`$ for $`r>0`$. Consequently $`(D\Delta_r+B\partial_r)\Phi\leq-D\lambda_1\Phi`$. Comparison with both signs of the exponential barrier proves the estimate. The initial quotient is finite because $`\Phi`$ has a simple boundary zero and both elevations vanish there with bounded derivatives. To compare rates, put $`T=(R^2-r^2)/(2d)`$. Green’s identity gives $`\int\Phi=\lambda_1\int T\Phi<\lambda_1R^2(2d)^{-1}\int\Phi`$. This proves the strict inequality. This contraction remains radial only. ◻

</div>

# Universal small-diffusion profile

Keep $`K,U,R,m,n`$ fixed and let $`D\downarrow0`$. Define
``` math
\begin{equation}
 p=\frac mn,\quad
 \ell=\left(\frac{d^mD^n}{K U^{n-1}}\right)^{1/(m+n)},\quad
 C_0=d^{m/n}(U/K)^{1/n}.\label{eq:scales}
\end{equation}
```
Apart from the geometric factor $`d^{m/(m+n)}`$, the length scale is the known specific-area scale in , after absorbing their grid-width factor into $`K`$. Dimensional analysis alone does not establish the profile, its convergence, or the constants below. Then $`s_D(r)=(U\ell/D)y(r/\ell)`$, where the single universal profile solves
``` math
\begin{equation}
 y'+\frac{d-1}{\rho}y+\rho^m y^n=1,\qquad
 y(\rho)\sim\rho/d\quad(\rho\downarrow0).\label{eq:universal}
\end{equation}
```
It is the positive global solution already proved in Theorem <a href="#thm:radial" data-reference-type="ref" data-reference="thm:radial">12</a>.

<div id="lem:outer" class="lemma">

**Lemma 17** (Outer profile, including its first correction). *For every $`m,n>0`$ and $`d\geq1`$,
``` math
\begin{equation}
 \rho^p y(\rho)=1-\frac{d-1-p}{n}\rho^{-(p+1)}
       +o(\rho^{-(p+1)})\qquad(\rho\to\infty).\label{eq:outer}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Put $`w=\rho^p y`$ and $`c=d-1-p`$. Direct substitution gives
``` math
\begin{equation}
 w'=\rho^p(1-w^n)-\frac c\rho w.\label{eq:wode}
\end{equation}
```
The bound $`y\leq\rho/d`$ implies $`w/\rho\leq\rho^p/d`$. If $`c<0`$, consequently $`w'\leq\rho^p(1+|c|/d-w^n)`$; for $`c\geq0`$ the simpler bound applies. This gives a global upper bound for $`w`$. For any fixed $`\varepsilon>0`$, the vector field at $`1-\varepsilon`$ and $`1+\varepsilon`$ points toward that interval once $`\rho`$ is large. Outside the interval its magnitude is bounded below by a positive multiple of $`\rho^p`$, whose integral diverges. Thus the solution enters and stays in the interval, proving $`w\to1`$.

For the correction put $`a=-c/n`$, $`q=p+1`$, and consider $`W_\pm=1+(a\pm\varepsilon)\rho^{-q}`$. Their residuals in <a href="#eq:wode" data-reference-type="eqref" data-reference="eq:wode">[eq:wode]</a> have respectively the supersolution and subsolution signs, since the leading terms are $`\pm n\varepsilon/\rho`$, while their derivatives and the remaining terms are $`O(\rho^{-p-2})`$. Near one the right side of <a href="#eq:wode" data-reference-type="eqref" data-reference="eq:wode">[eq:wode]</a> is strictly decreasing in $`w`$. If $`w`$ remained above $`W_+`$, its gap derivative would eventually be at most $`-n\varepsilon/(2\rho)`$, an impossibility after integration. The lower barrier is analogous. Both barriers are invariant after entry. Letting $`\varepsilon\downarrow0`$ proves <a href="#eq:outer" data-reference-type="eqref" data-reference="eq:outer">[eq:outer]</a>. ◻

</div>

<div id="lem:outersecond" class="lemma">

**Lemma 18** (Second outer correction). *Put $`p=m/n`$, $`q=p+1`$, $`c=d-1-p`$, and
``` math
A_1=-\frac{c}{n},\qquad
 A_2=\frac{c\{(3-n)c-2q\}}{2n^2}.
```
Then the universal profile satisfies
``` math
\rho^p y(\rho)
 =1+A_1\rho^{-q}+A_2\rho^{-2q}+O(\rho^{-3q}).
```
The constants implicit in the remainder may depend on $`d,m,n`$. If $`c=0`$, the stronger bound $`1-\rho^py(\rho)=O(\exp[-k\rho^q/q])`$ holds for every $`0<k<n`$.*

</div>

<div class="proof">

*Proof.* The previously established convergence $`w=\rho^py\to1`$ and equation $`w'=F(\rho,w)=\rho^p(1-w^n)-cw/\rho`$ are used here. Set $`P=1+A_1\rho^{-q}+A_2\rho^{-2q}`$. Taylor expansion about one is legitimate for every real $`n>0`$, since $`P`$ is bounded away from zero for sufficiently large $`\rho`$. In the residual $`\mathcal R=P'-F(\rho,P)`$, cancellation of the coefficients of $`\rho^{-1}`$ and $`\rho^{-q-1}`$ gives
``` math
nA_1+c=0,\qquad
 nA_2+\frac{n(n-1)}2A_1^2+(c-q)A_1=0.
```
These identities give the displayed coefficients, and $`\mathcal R=O(\rho^{-2q-1})`$. For $`e=w-P`$, the mean-value theorem gives $`e'=a(\rho)e-\mathcal R`$, with $`a(\rho)\leq-k_0\rho^p`$ for some $`k_0>0`$ and all sufficiently large $`\rho`$. Variation of constants therefore bounds $`|e(\rho)|`$ by an exponentially small initial term and
``` math
C\int_{\rho_0}^\rho
 \exp\!\left[-k_0\int_t^\rho u^p\,du\right]t^{-2q-1}\,dt.
```
On $`[\rho_0,\rho/2]`$ the exponential makes the integral exponentially small. On $`[\rho/2,\rho]`$, bound $`t^{-2q-1}`$ by $`C\rho^{-2q-1}`$ and the exponential by $`\exp[-k_0(\rho/2)^p(\rho-t)]`$. The remaining integral is $`O(\rho^{-2q-1-p})=O(\rho^{-3q})`$. When $`c=0`$, the exact equation $`dw/d\tau=1-w^n`$, with $`\tau=\rho^q/q`$ and $`0<w<1`$, gives $`1-w=O(e^{-k\tau})`$ for every $`k<n`$ by the mean-value theorem near one. ◻

</div>

<div id="thm:crest" class="theorem">

**Theorem 19** (Sharp summit classification). *For every fixed $`r\in(0,R]`$,
``` math
s_D(r)\longrightarrow C_0 r^{-p},\qquad
 z_D(r)\longrightarrow C_0\int_r^R t^{-p}\,\mathrm dt.
```
At the summit there are exactly three regimes.
``` math
\begin{align}
 p<1:\quad &z_D(0)\longrightarrow\frac{C_0R^{1-p}}{1-p};\label{eq:crest1}\\
 p=1:\quad &z_D(0)=C_0\{\log(R/\ell)+\mathcal C_{d,m,n}+o(1)\};\label{eq:crest2}\\
 p>1:\quad &z_D(0)\sim\frac{U\ell^2}{D}\,\mathcal J_{d,m,n},\quad
 \mathcal J_{d,m,n}=\int_0^\infty y(\rho)\,\mathrm d\rho\in(0,\infty).\label{eq:crest3}
\end{align}
```
Here
``` math
\mathcal C_{d,m,n}=\lim_{S\to\infty}\left(\int_0^S y(\rho)\,\mathrm d\rho-\log S\right)
```
exists in the critical case. For $`p<1`$, convergence of the elevation is uniform on the closed ball. For $`p>1`$, the power of $`D`$ in <a href="#eq:crest3" data-reference-type="eqref" data-reference="eq:crest3">[eq:crest3]</a> is $`(n-m)/(m+n)`$, explicitly
``` math
\frac{U\ell^2}{D}\mathcal J
 =U\left(\frac{d^m}{KU^{n-1}}\right)^{2/(m+n)}
 \mathcal J\,D^{(n-m)/(m+n)}.
```*

</div>

<div class="proof">

*Proof.* The identity $`C_0=U\ell^{p+1}/D`$ and Lemma <a href="#lem:outer" data-reference-type="ref" data-reference="lem:outer">17</a> give the pointwise slope limit. On compact intervals away from zero it is uniform, so it can be integrated. The exact summit identity is
``` math
\begin{equation}
 z_D(0)=\frac{U\ell^2}{D}\int_0^{R/\ell}y(\rho)\,\mathrm d\rho.\label{eq:crestexact}
\end{equation}
```
When $`p<1`$, the globally bounded $`w=\rho^p y`$ gives an integrable uniform bound $`s_D(r)\leq C C_0r^{-p}`$. Dominated convergence proves convergence of slopes in $`L^1(0,R)`$ and hence uniform convergence of elevations, including <a href="#eq:crest1" data-reference-type="eqref" data-reference="eq:crest1">[eq:crest1]</a>. At $`p=1`$, <a href="#eq:outer" data-reference-type="eqref" data-reference="eq:outer">[eq:outer]</a> implies that $`y-\rho^{-1}`$ is integrable at infinity, giving <a href="#eq:crest2" data-reference-type="eqref" data-reference="eq:crest2">[eq:crest2]</a>. At $`p>1`$, $`y\sim\rho^{-p}`$ is integrable at infinity, while $`y\sim\rho/d`$ is integrable at zero. Equation <a href="#eq:crestexact" data-reference-type="eqref" data-reference="eq:crestexact">[eq:crestexact]</a> proves <a href="#eq:crest3" data-reference-type="eqref" data-reference="eq:crest3">[eq:crest3]</a>. ◻

</div>

<div class="corollary">

**Corollary 20** (The finite-crest viscosity limit). *For $`0<p<1`$, the continuous radial limit in Theorem <a href="#thm:crest" data-reference-type="ref" data-reference="thm:crest">19</a> is a viscosity solution of
``` math
K(r/d)^m|\nabla z|^n-U=0
```
on the entire ball, with zero boundary values. For $`p\geq1`$ the limiting profile is not a finite continuous viscosity solution on the closed ball because its summit diverges.*

</div>

<div class="proof">

*Proof.* Away from zero the equation is classical. At zero the limit has the form $`z(0)-Cr^{1-p}`$, $`C>0`$. No smooth function touches this cusp from below at zero, so the supersolution condition there is vacuous. Every upper test has Hamiltonian value $`-U\leq0`$, proving the subsolution condition. This statement concerns the scalar limiting stream-power equation, not the different three-field wet–dry system. ◻

</div>

## All weighted relief moments

For $`\beta>0`$ put $`V_\beta(D)=\int_0^R r^{\beta-1}z_D(r)\,\mathrm dr`$. Physical integrated elevation in $`d`$ dimensions is $`|\mathbb S^{d-1}|V_d`$.

<div id="thm:moments" class="theorem">

**Theorem 21** (Moment thresholds). *For every $`\beta>0`$,
``` math
\begin{equation}
 V_\beta(D)=\frac{U\ell^{\beta+2}}{\beta D}
       \int_0^{R/\ell}\rho^\beta y(\rho)\,\mathrm d\rho.\label{eq:momentexact}
\end{equation}
```
Consequently
``` math
\begin{align*}
 p<\beta+1:\quad&V_\beta(D)\to
       \frac{C_0R^{\beta+1-p}}{\beta(\beta+1-p)},\\
 p=\beta+1:\quad&V_\beta(D)=\frac{C_0}{\beta}
       \{\log(R/\ell)+\mathcal C_\beta+o(1)\},\\
 p>\beta+1:\quad&V_\beta(D)\sim
       \frac{U\ell^{\beta+2}}{\beta D}\mathcal J_\beta,
 \qquad\mathcal J_\beta=\int_0^\infty\rho^\beta y(\rho)\,\mathrm d\rho.
\end{align*}
```
The critical constant is the corresponding convergent logarithmic renormalization. The supercritical power of $`D`$ is $`\{n(\beta+1)-m\}/(m+n)`$. In particular, total landscape volume has its threshold at $`m/n=d+1`$, not at the summit threshold $`m/n=1`$.*

</div>

<div class="proof">

*Proof.* Tonelli’s theorem gives $`V_\beta=\beta^{-1}\int_0^R t^\beta s_D(t)\,\mathrm dt`$, proving <a href="#eq:momentexact" data-reference-type="eqref" data-reference="eq:momentexact">[eq:momentexact]</a>. The tail is $`\rho^{\beta-p}(1+O(\rho^{-p-1}))`$ by Lemma <a href="#lem:outer" data-reference-type="ref" data-reference="lem:outer">17</a>. Integrating this tail, or using dominated convergence when it is integrable, gives the three alternatives and their constants. Substitution of <a href="#eq:scales" data-reference-type="eqref" data-reference="eq:scales">[eq:scales]</a> gives the exponent of $`D`$. ◻

</div>

<div id="thm:momentcorrections" class="theorem">

**Theorem 22** (Rates for finite relief moments). *Let $`\beta>0`$, $`p<\beta+1`$, and put $`h=\beta+1-p>0`$, $`q=p+1`$, $`A_1=-(d-1-p)/n`$. Write
``` math
V_\beta^{(0)}=\frac{C_0R^h}{\beta h}.
```
If $`0<h<q`$ (equivalently $`\beta<2p`$), the constant
``` math
H_\beta=\int_0^\infty
       \{\rho^\beta y(\rho)-\rho^{\beta-p}\}\,d\rho
```
is absolutely convergent, and
``` math
V_\beta(D)=V_\beta^{(0)}+
 \frac{C_0}{\beta}\left\{
 H_\beta\ell^h+\frac{A_1R^{h-q}}{h-q}\ell^q
 +O(\ell^{2q})\right\}.
```
If $`h=q`$ (equivalently $`\beta=2p`$), the finite constant
``` math
H_\beta=\lim_{S\to\infty}\left\{
 \int_0^S\rho^\beta y(\rho)\,d\rho
 -\frac{S^q}{q}-A_1\log S\right\}
```
exists, and
``` math
V_\beta(D)=V_\beta^{(0)}+
 \frac{C_0}{\beta}\ell^q
       \{A_1\log(R/\ell)+H_\beta\}
 +O(\ell^{2q}).
```
If $`h>q`$ (equivalently $`\beta>2p`$), then
``` math
V_\beta(D)=V_\beta^{(0)}+
 \frac{C_0A_1R^{h-q}}{\beta(h-q)}\ell^q+o(\ell^q).
```
All statements concern fixed positive $`R,K,U,m,n`$ as $`D\downarrow0`$. They remain valid when displayed coefficients vanish; no nonzero leading correction is asserted in that case.*

</div>

<div class="proof">

*Proof.* The exact scaling formula is
``` math
V_\beta(D)=\frac{C_0}{\beta}\ell^h I_\beta(R/\ell),\qquad
 I_\beta(S)=\int_0^S\rho^\beta y(\rho)\,d\rho.
```
The outer expansion gives
``` math
I_\beta'(\rho)=\rho^{h-1}
     +A_1\rho^{h-q-1}+O(\rho^{h-2q-1}).
```
When $`h<q`$, the difference of the first two terms in the definition of $`H_\beta`$ is integrable at infinity; it is integrable at zero because $`h>0`$ and $`y(\rho)=O(\rho)`$. Integrating the tail from $`S`$ to infinity gives $`I_\beta(S)=S^h/h+H_\beta+
A_1S^{h-q}/(h-q)+O(S^{h-2q})`$. When $`h=q`$, subtraction of $`A_1/\rho`$ for large $`\rho`$ leaves an integrable remainder, yielding $`I_\beta(S)=S^q/q+A_1\log S+H_\beta+O(S^{-q})`$. When $`h>q`$, integration of the first correction gives $`I_\beta(S)=S^h/h+A_1S^{h-q}/(h-q)+o(S^{h-q})`$. Substitution of $`S=R/\ell`$ proves the assertions. ◻

</div>

Since $`\ell^{p+1}=d^{m/n}D/(K^{1/n}U^{(n-1)/n})`$, these corrections have respectively fractional-power, $`D\log(1/D)`$, and $`D`$ scales. The second threshold $`\beta=2p`$ distinguishes a correction controlled by the summit region from one controlled by the outer profile; it differs from the finiteness threshold $`p=\beta+1`$. Vanishing coefficients can suppress the displayed correction, so a universally sharp rate is not claimed.

## Exactly one maximum slope

<div id="prop:peak" class="proposition">

**Proposition 23** (The radial transition scale). *The universal slope $`y`$ increases to a single nondegenerate maximum at $`\rho_*\in(0,\infty)`$ and decreases thereafter. If $`R>\ell\rho_*`$, the physical maximum occurs at $`r_* =\ell\rho_*`$ and has size $`(U\ell/D)y(\rho_*)`$. Otherwise the maximum on the finite hillslope occurs at the boundary.*

</div>

<div class="proof">

*Proof.* For $`d=1`$ the nullcline is $`H(\rho)=\rho^{-p}`$, strictly decreasing. The solution starts below it and must cross it, since remaining below would make $`y`$ increasing while $`H\to0`$. At a crossing $`(y-H)'=-H'>0`$, so there can be only one. For $`d>1`$ the positive nullcline satisfies $`\rho^m H^n+(d-1)H/\rho=1`$. Writing $`h=H/\rho`$ shows that $`h`$ strictly decreases from $`1/(d-1)`$ to zero and that $`H'`$ has the sign of $`(d-1)(m+1)h-m`$. Thus $`H`$ has one strict maximum. Initially $`y\sim\rho/d<H\sim\rho/(d-1)`$. A first crossing cannot occur while $`H`$ is increasing, since $`(y-H)'=-H'<0`$ there. Nor can it occur at the strict maximum: at a tangency there $`(y-H)''=-H''>0`$, contradicting negativity immediately before contact. A crossing must eventually occur because $`H\to0`$. After that point $`H'<0`$, so a reverse crossing is impossible. At this crossing $`y''<0`$, proving nondegeneracy. ◻

</div>

# An integrable radial family and deterministic checks

If $`p=d-1`$ and $`d>1`$, the transformed equation <a href="#eq:wode" data-reference-type="eqref" data-reference="eq:wode">[eq:wode]</a> separates. With $`\tau=\rho^d/d`$,
``` math
\begin{equation}
 \frac{\mathrm dw}{\mathrm d\tau}=1-w^n,\quad w(0)=0,
 \qquad\int_0^{w(\rho)}\frac{\,\mathrm du}{1-u^n}=\frac{\rho^d}{d}.\label{eq:separable}
\end{equation}
```
Here $`0<w<1`$. For $`n=1`$, $`m=d-1`$, and for $`n=2`$, $`m=2(d-1)`$, respectively,
``` math
y(\rho)=\rho^{-(d-1)}(1-e^{-\rho^d/d}),\qquad
 y(\rho)=\rho^{-(d-1)}\tanh(\rho^d/d).
```
These follow by elementary integration of <a href="#eq:separable" data-reference-type="eqref" data-reference="eq:separable">[eq:separable]</a> and provide exact benchmarks throughout the domain, not only asymptotic slopes.

In the $`d=2,m=n=1`$ case,
``` math
\begin{equation}
 \int_0^S y(\rho)\,\mathrm d\rho
 =\tfrac12\{\gamma_E+\log(S^2/2)+E_1(S^2/2)\},\qquad
 \mathcal C=\frac{\gamma_E-\log2}{2}.\label{eq:exactlog}
\end{equation}
```
Here $`E_1(x)=\int_x^\infty e^{-t}\,\mathrm dt/t`$. Differentiation and the zero-limit at $`S=0`$ verify the identity. For $`d\geq3,m=d-1,n=1`$, integration by parts gives
``` math
\mathcal J=\frac{d^{2/d-1}\Gamma(2/d)}{d-2}.
```
More generally, for $`0\leq\beta<d-2`$,
``` math
\mathcal J_\beta=
 \frac{d^{(\beta+2)/d-1}\Gamma((\beta+2)/d)}{d-\beta-2};
```
at $`\beta=d-2`$ the logarithmic constant is $`(\gamma_E-\log d)/d`$. These formulas are derived by integrating the displayed exponential profile.

The accompanying script checks the ellipse identities <a href="#eq:ellipse" data-reference-type="eqref" data-reference="eq:ellipse">[eq:ellipse]</a>, verifies interior residuals for the companion wet–dry benchmarks, and integrates <a href="#eq:universal" data-reference-type="eqref" data-reference="eq:universal">[eq:universal]</a> for seven parameter triples. The original seven-case replay checks leading-order normalization and sampled slope bounds. The added `verify_extensions.py` instead integrates $`v=\rho^{p+1}(\rho^py-1)`$ using a cancellation-safe nonlinear remainder. The table reports $`v(120)`$ from the tighter of two tolerances. At $`\rho=30,60,120`$, it asserts $`|v-A_1|<4|A_2|\rho^{-(p+1)}+2\times10^{-6}`$ and tolerance-refinement differences below $`2\times10^{-7}`$. These are declared finite-sample test tolerances, not rigorous error bounds. The observed second correction is logged as diagnostic only.

<div class="center">

| $`d`$ | $`m`$ | $`n`$ | observed correction |  prediction | refinement difference |
|------:|------:|------:|--------------------:|------------:|----------------------:|
|     2 |   0.5 |     1 |         -0.50038109 | -0.50000000 |          0.0000000000 |
|     2 |     1 |     1 |          0.00000000 | -0.00000000 |          0.0000000000 |
|     2 |     2 |     1 |          1.00000231 |  1.00000000 |          0.0000000000 |
|     3 |   0.6 |   1.2 |         -1.25011903 | -1.25000000 |          0.0000000001 |
|     1 |     1 |     2 |          0.25016660 |  0.25000000 |          0.0000000000 |
|     2 |   0.4 |   0.6 |         -0.55595794 | -0.55555556 |          0.0000000000 |
|     3 |     3 |     1 |          1.00000002 |  1.00000000 |          0.0000000000 |

</div>

The $`n=1`$ solutions agree with an independent integrating-factor quadrature at the tested radii to maximum absolute error below $`1.3\times10^{-11}`$. The critical renormalized integral is checked at radius 30 against the exact constant with absolute tolerance $`10^{-8}`$, matching <a href="#eq:exactlog" data-reference-type="eqref" data-reference="eq:exactlog">[eq:exactlog]</a>. These are floating-point consistency checks, not interval certificates. The symbolic checks prove polynomial identities, not the compactness, regularity, or continuation theorems.

# Interpretation, obstructions, and remaining scope

A simple obstruction explains why existence cannot be asserted for every prescribed topography. Suppose a $`C^1`$ landscape has a nonempty compact sublevel basin inside $`\Omega`$, with positive rainfall and no allowed sink. Choose a nonnegative test function $`\varphi=\eta(c-z)`$ supported in that basin, with $`\eta'\geq0`$. If $`q=-a\nabla z/|\nabla z|`$, $`a\geq0`$, then
``` math
q\cdot\nabla\varphi=a\eta'(c-z)|\nabla z|\geq0,
 \qquad\int\rho\varphi=-\int q\cdot\nabla\varphi\leq0,
```
a contradiction. One may justify the $`C^1`$ test by approximation. Ponding, filling or a sink changes the model; it is not a solution of the unmodified conservation equation. This conservation argument is consistent with the established critical-point discussion in and is not claimed as a new physical observation. The small-erosion states avoid the obstruction because $`-\Delta z>0`$.

The results close several precise subproblems: weak-erosion steady existence on general smooth domains with positive variable forcing; all-parameter regular radial steady existence; global radial relaxation for $`n\geq1`$; and a complete radial small-diffusion classification, including weighted observables and the slope transition. The constructive theorem additionally gives local nonradial uniqueness and parameter stability under constant forcing, $`m+n\geq1`$, and its stated geometric margin. No nonradial existence for arbitrary erosion intensity, unrestricted general-domain uniqueness, nonradial dynamical well-posedness, stability to channel-forming perturbations, or evolution for $`0<n<1`$ in the same classical class is proved. The separate three-field wet–dry problem and the Díaz et al. conjecture are addressed by exact benchmarks, a corrected profile problem and conditional compatibility obstructions in the companion document. The whole supplied Problem 5 must therefore remain marked *partially resolved*, not solved.

#### Reproducibility and disclosure.

All model-specific arguments are displayed. Standard Dirichlet elliptic regularity, the compact-convex fixed-point theorem, elementary ODE theory, heat-semigroup local theory, and maximum principles are the external mathematical tools. Source code, software versions, raw numerical outputs, a claim ledger and a hash manifest accompany this manuscript. No real-world landscape data have been fitted. Mathematical existence is not validation of the model’s sediment-coupling assumptions; see the distinct physical-model analysis in . The general-domain theorem uses zero elevation on the whole boundary, not arbitrary mixed, single-outlet or periodic conditions. The supplied referee audit and the present additional reviews are AI-assisted assessments, not human peer-review acceptance or formal proof certificates.

#### Research declarations.

Scholarly attribution is Anonymous under the Evidence Press release protocol. Evidence Press is the publisher; account ownership and publication authorization are not attributed as mathematical contributions. Codex supplied AI-assisted analysis, drafting, code, revision and internal checking. Supplied AI-assisted audit material informed the revisions; no human specialist acceptance or formal proof verification is claimed. No human research contribution was established in the available provenance. Funding information and personal competing-interest declarations were not supplied; no grant, affiliation or absence of personal conflicts is inferred. The publisher’s role is preparation and dissemination of the candidate. There were no human participants, animal subjects or personal research data. The archive provides editable sources, synthetic benchmark data and replay code: original research prose and data are CC0-1.0, and original code is MIT, with cited works retaining their own rights.

<div class="thebibliography">

99 Anand, S. K., Bertagni, M. B., Drivas, T. D., & Porporato, A. (2023). Self-similarity and vanishing diffusion in fluvial landscapes. *Proceedings of the National Academy of Sciences, 120*(51), e2302401120. <https://doi.org/10.1073/pnas.2302401120>. Author text: <https://arxiv.org/abs/2401.04113>. Binard, J., Degond, P., & Noble, P. (2024). Well-posedness and stability analysis of a landscape evolution model. *Journal of Nonlinear Science, 34*, 20. <https://doi.org/10.1007/s00332-023-09997-9>. Author text: <https://arxiv.org/abs/2211.09629>. Birnir, B., & Landry, T. B. (2025). Existence theorems for PDEs modeling erosion and the optimal transportation of sediment. *Analysis and Mathematical Physics, 15*, 107. <https://doi.org/10.1007/s13324-025-01100-7>. Bonetti, S., Bragg, A. D., & Porporato, A. (2018). On the theory of drainage area for regular and non-regular points. *Proceedings of the Royal Society A, 474*, 20170693. <https://doi.org/10.1098/rspa.2017.0693>. Bonetti, S., Hooshyar, M., Camporeale, C., & Porporato, A. (2020). Channelization cascade in landscape evolution. *Proceedings of the National Academy of Sciences, 117*, 1375–1382. <https://doi.org/10.1073/pnas.1911817117>. Author text: <https://arxiv.org/abs/1812.03696>. Briane, M. (2014). Isotropic realizability of electric fields around critical points. *Discrete and Continuous Dynamical Systems–B, 19*(2), 353–372. <https://doi.org/10.3934/dcdsb.2014.19.353>. Author text: <https://arxiv.org/abs/1306.0236>. Briane, M. (2018). Reconstruction of isotropic conductivities from non smooth electric fields. *ESAIM: Mathematical Modelling and Numerical Analysis, 52*(3), 1173–1193. <https://doi.org/10.1051/m2an/2018013>. Richter, G. R. (1981). An inverse problem for the steady state diffusion equation. *SIAM Journal on Applied Mathematics, 41*(2), 210–221. <https://doi.org/10.1137/0141016>. Full text inspected, especially pp. 213–219. Gilbarg, D., & Trudinger, N. S. (2001). *Elliptic partial differential equations of second order*. Springer. <https://doi.org/10.1007/978-3-642-61798-0>. Henry, D. (1981). *Geometric theory of semilinear parabolic equations*. Lecture Notes in Mathematics, 840. Springer. <https://doi.org/10.1007/BFb0089647>. Hooshyar, M., Anand, S. K., & Porporato, A. (2020). Variational analysis of landscape elevation and drainage networks. *Proceedings of the Royal Society A, 476*, 20190775. <https://doi.org/10.1098/rspa.2019.0775>. Author text: <https://arxiv.org/abs/1911.03519>. Litwin, D. G., Malatesta, L. C., & Sklar, L. S. (2025). Hillslope diffusion and channel steepness in landscape evolution models. *Earth Surface Dynamics, 13*, 277–293. <https://doi.org/10.5194/esurf-13-277-2025>.

</div>
