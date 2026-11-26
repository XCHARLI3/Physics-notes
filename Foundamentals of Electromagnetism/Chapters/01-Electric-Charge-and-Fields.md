# Chapter 1 — Electric Charge and Electric Fields

Electrostatics starts from observed interactions between charged objects. Coulomb's law describes the force between two point charges; superposition extends it to many charges. We then separate the source of an interaction from the response to it by introducing the electric field. This makes it possible to describe discrete particles, continuous matter and dipoles within one framework.

## 1.1 Electric charge

A glass rod rubbed with silk and a plastic rod rubbed with fur behave differently: two similarly charged rods repel, while rods carrying opposite charge attract. These observations motivate two kinds of charge, named positive and negative. Friction usually transfers electrons rather than creating electric charge; a neutral object can also be attracted when its charges rearrange, so attraction alone does not identify its net charge.

Electric charge is measured in coulombs ($\mathrm C$). Protons carry $+e$, electrons $-e$, and neutrons zero *net* charge. Millikan's oil-drop measurements found electric charges in discrete steps, providing evidence for charge quantisation in ordinary isolated objects:

$$e=1.602176634\times10^{-19}\ \mathrm C,\qquad Q=Ne\quad(N\in\mathbb Z).$$

Quarks have fractional charges but are not observed as free isolated particles. Charge can move between bodies, yet the total charge of an isolated system remains constant. Later, when current has been introduced, this global statement will become a local continuity equation.

## 1.2 Coulomb's law

Coulomb's torsion-balance measurements established the force's inverse-square dependence on separation. For static point charges $q_1$ at $\mathbf r_1$ and $q_2$ at $\mathbf r_2$ in vacuum, define the displacement from the source to the receiving charge as $\mathbf R=\mathbf r_2-\mathbf r_1$. Positions and distances are measured in metres ($\mathrm m$), force in newtons ($\mathrm N$), and vacuum permittivity $\varepsilon_0$ in farads per metre ($\mathrm{F/m}$). Then

$$\boxed{\mathbf F_{2\leftarrow1}=\frac{q_1q_2}{4\pi\varepsilon_0}\frac{\mathbf R}{|\mathbf R|^3}}.$$

The vector in the numerator supplies one power of distance, so the force magnitude varies as $1/R^2$. Its sign is set by $q_1q_2$: equal signs repel, opposite signs attract. The inverse-square form resembles Newtonian gravitation, but gravity between positive masses is attractive whereas the electric interaction has two signs. Coulomb's law is a measured physical law, not a consequence of algebra; its static instantaneous form does not describe arbitrary time-dependent sources.

## 1.3 Superposition

What happens when more than two charges are present? Experiment supports a further principle: in classical electrostatics, each source's contribution can be calculated separately and the resulting **vectors** added. This is not implied by the two-charge Coulomb formula alone.

$$\boxed{\mathbf F_i=\sum_{j\ne i}\mathbf F_{i\leftarrow j}=\frac{q_i}{4\pi\varepsilon_0}\sum_{j\ne i}q_j\frac{\mathbf r_i-\mathbf r_j}{|\mathbf r_i-\mathbf r_j|^3}}.$$

This linear addition is the reason a complicated collection of sources can be built from simple ones. Symmetry may cause some vector components to cancel even when their individual magnitudes do not.

## 1.4 From force to electric field

The direct-force description always names both the source and the charge receiving the force. Instead, let the sources create a field at every position, and let any small test charge respond locally to that field. Electric field is force per unit charge, with units $\mathrm{N/C}=\mathrm{V/m}$. For an ideal test charge $q_0$ that does not disturb the original sources,

$$\boxed{\mathbf E(\mathbf r)=\lim_{q_0\to0}\frac{\mathbf F(\mathbf r)}{q_0}},\qquad\boxed{\mathbf F=q\mathbf E}.$$

A point source $q$ at $\mathbf r'$ therefore produces

$$\mathbf E(\mathbf r)=\frac{q}{4\pi\varepsilon_0}\frac{\mathbf r-\mathbf r'}{|\mathbf r-\mathbf r'|^3}.$$

The first formula describes the **production** of a field; $\mathbf F=q\mathbf E$ describes the **response** of another charge. No test charge needs to be physically present for the source field to be defined. This separation becomes essential when fields later propagate through space rather than responding instantaneously to changing sources.

By superposition,

$$\boxed{\mathbf E(\mathbf r)=\frac1{4\pi\varepsilon_0}\sum_iq_i\frac{\mathbf r-\mathbf r_i}{|\mathbf r-\mathbf r_i|^3}}.$$

## 1.5 Field lines and symmetry

A vector field assigns a direction and magnitude to each point; field lines provide a picture of its direction. Their tangent is parallel to $\mathbf E$, and the chosen density of lines represents relative field strength. The lines are not physical objects, and space between drawn lines still contains a field.

