**Archive DOI:** <https://doi.org/10.5281/zenodo.23178664>. Version 1.3.0-candidate.

**Status.** Prospective research and source-audit note; AI-assisted reviews supplied; no human referee acceptance or proof-assistant certification. Corrections below concern equations as printed in the inspected author PDF, not an allegation about intent or a refutation of every conclusion of that paper.

# The three-field equations and vacuum

Write $`h\geq0`$ for water depth, $`z`$ for bed elevation, $`c\geq0`$ for suspended sediment concentration, and $`r\geq0`$ for rainfall. The normalized model of Binard, Degond and Noble is
``` math
\begin{align}
 h_t+\operatorname{div}(hv)&=r, &v&=-\nabla(h+z),\label{eq:water}\\
 z_t&=\kappa\Delta z+sc-eh^m|v|^n,\label{eq:bed}\\
 (hc)_t+\operatorname{div}(hcv)&=eh^m|v|^n-sc.\label{eq:sediment}
\end{align}
```
Here $`\kappa,e,s>0`$ and $`m,n>0`$. Where $`h>0`$, the last equation becomes
``` math
c_t+v\cdot\nabla c=e h^{m-1}|v|^n-\frac{s+r}{h}c.
```
The division by $`h`$ explains why a theorem formulated in positive-depth Sobolev spaces does not automatically cover vacuum. The local theorem in assumes a positive water-depth lower bound and additional regularity and parameter conditions. We do not remove those hypotheses for arbitrary initial data.

We use the conservative equations <a href="#eq:water" data-reference-type="eqref" data-reference="eq:water">[eq:water]</a>–<a href="#eq:sediment" data-reference-type="eqref" data-reference="eq:sediment">[eq:sediment]</a> directly, with $`c=0`$ in dry regions. This convention is forced in any open dry spacetime region on which $`r=0`$ and the equations hold as regular functions: $`hc=hcv=eh^m|v|^n=0`$, so <a href="#eq:sediment" data-reference-type="eqref" data-reference="eq:sediment">[eq:sediment]</a> gives $`sc=0`$. It is not legitimate to prescribe an arbitrary nonzero concentration on such a region and still claim a solution of the displayed system. Initial-time traces require their own compatibility conditions; the observation is not a general trace theorem.

# A global traveling wet–dry front

<div id="thm:front" class="theorem">

**Theorem 1** (Planar front for the full conservative system). *Fix $`b\in\mathbb R^d`$, a unit vector $`\nu`$, $`\alpha>0`$, and $`z_0\in\mathbb R`$. Set
``` math
v_w=-(b+\alpha\nu),\qquad V=v_w\cdot\nu=-b\cdot\nu-\alpha,
 \qquad \xi=\nu\cdot x-Vt.
```
For zero rainfall, the fields
``` math
\begin{equation}
 h=\alpha\xi_+,\qquad z=b\cdot x+z_0,\qquad
 c=\frac es|v_w|^n h^m\label{eq:front}
\end{equation}
```
solve <a href="#eq:water" data-reference-type="eqref" data-reference="eq:water">[eq:water]</a>–<a href="#eq:sediment" data-reference-type="eqref" data-reference="eq:sediment">[eq:sediment]</a> globally in space and time in distributions, with $`v=v_w`$ on the wet side and $`v=-b`$ on the dry side. The water depth is also a viscosity solution of the scalar water equation with the displayed affine bed. No singular mass source is placed at the interface.*

</div>

<div class="proof">

*Proof.* In the wet region $`h_t+v_w\cdot\nabla h=-\alpha V+\alpha v_w\cdot\nu=0`$. The bed is time-independent and harmonic, while $`sc=eh^m|v_w|^n`$, so the bed equation holds. Moreover $`hc=(e/s)|v_w|^n h^{m+1}`$ travels at the same normal speed $`V`$; its transport derivative is zero, as is the sediment source. All equations hold in the dry region as well. At the interface, $`h,hv,hc,hcv`$ have zero traces from both sides. Thus their distributional derivatives create no surface Dirac term. The affine bed has no singular Laplacian.

For the viscosity assertion write the scalar equation as
``` math
F(h,h_t,\nabla h,\Delta h):=h_t-h\Delta h-|\nabla h|^2-b\cdot\nabla h=0.
```
At a wet or dry interior point the equation is classical. At the moving corner there is no smooth upper test, because the spatial profile is a convex wedge. A smooth lower test has first-order spacetime jet
``` math
p=\theta\alpha\nu,\qquad a=-\theta\alpha V,
 \qquad 0\leq\theta\leq1.
```
This follows by testing tangential spacetime directions and the two normal one-sided slopes. Since $`h=0`$ at the corner, the second-order term vanishes and
``` math
F(0,a,p,\Delta\phi)
 =-\theta\alpha V-\theta^2\alpha^2-\theta\alpha b\cdot\nu
 =\alpha^2\theta(1-\theta)\geq0.
```
This is the supersolution inequality; the subsolution condition is vacuous there. Hence the viscosity conditions hold everywhere. ◻

</div>

<div class="proposition">

