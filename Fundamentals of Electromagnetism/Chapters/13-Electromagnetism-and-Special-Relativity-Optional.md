# Chapter 13 — Electromagnetism and Special Relativity (Extended Content)

Electric and magnetic fields are not wholly separate phenomena. An observer who sees a stationary charge may describe only an electric field; an observer moving relative to that charge can also measure a magnetic field. The laws must fit together because all inertial observers agree on the speed of light.

## 13.1 Why relativity belongs here

Maxwell's vacuum equations predict one speed $c$, not a speed obtained by adding the wave speed to that of its source. Special relativity preserves $c$ in every inertial frame. The apparent division into electric and magnetic effects therefore depends on the observer, even though the underlying electromagnetic field is one physical object.

A useful qualitative example is a current-carrying wire: mobile electrons and the positive lattice have different velocities. Changing reference frames changes their measured charge densities because simultaneity and lengths transform. What appears mainly as a magnetic interaction in one frame can acquire an electric component in another. This is an illustration, not a license to derive the entire magnetic force from naïve length contraction alone.

## 13.2 Lorentz transformations and four-vectors

For two inertial frames with relative speed $v$ (metres per second) in the $x$ direction, set $\beta=v/c$ and $\gamma=(1-\beta^2)^{-1/2}$. Both $\beta$ and $\gamma$ are dimensionless; $c$ is light speed ($\mathrm{m/s}$). With $S'$ moving at $+v$ relative to $S$,

$$
\boxed{ct'=\gamma(ct-\beta x)},\qquad\boxed{x'=\gamma(x-vt)},\quad y'=y,\ z'=z.
$$

Space and time coordinates mix, but the interval $c^2t^2-x^2-y^2-z^2$ is unchanged. A four-vector collects quantities that transform in the same way as $(ct,x,y,z)$; the four-current is

$$
\boxed{J^\mu=(c\rho,\mathbf J)}.
$$

Here $J^\mu$ is the four-current, with all components in $\mathrm{A/m^2}$; $\rho$ is charge density ($\mathrm{C/m^3}$), and $\mathbf J$ is current density ($\mathrm{A/m^2}$). Its continuity equation becomes the compact statement $\partial_\mu J^\mu=0$, which is the same local charge conservation derived in Chapter 6. The notation is useful because it makes relativistic consistency visible without changing the physics.

## 13.3 How electric and magnetic fields transform

Decompose the fields into components parallel and perpendicular to the frame velocity $\mathbf v$. For the standard convention where $S'$ moves with velocity $\mathbf v$ relative to $S$,

$$
\boxed{\begin{aligned}
\mathbf E'_\parallel&=\mathbf E_\parallel,&\mathbf B'_\parallel&=\mathbf B_\parallel,\\
\mathbf E'_\perp&=\gamma(\mathbf E_\perp+\mathbf v\times\mathbf B),&
\mathbf B'_\perp&=\gamma\left(\mathbf B_\perp-\frac{\mathbf v\times\mathbf E}{c^2}\right).
\end{aligned}}
$$

These formulas use the boost convention of the previous section; reversing the boost changes the signs of $\mathbf v$. For example, a pure electric field in one frame can produce a magnetic field in another when the boost is transverse to $\mathbf E$. The invariants $E^2-c^2B^2$ and $\mathbf E\cdot\mathbf B$ stay unchanged under Lorentz transformations.

## 13.4 Electric and magnetic potentials are related too

We already wrote $\mathbf E=-\nabla\phi-\partial_t\mathbf A$ and $\mathbf B=\nabla\times\mathbf A$. Special relativity packages $\phi$ and $\mathbf A$ into a four-potential,

$$
\boxed{A^\mu=\left(\frac\phi c,\mathbf A\right)}.
$$

With metric signature $(+,-,-,-)$, the gauge change $A^\mu\mapsto A^\mu-\partial^\mu\chi$ does not change the electromagnetic field (the arbitrary gauge function $\chi$ has units of webers). A rank-two antisymmetric **field tensor** collects the six independent components of $\mathbf E$ and $\mathbf B$, making their mixing under boosts systematic. The complete tensor formula and covariant Maxwell equations belong to a fuller classical electrodynamics course; they are not prerequisites for Chapters 1–12.

## 13.5 The next step

A convenient gauge (the Lorenz gauge) turns the potential equations into sourced wave equations. Their solutions must depend on the state of distant sources at *earlier* times because electromagnetic effects propagate at finite speed. This leads to retarded potentials, radiation from accelerating charges and covariant field theory. The foundation developed here is enough to see **why** those topics arise, without treating them as part of introductory electromagnetism.