If $s$ measures arc length along a field line where $\mathbf E\neq0$,

$$\frac{d\mathbf r}{ds}=\frac{\mathbf E(\mathbf r)}{|\mathbf E(\mathbf r)|}.$$

Symmetry offers more than a picture. If a source is unchanged by a reflection or rotation, its field must transform accordingly. At an observation point fixed by that symmetry, components that reverse sign must vanish. We will use this repeatedly before attempting an integral.

## 1.6 From discrete charges to continuous distributions

A macroscopic body contains too many individual charges to sum conveniently. If we look on scales larger than the microscopic spacing, small groups of charges can be described by a smooth charge density. The line density $\lambda$, surface density $\sigma$, and volume density $\rho$ have units $\mathrm{C/m}$, $\mathrm{C/m^2}$ and $\mathrm{C/m^3}$, respectively. For a line, surface or volume,

$$dq=\lambda\,dl,\qquad dq=\sigma\,dS,\qquad dq=\rho\,dV.$$

Divide the source into small elements, treat each as a point charge, add their fields, and take the continuous limit:

$$\sum_i\Delta q_i\frac{\mathbf r-\mathbf r_i}{|\mathbf r-\mathbf r_i|^3}\longrightarrow\int\frac{\mathbf r-\mathbf r'}{|\mathbf r-\mathbf r'|^3}\,dq.$$

For a volume distribution this gives