**Proposition 2** (Classification within the planar traveling ansatz). *Suppose the bed is the fixed affine function $`b\cdot x+z_0`$, rainfall is zero, and the wet side $`\nu\cdot x-Vt>0`$ (after orienting $`\nu`$ toward the wet region) of a profile, classical inside the wet region, has $`h=H(\nu\cdot x-Vt)>0`$, continuous zero depth at its edge, and zero limiting water flux there. Then the depth is the wedge in <a href="#eq:front" data-reference-type="eqref" data-reference="eq:front">[eq:front]</a>, and the bed equation forces its concentration to be the one in <a href="#eq:front" data-reference-type="eqref" data-reference="eq:front">[eq:front]</a>.*

</div>

<div class="proof">

*Proof.* The water equation has first integral
``` math
H(-b\cdot\nu-H'-V)=\text{constant}.
```
The zero-flux edge condition makes the constant zero. On the wet side, $`H'=-b\cdot\nu-V=\alpha`$ is constant. A positive one-sided profile emerging from zero has $`\alpha>0`$. The bed equation then gives $`sc=eH^m|b+\alpha\nu|^n`$, and the sediment equation has already been checked. ◻

</div>

<div class="remark">

*Remark 3* (Exact family, not a general well-posedness theorem). The depth in <a href="#eq:front" data-reference-type="eqref" data-reference="eq:front">[eq:front]</a> is unbounded on a half-space and the bed is affine. These solutions are locally integrable distributional solutions, not finite-mass perturbations in the global Sobolev class used in . The viscosity assertion is for the scalar water component, not an unspecified vector-valued viscosity theory for all three fields. The construction neither proves uniqueness for general wet–dry data nor controls perturbations of the front.

</div>

# Global wet-up from complete vacuum

<div id="thm:wetup" class="theorem">

**Theorem 4** (Spatially homogeneous rainfall over an affine bed). *Let $`r:[0,\infty)\to[0,\infty)`$ be continuous. Put $`H(t)=\int_0^t r(\tau)\,\mathrm d\tau`$ and fix $`b\in\mathbb R^d`$. Define
``` math
\begin{equation}
 W(t)=e|b|^n\int_{\{0<\tau<t:H(\tau)>0\}}
 H(\tau)^m\exp\!\left[-s\int_\tau^t\frac{\,\mathrm d\eta}{H(\eta)}\right]\,\mathrm d\tau,\label{eq:wetupW}
\end{equation}
```
with $`W(t)=0`$ if $`H(t)=0`$. Then
``` math
\begin{equation}
 h(x,t)=H(t),\quad
 c(x,t)=\begin{cases}W(t)/H(t),&H(t)>0,\\0,&H(t)=0,\end{cases}
 \quad z(x,t)=b\cdot x+z_0-W(t)\label{eq:wetup}
\end{equation}
```
is a global conservative solution of the full system, starting with $`h=c=0`$. The concentration is continuous through the initial dry interval and
``` math
\begin{equation}
 0\leq c(t)\leq\frac es|b|^n H(t)^m.\label{eq:wetupbound}
\end{equation}
```
These are the unique continuous solutions within this homogeneous-water and homogeneous-concentration ansatz with an affine bed with the stated initial traces.*

</div>

<div class="proof">

*Proof.* Since $`H`$ is nondecreasing, once it is positive it remains positive. On that interval the integral <a href="#eq:wetupW" data-reference-type="eqref" data-reference="eq:wetupW">[eq:wetupW]</a> solves the linear equation
``` math
\begin{equation}
 W'=e|b|^n H^m-sW/H.\label{eq:Wode}
\end{equation}
```
The function $`\overline W=(e/s)|b|^nH^{m+1}`$ is a supersolution, because its derivative is nonnegative and the right side of <a href="#eq:Wode" data-reference-type="eqref" data-reference="eq:Wode">[eq:Wode]</a> is zero at $`W=\overline W`$. Comparison, first away from the initial dry endpoint and then by a limit, gives $`0\leq W\leq\overline W`$. This proves <a href="#eq:wetupbound" data-reference-type="eqref" data-reference="eq:wetupbound">[eq:wetupbound]</a> and continuity of $`c`$ at vacuum. It also shows that the right side of <a href="#eq:Wode" data-reference-type="eqref" data-reference="eq:Wode">[eq:Wode]</a> tends to zero at that endpoint. Thus $`W`$ extends as a $`C^1`$ function by zero across the initial dry interval.

Here $`v=-b`$, $`\Delta z=0`$, and all divergences of the spatially constant water and sediment fluxes vanish. The water equation is $`H'=r`$. The sediment equation is exactly <a href="#eq:Wode" data-reference-type="eqref" data-reference="eq:Wode">[eq:Wode]</a>; the bed equation is its negative because $`z_t=-W'`$. This verifies the full system, including vacuum. For uniqueness, the difference of two continuous solutions for $`W`$ satisfies $`Y'=-sY/H`$ on the wet interval. Its magnitude at any later time is no larger than its magnitude at an earlier time. Letting that earlier time tend to the common zero initial trace proves $`Y=0`$. The water equation and bed-plus-sediment conservation fix $`H`$ and $`z`$ within the ansatz. ◻

</div>

For constant rainfall $`r_0>0`$, the formula becomes elementary. Set
``` math
A=\frac{e r_0^m|b|^n}{s+(m+1)r_0}.
```
Then
``` math
\begin{equation}
 h=r_0t,\qquad c=At^m,\qquad
 z=b\cdot x+z_0-r_0A t^{m+1}.\label{eq:constantwetup}
\end{equation}
```
All three residuals vanish exactly. For $`m<1`$ the concentration need not be differentiable at $`t=0`$, but the conservative variable $`hc=r_0A t^{m+1}`$ is $`C^1`$ there. These formulas provide tests of vacuum handling and source-term balance for numerical solvers. They do not resolve spatially varying wet-up or coupled free-boundary stability.

# The channel problem and its printed formulations

Díaz, Fowler, Muñoz and Schiavi study, on the positive half-line, a nonnegative depth $`u`$, its power $`v=u^m`$, $`m>1`$, and a free boundary $`f(t)`$. Here $`m`$ is the porous-medium exponent of this reduced channel equation; it is not identified with the main manuscript’s contributing-area exponent. The physical reduction uses $`m=3/2`$. With $`C=M/2>0`$, their strong-local formulation includes
``` math
\begin{equation}
 u_t=v_{xx}+v\quad(0<x<f(t)),\qquad
 v_x(0,t)=0,\quad u(f(t),t)=0,\quad
 \int_0^{f(t)}v(x,t)\,\mathrm dx=C.\label{eq:SL}
\end{equation}
```
The equation is imposed inside the positive set. Their global formulation (P), printed on page 1674, uses instead
``` math
\begin{equation}
 u_t=v_{xx}+v-C\delta_{f(t)},\label{eq:P}
\end{equation}
```
together with the zero-total-measure condition for $`\mu=u_t-v_{xx}`$, intended to impose $`\int v=C`$. The same page conjectures solvability for suitable strictly positive initial data decaying at infinity. The stationary compact profile $`v=C\cos x`$ on $`[0,\pi/2]`$, zero beyond, is already proved in that paper and is not a new result here.

The inspected author PDF has 20 pages; printed pages 1673, 1674 and 1677 correspond to PDF pages 11, 12 and 15. These pages were checked as rendered images, rather than relying on extracted mathematical text. The following audit refers to those displayed equations.

## A contradictory profile normalization

<div id="prop:contradiction" class="proposition">

**Proposition 5** (The two printed requirements are incompatible). *For $`m>1`$ and $`c_*>0`$, no nonnegative compactly supported profile with zero derivative at the origin can satisfy both
``` math
\begin{equation}
 w''+w-\frac1{m-1}w^{1/m}=c_*\delta_L,
 \qquad\int_0^\infty w(x)\,\mathrm dx=c_* .\label{eq:printed}
\end{equation}
```
Here the second derivative is distributional, including the edge contribution, and the origin has the stated no-flux trace.*

</div>

<div class="proof">

*Proof.* Pair the distributional equation with a cutoff equal to one on the support, using the no-flux trace at zero. The total integral of $`w''`$ is zero. Hence
``` math
\int_0^\infty w\,\mathrm dx-\frac1{m-1}\int_0^\infty w^{1/m}\,\mathrm dx=c_*.
```
The asserted normalization forces the second integral to vanish, so $`w=0`$ almost everywhere, contradicting $`c_*>0`$. ◻

</div>

The unnumbered proposition on printed page 1673 includes exactly the pair of requirements in <a href="#eq:printed" data-reference-type="eqref" data-reference="eq:printed">[eq:printed]</a>. The contradiction is algebraic; it does not depend on a numerical experiment or on the unsolved positive-data conjecture.

## A complete repair of the profile boundary-value problem

The ODE itself is consistent when its integral is not incorrectly prescribed. It has the following constructive solution.

<div id="thm:repair" class="theorem">

**Theorem 6** (Correct positive profile and sharp width bounds). *For every $`m>1`$ and $`c_*>0`$, there is a unique pair $`(w,L)`$ in the class
``` math
w>0\text{ on }[0,L),\quad w'(0)=0,\quad w(L)=0,\quad
 w=0\text{ on }[L,\infty),
```
with $`w`$ classical inside its support and continuous at the edge, satisfying the distributional ODE in <a href="#eq:printed" data-reference-type="eqref" data-reference="eq:printed">[eq:printed]</a>. Its amplitude $`A=w(0)`$ is the unique root above $`A_0`$ of
``` math
\begin{equation}
 \frac{A^2}{2}-\frac{m}{(m-1)(m+1)}A^{(m+1)/m}
 =\frac{c_*^2}{2},\qquad
 A_0=\left(\frac{2m}{m^2-1}\right)^{m/(m-1)}.\label{eq:amplitude}
\end{equation}
```
Writing
``` math
\mathcal V(u)=\frac{u^2}{2}-\frac{m}{(m-1)(m+1)}u^{(m+1)/m},
```
the profile and its width are determined by
``` math
\begin{equation}
 x=\int_{w(x)}^A\frac{\,\mathrm du}{\sqrt{c_*^2-2\mathcal V(u)}},
 \qquad L=\int_0^A\frac{\,\mathrm du}{\sqrt{c_*^2-2\mathcal V(u)}}.\label{eq:profilequad}
\end{equation}
```
The width strictly decreases with $`c_*`$ and obeys the sharp bounds
``` math
\begin{equation}
 \frac\pi2<L(c_*)<\frac{\pi m}{m-1},\qquad
 \lim_{c_*\to\infty}L(c_*)=\frac\pi2,\quad
 \lim_{c_*\downarrow0}L(c_*)=\frac{\pi m}{m-1}.\label{eq:width}
\end{equation}
```
Its correct integral identity is
``` math
\begin{equation}
 \int_0^L w\,\mathrm dx=c_*+\frac1{m-1}\int_0^L w^{1/m}\,\mathrm dx>c_* .\label{eq:correctmass}
\end{equation}
```*