$$\boxed{\mathbf E(\mathbf r)=\frac1{4\pi\varepsilon_0}\int_V\rho(\mathbf r')\frac{\mathbf r-\mathbf r'}{|\mathbf r-\mathbf r'|^3}\,d^3r'}.$$

Here $\mathbf r'$ is a **source position**, while $\mathbf r$ is the **observation position**. Replacing $\rho\,dV$ by $\lambda\,dl$ or $\sigma\,dS$ gives the corresponding line or surface integral. The approximation is continuous, not an assertion that microscopic charges cease to be discrete.

## 1.7 Fields of simple distributions

Consider a uniformly charged ring of radius $R$ (metres) and total charge $Q$ (coulombs) in the $xy$-plane. Let $z$ be the signed axial observation height (metres) and $\hat{\mathbf z}$ the upward unit vector. At this point, opposite elements cancel horizontally; each contributes only its $z$-component:

$$dE_z=\frac1{4\pi\varepsilon_0}\frac{z\,dq}{(R^2+z^2)^{3/2}},\qquad \int dq=Q.$$

Hence

$$\boxed{\mathbf E(z)=\frac{Qz}{4\pi\varepsilon_0(R^2+z^2)^{3/2}}\hat{\mathbf z}}.$$

At $z=0$ the field vanishes by symmetry. For $|z|\gg R$, the ring appears point-like and the field approaches the Coulomb field of $Q$.

A uniformly charged disk can be assembled from concentric rings. A ring of radius $s$ and thickness $ds$ carries $dq=2\pi\sigma s\,ds$. For $z>0$,

$$E_z=\frac{\sigma z}{2\varepsilon_0}\int_0^R\frac{s\,ds}{(s^2+z^2)^{3/2}}=\boxed{\frac{\sigma}{2\varepsilon_0}\left(1-\frac{z}{\sqrt{R^2+z^2}}\right)}.$$

The $R\to\infty$ limit gives the field of an infinite uniformly charged sheet: $\mathbf E=(\sigma/2\varepsilon_0)\operatorname{sgn}(z)\hat{\mathbf z}$. The two sides point away from a positively charged sheet.

For a finite uniformly charged rod extending from $-a$ to $a$ on the $x$-axis, where $a$ is half its length, consider the point $(0,z)$ with $z>0$. Horizontal components again cancel:

$$E_z=\frac{\lambda z}{4\pi\varepsilon_0}\int_{-a}^a\frac{dx}{(x^2+z^2)^{3/2}}=\boxed{\frac{\lambda a}{2\pi\varepsilon_0z\sqrt{a^2+z^2}}}.$$

Taking $a\to\infty$ recovers $E=\lambda/(2\pi\varepsilon_0 z)$ for the infinite line. The important method is always the same: locate an element $dq$, use symmetry to discard cancelling components, integrate what remains, and test a simple limit. Chapter 2 will obtain several of these results much faster using Gauss's law.

## 1.8 Electric dipoles

Two equal and opposite charges, each of magnitude $q>0$, separated by a vector $\mathbf d$ from negative to positive form an electric dipole. Its moment $\mathbf p$ has units $\mathrm{C\,m}$:

$$\boxed{\mathbf p=q\mathbf d}.$$

Its total charge is zero, but the two charges occupy different positions. With charges at $\pm\mathbf d/2$, superposition gives the exact field:

$$\mathbf E(\mathbf r)=\frac{q}{4\pi\varepsilon_0}\left[\frac{\mathbf r-\mathbf d/2}{|\mathbf r-\mathbf d/2|^3}-\frac{\mathbf r+\mathbf d/2}{|\mathbf r+\mathbf d/2|^3}\right].$$

Far away ($r\gg d$), the ratio $d/r$ is small. To see *why* the answer changes power law, let $\mathbf f(\mathbf r)=\mathbf r/r^3$. Taylor-expand both displaced sources, keeping only their first displacement term:

$$\mathbf f(\mathbf r\pm\mathbf d/2)\simeq\mathbf f(\mathbf r)\pm\frac12(\mathbf d\cdot\nabla)\mathbf f(\mathbf r).$$

The two zeroth-order terms cancel because the net charge is zero; the remaining first-order term is $-(\mathbf d\cdot\nabla)(\mathbf r/r^3)$. Differentiating this vector expression gives

$$\boxed{\mathbf E_{\rm dip}(\mathbf r)\simeq\frac{3(\mathbf p\cdot\hat{\mathbf r})\hat{\mathbf r}-\mathbf p}{4\pi\varepsilon_0r^3}}.$$

The field falls as $r^{-3}$, faster than a point charge's $r^{-2}$ field because the net monopole contribution has cancelled. On the dipole axis the field points along $\mathbf p$ with magnitude $2p/(4\pi\varepsilon_0r^3)$; on its perpendicular bisector it points against $\mathbf p$ with magnitude $p/(4\pi\varepsilon_0r^3)$. Chapter 3 will obtain the same far field more economically by differentiating the dipole potential.

## 1.9 How a charge or dipole responds

A point charge accelerates according to $m\mathbf a=q\mathbf E$ when magnetic and relativistic effects are negligible. For a *rigid* dipole in a uniform field, the forces on its charges are equal and opposite, so the net force is zero. Because the forces act at different points, they still produce a torque:

$$\boxed{\boldsymbol\tau=\mathbf p\times\mathbf E},\qquad \tau=pE\sin\theta.$$

The torque $\boldsymbol\tau$ (newton-metres, $\mathrm{N\,m}$) tends to reduce the angle $\theta$ (radians) between $\mathbf p$ and $\mathbf E$. To obtain potential energy, start from work rather than guessing a cosine. Put the charges $\pm q$ at distance $a=d/2$ from the centre. A small rotation $d\theta$ moves each charge tangentially by $ds=a\,d\theta$. The total component of electric force opposing an *increase* of $\theta$ is $2qE\sin\theta$, so the field does

$$dW_{\rm field}=-2(qE\sin\theta)(a\,d\theta)=-pE\sin\theta\,d\theta.$$

Potential energy $U$ is measured in joules ($\mathrm J$) and increases by the **opposite** of work done by the field: $dU=-dW_{\rm field}$. Only energy *differences* have physical meaning, so choose $U(\pi/2)=0$ as a convenient reference:

$$U(\theta)-U(\pi/2)=\int_{\pi/2}^{\theta}pE\sin\theta'\,d\theta'\quad\Rightarrow\quad\boxed{U=-pE\cos\theta=-\mathbf p\cdot\mathbf E}.$$

The aligned state $\theta=0$ has the lowest potential energy. The argument assumes fixed $p$, uniform $\mathbf E$ and a quasistatic rotation; it is not automatically the energy formula for a field-induced dipole whose magnitude changes.

If the field is nonuniform, the two forces need not cancel. For a dipole small relative to the scale of field variation,

$$\mathbf F=q\left[\mathbf E(\mathbf r+\mathbf d/2)-\mathbf E(\mathbf r-\mathbf d/2)\right]\simeq\boxed{(\mathbf p\cdot\nabla)\mathbf E}.$$

In an electrostatic field with fixed $\mathbf p$, this is also $\mathbf F=\nabla(\mathbf p\cdot\mathbf E)$.

## 1.10 Point charges as charge densities

The three-dimensional Dirac delta $\delta^{(3)}$ has units $\mathrm{m^{-3}}$ and picks out the value of a function at a specified point $\mathbf a$:

$$\int f(\mathbf r)\delta^{(3)}(\mathbf r-\mathbf a)\,d^3r=f(\mathbf a).$$

Thus a collection of point charges can be written as a density,

$$\boxed{\rho(\mathbf r)=\sum_iq_i\delta^{(3)}(\mathbf r-\mathbf r_i)}.$$

Substitution into the continuous field integral recovers the discrete sum exactly. The delta function does not turn point charges into extended objects; it allows both descriptions to use the same integral formula.

---
**Reference.** R. Shankar, *Fundamentals of Physics II: Electromagnetism, Optics, and Quantum Mechanics*, Chapters 1–2 (primary explanatory route), §3.1–3.2 (models);  David Halliday, Robert Resnick and Jearl Walker, *Fundamentals of Physics*, 12th ed., Chapters 21–22; David J. Griffiths, *Introduction to Electrodynamics*, 5th ed., Chapters 1–3 (selective mathematical extensions).