</div>

<div class="proof">

*Proof.* The potential $`\mathcal V`$ is negative on $`(0,A_0)`$ and strictly increasing on $`[A_0,\infty)`$, from zero to infinity. Thus <a href="#eq:amplitude" data-reference-type="eqref" data-reference="eq:amplitude">[eq:amplitude]</a> has one root $`A>A_0`$. The interior ODE has conserved energy
``` math
\tfrac12(w')^2+\mathcal V(w)=c_*^2/2.
```
Starting at $`A`$ with zero derivative, the solution decreases since $`\mathcal V'(A)>0`$. For $`0<w<A`$, the denominator in <a href="#eq:profilequad" data-reference-type="eqref" data-reference="eq:profilequad">[eq:profilequad]</a> is positive. Its square-root zero at $`A`$ is integrable, and its value at zero is $`c_*>0`$. The solution reaches zero in finite time $`L`$, with $`w'(L-)=-c_*`$. Its zero extension has the singular second derivative $`c_*\delta_L`$. This constructs the desired solution. Conversely, that edge coefficient and energy conservation force <a href="#eq:amplitude" data-reference-type="eqref" data-reference="eq:amplitude">[eq:amplitude]</a> and the decreasing branch <a href="#eq:profilequad" data-reference-type="eqref" data-reference="eq:profilequad">[eq:profilequad]</a>, proving uniqueness in the stated positive-profile class. Integrating the equation proves <a href="#eq:correctmass" data-reference-type="eqref" data-reference="eq:correctmass">[eq:correctmass]</a>.

For the width, put $`r_*=(m+1)/m\in(1,2)`$ and
``` math
\eta=\frac{2m}{(m-1)(m+1)}A^{r_*-2}\in(0,1).
```
Rescaling $`u=At`$ in <a href="#eq:profilequad" data-reference-type="eqref" data-reference="eq:profilequad">[eq:profilequad]</a> yields
``` math
L=\int_0^1\frac{\,\mathrm dt}{\sqrt{1-t^2-\eta(1-t^{r_*})}}.
```
The integrand strictly increases with $`\eta`$, whereas $`\eta`$ strictly decreases with $`A`$ and hence with $`c_*`$. At $`\eta=0`$ the integral is $`\pi/2`$. As $`\eta\uparrow1`$, monotone convergence gives
``` math
\int_0^1\frac{\,\mathrm dt}{\sqrt{t^{r_*}-t^2}}
 =\frac{\pi}{2-r_*}=\frac{\pi m}{m-1};
```
the substitution $`t^{(2-r_*)/2}=\sin\theta`$ verifies the last identity. These limits prove all of <a href="#eq:width" data-reference-type="eqref" data-reference="eq:width">[eq:width]</a>. ◻

</div>

At $`c_*=0`$, the limiting positive half-profile has the elementary expression
``` math
w_0(x)=A_0\cos^{\,2m/(m-1)}\!\left(\frac{m-1}{2m}x\right),
 \qquad 0\leq x\leq\frac{\pi m}{m-1},
```
and is zero beyond. Substitution verifies it. Such separable-profile constructions belong to the classical phase-plane theory; the purpose here is to supply a complete, correct replacement for the inconsistent normalization, not to claim the underlying energy method is new.

## The separable Dirac coefficient is time dependent

<div class="proposition">

**Proposition 7** (Exact time-scaling audit). *Let $`w`$ be the corrected profile of Theorem <a href="#thm:repair" data-reference-type="ref" data-reference="thm:repair">6</a>, $`T>0`$, and set
``` math
u(x,t)=(T-t)^{-1/(m-1)}w(x)^{1/m},\qquad 0\leq t<T.
```
Then, distributionally,
``` math
\begin{equation}
 u_t=(u^m)_{xx}+u^m
 -c_*(T-t)^{-m/(m-1)}\delta_L.\label{eq:correctblowup}
\end{equation}
```
Thus this ansatz does not solve an equation with a fixed nonzero Dirac coefficient $`C`$ on a time interval. Choosing $`c_*=CT^{m/(m-1)}`$ matches that coefficient only at $`t=0`$.*

</div>

<div class="proof">

*Proof.* Both the time derivative of $`(T-t)^{-1/(m-1)}`$ and its $`m`$th power contain the factor $`(T-t)^{-m/(m-1)}`$. Multiplying the profile equation by this factor gives <a href="#eq:correctblowup" data-reference-type="eqref" data-reference="eq:correctblowup">[eq:correctblowup]</a>. Its edge coefficient changes strictly in time for $`c_*>0`$. ◻

</div>

This is the second inconsistency in the separable claim on printed page 1673. The repaired profile really does give a blow-up solution, but of the time-dependent-sink equation <a href="#eq:correctblowup" data-reference-type="eqref" data-reference="eq:correctblowup">[eq:correctblowup]</a>, without the fixed-$`\int u^m`$ constraint.

# The moving-boundary identity and the normalization gap

<div id="prop:flux" class="proposition">

**Proposition 8** (Flux and two different integral quantities). *Assume $`f\in C^1`$, $`u`$ is continuous with $`u(f(t),t)=0`$, and $`v=u^m`$ is piecewise $`C^2`$ in space with a finite interior derivative trace at the edge. Assume also that the interior equation <a href="#eq:SL" data-reference-type="eqref" data-reference="eq:SL">[eq:SL]</a> holds, that the zero extension has locally integrable time derivative, and that the differentiations of the following integrals are justified. Put
``` math
q(t)=-v_x(f(t)-,t),\qquad
 N(t)=\int_0^{f(t)}u(x,t)\,\mathrm dx,\qquad
 C(t)=\int_0^{f(t)}u(x,t)^m\,\mathrm dx.
```
Then the correct zero-extension equation and integral identity are
``` math
\begin{equation}
 u_t=v_{xx}+v-q(t)\delta_{f(t)},\qquad N'(t)=C(t)-q(t).\label{eq:fluxidentity}
\end{equation}
```
In particular, imposing the local constraint $`C(t)=C`$ gives $`q(t)=C-N'(t)`$. In this regular class, replacing the edge coefficient by $`C`$ imposes the additional condition $`N'(t)=0`$.*

</div>

<div class="proof">

*Proof.* The continuous zero trace of $`v`$ removes a Dirac term from its first derivative. The jump in $`v_x`$ from $`-q`$ to zero gives $`+q\delta_{f(t)}`$ in its second derivative. The zero trace of $`u`$ removes the moving-edge Dirac term from $`u_t`$. These distributional identities prove the first equation. Integrating the interior equation and using the no-flux condition at zero gives $`N'=v_x(f-)+\int v=C(t)-q`$. The remaining conclusions follow algebraically. ◻

</div>

The distinction is between $`\int u`$ and $`\int u^m`$. They are not interchangeable. The source paper itself prints a flux identity involving $`\int u_t`$ on page 1674, but its simultaneous fixed-Dirac formulation requires the additional cancellation exhibited above in the regular class. Proposition <a href="#prop:flux" data-reference-type="ref" data-reference="prop:flux">8</a> does not rule out less regular measure-valued time derivatives; their singular parts must instead be specified and checked explicitly.

The existence theorem on printed page 1677 is for a coefficient $`\lambda(t)=C^*(t)^{m-1}>0`$:
``` math
\begin{equation}
 u_t=(u^m)_{xx}+\lambda(t)u^m-C\delta_{f(t)},\qquad
 \lambda(t)\int_0^\infty u^m\,\mathrm dx=C.\label{eq:lambda}
\end{equation}
```
The paper states that a rescaling can put the equation into a normalized form. A naive time-dependent scaling does not do so without extra terms.

<div class="proposition">

**Proposition 9** (Terms generated by a smooth scaling). *Take positive $`C^1`$ functions $`A,B`$ and an increasing $`C^1`$ time change $`\tau(t)`$. In <a href="#eq:lambda" data-reference-type="eqref" data-reference="eq:lambda">[eq:lambda]</a> put $`u(x,t)=A(t)V(B(t)x,\tau(t))`$, and write $`y=B(t)x`$. Then
``` math
\begin{align}
 V_\tau={}&\frac{A^{m-1}B^2}{\tau'}(V^m)_{yy}
 +\frac{\lambda A^{m-1}}{\tau'}V^m
 -\frac{CB}{A\tau'}\delta_{Bf}\nonumber\\
 &-\frac{A'}{A\tau'}V-\frac{B'}{B\tau'}yV_y.\label{eq:scaling}
\end{align}
```
To normalize the diffusion and reaction coefficients to one and retain Dirac coefficient $`C`$, one must have
``` math
B^2=\lambda,\qquad \tau'=A^{m-1}B^2,\qquad A^mB=1.
```
For nonconstant $`\lambda`$, these generally leave nonzero amplitude and dilation terms on the second line of <a href="#eq:scaling" data-reference-type="eqref" data-reference="eq:scaling">[eq:scaling]</a>.*

</div>

<div class="proof">

*Proof.* Apply the chain rule, use $`\delta(x-f)=B\delta(y-Bf)`$, and divide by $`A\tau'`$. The three coefficient identities follow by equating the desired coefficients. Since $`B=\sqrt\lambda`$ and $`A=B^{-1/m}`$, nonconstant $`\lambda`$ generally has $`B'\ne0`$ and $`A'\ne0`$. Cancellation for a special profile, a different nonlinear transformation, or an independent proof that $`\lambda`$ is constant would require another argument; none follows from this scaling alone. ◻

</div>

This computation is already an obstruction for smooth nonconstant multipliers. The reported theorem only gives a bounded multiplier, for which differentiating a normalization requires still more justification. We do not infer from this calculation that every conceivable transformation is impossible.

#### Benchmark use.

The traveling wedge tests front speed and conservation across a moving zero-depth interface; testing only its wet interior misses the interface condition. Homogeneous wet-up tests source balance and the conservative variable $`hc`$ at vacuum, including nondifferentiable concentration when $`m<1`$. The repaired channel profile tests edge flux, amplitude selection and quadrature; it is not a benchmark for the fixed-coefficient constrained evolution unless the time-dependent sink in <a href="#eq:correctblowup" data-reference-type="eqref" data-reference="eq:correctblowup">[eq:correctblowup]</a> is used.

# A dynamical compatibility condition for the constraint

The local constraint imposes a condition beyond matching its initial value and the edge flux. This condition can be obtained without specifying a free-boundary velocity law.

#### A sufficient fixed-domain regularity class.

The positive-time identity below applies, for example, under the following conditions on every compact interval $`J\subset(0,T)`$. Let $`f\in C^1(J)`$ with $`\inf_J f>0`$, let $`\lambda\in C(J)`$, and pull back the positive interval by
``` math
V(y,t)=v(f(t)y,t),\qquad 0\leq y\leq1,\qquad a=(m-1)/m.
```
Assume
``` math
\begin{gathered}
 V\in C(J;C^1([0,1]))\cap W^{1,1}(J;L^1(0,1)),\\
 V(1,t)=0,\quad V_y(0,t)=0,\quad V(y,t)>0\ (0<y<1).
 \end{gathered}
```
The $`W^{1,1}`$ assumption means absolute continuity in time with values in $`L^1`$. Assume also that $`V`$ is $`C^2`$ in the spatial interior, that the interior equation holds there with the chain rule giving, almost everywhere,
``` math
\begin{equation}
 V_t=\frac{f'}f yV_y+
       mV^a\{f^{-2}V_{yy}+\lambda V\},
 \label{eq:fixedintervalchain}
\end{equation}
```
and that one nonnegative $`H_J\in L^1(0,1)`$ satisfies
``` math
\begin{equation}
 |V^aV_{yy}|+V^{-1/m}|V_y|^2\leq H_J(y)
 \quad(0<y<1,\ t\in J).
 \label{eq:weighteddomination}
\end{equation}
```
These are sufficient hypotheses, not an existence assertion or a proposed minimal weak-solution class. They allow a simple linear zero of $`v`$ at the edge: the weighted gradient term then has the integrable order $`(1-y)^{-1/m}`$. In particular they do not require $`u_x`$ to remain bounded.

<div id="thm:constraintderivative" class="theorem">

**Theorem 10** (Constraint derivative and selected multiplier). *Let $`m>1`$ and suppose that a nonnegative solution is positive on $`0<x<f(t)`$ and zero at $`x=f(t)`$. Put $`v=u^m`$ and assume
``` math
u_t=v_{xx}+\lambda(t)v,\qquad v_x(0,t)=0,
 \qquad v(f(t),t)=0.
```
Assume the sufficient fixed-domain conditions above on compact positive-time intervals. With weaker hypotheses giving absolute continuity, the integrated chain rule and the weighted integration by parts with zero boundary trace, the identity below is interpreted almost everywhere unless continuity of its right side is separately known. Set
``` math
M(t)=\int_0^{f(t)}v\,dx,\quad
 g=v^{(2m-1)/(2m)},\quad
 \chi_m=\frac{4m(m-1)}{(2m-1)^2}.
```
Under the stated sufficient fixed-domain conditions, $`M`$ is $`C^1`$ for $`0<t<T`$ and
``` math
\begin{equation}
 M'(t)=m\left\{\lambda(t)\int_0^{f(t)}g^2\,dx
                -\chi_m\int_0^{f(t)}g_x^2\,dx\right\}.
 \label{eq:constraintderivative}
\end{equation}
```
In particular, preserving $`M(t)=C>0`$ forces
``` math
\begin{equation}
 \lambda(t)=\chi_m
       \frac{\int_0^{f(t)}g_x^2\,dx}
            {\int_0^{f(t)}g^2\,dx}.
 \label{eq:selectedlambda}
\end{equation}
```
For the original coefficient $`\lambda=1`$, every such constrained state with $`g\in H^1(0,f(t))`$ obeys
``` math
\begin{equation}
 f(t)\geq\frac{\pi\sqrt{m(m-1)}}{2m-1}.
 \label{eq:necessarywidth}
\end{equation}
```
If its edge flux $`-v_x(f(t)-,t)`$ is strictly positive, the inequality is strict.*

</div>

<div class="proof">

*Proof.* Write $`a=(m-1)/m\in(0,1)`$. In the stated sufficient class, $`M=f\int_0^1V\,\mathrm dy`$ is locally absolutely continuous. Integrating <a href="#eq:fixedintervalchain" data-reference-type="eqref" data-reference="eq:fixedintervalchain">[eq:fixedintervalchain]</a> gives, almost everywhere,
``` math
M'=f'\int_0^1(V+yV_y)\,\mathrm dy
       +\frac m f\int_0^1V^aV_{yy}\,\mathrm dy
       +m\lambda f\int_0^1V^{a+1}\,\mathrm dy.
```
The first integral is $`[yV]_0^1=0`$, so no boundary-velocity term remains. Since $`V`$ is $`C^1`$ up to the edge and $`V(1,t)=0`$, the weighted edge trace $`V^aV_y`$ vanishes; at the origin it vanishes by $`V_y(0,t)=0`$. Integration by parts on truncated intervals, followed by <a href="#eq:weighteddomination" data-reference-type="eqref" data-reference="eq:weighteddomination">[eq:weighteddomination]</a>, is therefore valid. Returning to $`x`$ gives
``` math
M'=m\int_0^f v^a(v_{xx}+\lambda v)\,dx
   =-(m-1)\int_0^f v^{-1/m}v_x^2\,dx
      +m\lambda\int_0^f v^{2-1/m}\,dx.
```
Continuity of $`V,V_y,f,\lambda`$, positivity for $`0<y<1`$, and the dominating function $`H_J`$ show that this last expression is continuous in time. The almost-everywhere identity for the absolutely continuous mass consequently holds at every positive time and makes $`M`$ locally $`C^1`$. Writing $`\alpha=(2m-1)/(2m)`$ gives $`g_x^2=\alpha^2v^{-1/m}v_x^2`$ and $`g^2=v^{2-1/m}`$, proving <a href="#eq:constraintderivative" data-reference-type="eqref" data-reference="eq:constraintderivative">[eq:constraintderivative]</a> and <a href="#eq:selectedlambda" data-reference-type="eqref" data-reference="eq:selectedlambda">[eq:selectedlambda]</a>. The sharp one-sided Dirichlet Poincare inequality is
``` math
\int_0^f g_x^2\,dx\geq
       \left(\frac\pi{2f}\right)^2\int_0^f g^2\,dx,
 \qquad g(f)=0.
```
Combining it with the quotient $`1/\chi_m`$ forced by $`\lambda=1`$ proves <a href="#eq:necessarywidth" data-reference-type="eqref" data-reference="eq:necessarywidth">[eq:necessarywidth]</a>. Equality in Poincare requires $`g=A\cos(\pi x/(2f))`$. Then $`v=g^{1/\alpha}`$ has zero derivative at the edge, because $`1/\alpha>1`$. Thus a strictly positive edge flux excludes equality. ◻

</div>

#### An additional hypothesis at the initial time.

Positive-time regularity alone does not determine $`M'(0+)`$. A concrete sufficient extension is to impose the same fixed-domain conditions on $`[0,T_0]`$, with $`f(0)>0`$, $`V(\cdot,0)=v_0(f(0)\,\cdot)`$, $`V\in W^{1,1}(0,T_0;L^1)\cap C([0,T_0];C^1)`$, and a single $`H_0\in L^1(0,1)`$ satisfying <a href="#eq:weighteddomination" data-reference-type="eqref" data-reference="eq:weighteddomination">[eq:weighteddomination]</a> for $`0\leq t\leq T_0`$. The initial profile is $`C^2`$ in the spatial interior and has the same boundary traces; the interior evolution equation is required only for $`t>0`$. Dominated convergence now gives a right limit at zero for the right side of <a href="#eq:constraintderivative" data-reference-type="eqref" data-reference="eq:constraintderivative">[eq:constraintderivative]</a>. Absolute continuity yields $`M(t)-M(0)=\int_0^t M'(s)\,\mathrm ds`$, so division by $`t`$ gives
``` math
M'(0+)=m\int_0^{f(0)}v_0^a
                  \{v_0''+\lambda(0)v_0\}\,\mathrm dx.
```
Thus weighted spatial integrability of the initial profile is only one requirement; time continuity, absolute continuity and domination up to zero are separate hypotheses on an evolution. They are not inferred from the initial data alone.

<div class="remark">

*Remark 11* (The normalization does not select an arbitrary sink). Formula <a href="#eq:selectedlambda" data-reference-type="eqref" data-reference="eq:selectedlambda">[eq:selectedlambda]</a> selects the reaction coefficient needed to preserve $`\int u^m`$, conditional on a sufficiently regular solution. It is not an existence theorem for the resulting nonlocal problem. Changing only a boundary Dirac coefficient does not remove <a href="#eq:constraintderivative" data-reference-type="eqref" data-reference="eq:constraintderivative">[eq:constraintderivative]</a>: its contribution to this weighted calculation vanishes at $`u=0`$. Nor does <a href="#eq:selectedlambda" data-reference-type="eqref" data-reference="eq:selectedlambda">[eq:selectedlambda]</a> automatically imply the different relation $`\lambda\int u^m=C`$ used in the variable-multiplier formulation. The latter relation would additionally require $`\chi_m M\int g_x^2/\int g^2=C`$.

</div>

<div id="prop:initialobstruction" class="proposition">

**Proposition 12** (Initial mass and flux do not ensure compatibility). *Fix $`m>1`$, $`C>0`$, $`L=\pi/2`$, and define on $`[0,L]`$
``` math
\phi(x)=2\cos x+9\cos3x+5\cos5x
         =16\cos^3x(5\cos^2x-4),
 \qquad v_\varepsilon(x)=C\{\cos x+\varepsilon\phi(x)\}.
```
Extend $`v_\varepsilon`$ by zero beyond $`L`$ and set $`u_\varepsilon=v_\varepsilon^{1/m}`$. For all sufficiently small $`\varepsilon>0`$, these data are positive on $`[0,L)`$, have zero origin derivative and zero edge value, and satisfy both
``` math
\int_0^L v_\varepsilon\,dx=C,
 \qquad -v_\varepsilon'(L-)=C.
```
Nevertheless, they cannot be the initial data of an evolution with $`\lambda=1`$ and $`\int u^m=C`$ whose right derivative of the constraint at time zero is given by <a href="#eq:constraintderivative" data-reference-type="eqref" data-reference="eq:constraintderivative">[eq:constraintderivative]</a>; in particular, no such evolution satisfies the additional fixed-domain hypotheses at the initial time stated above.*

</div>

<div class="proof">

*Proof.* The factorization of $`\phi`$ shows positivity for $`|\varepsilon|<1/16`$. Direct integration gives $`\int_0^L\phi=2-3+1=0`$, and $`\phi'(0)=\phi'(L)=0`$. Thus the displayed mass and flux constraints hold. Put $`a=(m-1)/m`$ and $`I_a=\int_0^{\pi/2}\cos^{a+1}x\,dx>0`$. The derivative forced by the equation is
``` math
m\int_0^L v_\varepsilon^a
          (v_\varepsilon''+v_\varepsilon)\,dx
 =mC^{a+1}\varepsilon
       \frac{192a(1-a)}{(a+3)(a+5)}I_a+O(\varepsilon^2)>0
```
for sufficiently small positive $`\varepsilon`$. To verify the coefficient, use $`\phi''+\phi=-72\cos3x-120\cos5x`$ and
``` math
\int_0^{\pi/2}\cos^a x\cos3x\,dx
    =\frac{a-1}{a+3}I_a,\qquad
 \int_0^{\pi/2}\cos^a x\cos5x\,dx
    =\frac{(a-1)(a-3)}{(a+3)(a+5)}I_a.
```
These follow by expanding the multiple-angle cosines and integrating powers of cosine by parts. The expansion remainder is integrable uniformly in $`\varepsilon`$, since $`v_\varepsilon=C\cos x\{1+16\varepsilon\cos^2x(5\cos^2x-4)\}`$ and the bracket stays bounded away from zero. A constant constraint has zero right derivative, giving the contradiction. ◻

</div>

# What remains, and what the note establishes

For the full three-field system, the explicit fronts and arbitrary continuous homogeneous-rainfall wet-up family establish genuine global solutions with vacuum, including a viscosity check of the water front. General finite-energy wet–dry existence, uniqueness, continuous dependence, and global continuation under spatially varying data are not established. A useful next mathematical target is compactness for $`h`$ and the conservative variable $`hc`$ strong enough to identify both $`hc\,\nabla(h+z)`$ and the deposition ratio $`(hc)/h`$ near $`h=0`$; the exact families do not supply those estimates.

For the reduced channel equation, the corrected profile boundary-value problem is completely solved, including its unique amplitude, profile quadrature, integral identity and width range. The new compatibility obstruction concerns compactly supported initial data and an evolution with the stated right derivative at time zero. It does not exclude an initial layer or a weaker solution outside that class. The fixed-mass positive-data conjecture is not proved or disproved. In particular, the absence of a finite free boundary at $`t=0`$ for strictly positive data is not a counterexample: a boundary could in principle enter from infinity immediately. Conversely, a solution that remained strictly positive throughout the half-line could not satisfy the stated zero-total-measure condition with a positive integral and no edge sink. The admissible evolution must therefore make that boundary mechanism precise.

The most economical next step is to settle the exact intended weak formulation: either retain the local constraint and the derived coefficient $`q=C-N'`$, or retain the fixed coefficient and prove the extra conservation or singular cancellation it entails. Existence for the variable-multiplier equation must not be relabeled existence for the original fixed-coefficient equation without that step.

#### Checks and provenance.

The bundled code checks the three interior residuals of the constant-rainfall family and traveling front, the separable time factor, and independent quadratures for the corrected profile. The compatibility script additionally checks the perturbation identities exactly and its positive constraint derivative by sampled quadrature with an analytical Taylor-remainder bound. Distributional, viscosity, and general existence arguments remain analytical proofs, not computer-certified claims. The paper’s rendered pages were inspected directly; no third-party full text or font files are redistributed in the bundle.

#### Research declarations.

Scholarly attribution is Anonymous under the Evidence Press release protocol. Evidence Press is the publisher; account ownership and publication authorization are not attributed as mathematical contributions. Codex supplied AI-assisted analysis, drafting, code, revision and internal checking. Supplied AI-assisted audit material informed the revisions; no human specialist acceptance or formal proof verification is claimed. No human research contribution was established in the available provenance. Funding information and personal competing-interest declarations were not supplied; no grant, affiliation or absence of personal conflicts is inferred. The publisher’s role is preparation and dissemination of the candidate. There were no human participants, animal subjects or personal research data. The archive provides editable sources, synthetic benchmark data and replay code: original research prose and data are CC0-1.0, and original code is MIT, with cited works retaining their own rights.

<div class="thebibliography">

9 Binard, J., Degond, P., & Noble, P. (2024). Well-posedness and stability analysis of a landscape evolution model. *Journal of Nonlinear Science, 34*, 20. <https://doi.org/10.1007/s00332-023-09997-9>. Author manuscript: <https://arxiv.org/abs/2211.09629>. Díaz, J. I., Fowler, A. C., Muñoz, A. I., & Schiavi, E. (2008). Mathematical analysis of a model of river channel formation. *Pure and Applied Geophysics, 165*, 1663–1682. <https://doi.org/10.1007/s00024-004-0394-3>. Inspected author PDF: <https://people.maths.ox.ac.uk/~fowler/papers/2008.5.pdf>.

</div>
