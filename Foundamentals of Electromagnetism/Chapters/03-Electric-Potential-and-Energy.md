# Chapter 3 — Electric Potential and Electrostatic Energy

The field tells us the force on a charge at each position. Potential gives another description: how much work the field can do as a charge moves between positions. A scalar potential is often easier to calculate than a vector field, and the connection between them reveals why electrostatics is naturally a boundary-value problem.

## 3.1 Work and the conservative electric field

Work $W$ and energy $U$ are measured in joules ($\mathrm J$). The electric force on a charge is $\mathbf F=q\mathbf E$, so its work along a path $C$ from points $A$ to $B$ is

$$W_{A\to B}=\int_C\mathbf F\cdot d\mathbf l=q\int_C\mathbf E\cdot d\mathbf l.$$

Does the answer depend on the path? For a static *point* source, Coulomb's field is radial and its work can be integrated using only the initial and final radii:

$$W_{A\to B}=\frac{qQ}{4\pi\varepsilon_0}\int_{r_A}^{r_B}\frac{dr}{r^2}=\frac{qQ}{4\pi\varepsilon_0}\left(\frac1{r_A}-\frac1{r_B}\right).$$

The endpoints alone determine the answer. Since a sum of conservative fields is also conservative, superposition establishes the same result for arbitrary static charge distributions (away from their singularities):

$$\boxed{\oint_C\mathbf E\cdot d\mathbf l=0}.$$

This is a property of *electrostatics*, not of general time-dependent electromagnetic fields. Induced electric fields in Chapter 9 can have nonzero circulation.

## 3.2 Potential difference and reference level

For a conservative force, the change of potential energy is the negative of the work done by the field: $\Delta U=-W_{A\to B}$. Dividing by a test charge defines the electric potential $\phi$, measured in volts ($1\,\mathrm V=1\,\mathrm{J/C}$), through its difference between two points:

$$\boxed{\phi(B)-\phi(A)=-\int_A^B\mathbf E\cdot d\mathbf l},\qquad U=q\phi\ \text{(for a test charge in an external field)}.$$

Only differences matter. Here $C$ is an arbitrary constant potential offset, not capacitance. The shift $\phi\mapsto\phi+C$ changes no electric field, so we can set $\phi(\infty)=0$ for sufficiently localised sources. For a point charge $Q$,

$$\boxed{\phi(r)=\frac{Q}{4\pi\varepsilon_0r}}.$$

The sign follows the source charge: a positive charge produces positive potential relative to infinity, while a negative charge produces negative potential.

## 3.3 Recovering the field from potential

For an infinitesimal displacement, $d\phi=-\mathbf E\cdot d\mathbf l$. But the differential of any scalar function is $d\phi=\nabla\phi\cdot d\mathbf l$. Since $d\mathbf l$ can point anywhere,

$$\boxed{\mathbf E=-\nabla\phi}.$$

The curl of a smooth gradient is zero, giving the second static-field equation,

$$\boxed{\nabla\times\mathbf E=0}.$$

Along an equipotential surface $d\phi=0$, so $\mathbf E$ is perpendicular to its tangent directions. This is why electric field lines cross equipotentials normally (except at points where $\mathbf E=0$).

## 3.4 Potential of a continuous source

It is usually easier to add *scalar potentials* than electric-field vectors. By superposition, a distribution $\rho(\mathbf r')$ ($\mathbf r'$ is source position vector, $\mathbf r$ is observation position vector) creates

$$\boxed{\phi(\mathbf r)=\frac1{4\pi\varepsilon_0}\int_V\frac{\rho(\mathbf r')}{|\mathbf r-\mathbf r'|}\,d^3r'}.$$

For line and surface charges replace $\rho\,dV$ by $\lambda\,dl$ or $\sigma\,dS$. Differentiating with respect to the *observation coordinate* $\mathbf r$ gives the Coulomb-field integral of Chapter 1. The source coordinate $\mathbf r'$ is held fixed during this differentiation.

## 3.5 Dipole potential and multipole approximation

For charges $+q$ and $-q$ at $\pm\mathbf d/2$,

$$\phi(\mathbf r)=\frac{q}{4\pi\varepsilon_0}\left(\frac1{|\mathbf r-\mathbf d/2|}-\frac1{|\mathbf r+\mathbf d/2|}\right).$$

At $r\gg d$, the source separation is small relative to the observation distance. Use $1/|\mathbf r-\mathbf r'|\simeq 1/r+(\hat{\mathbf r}\cdot\mathbf r')/r^2$ (by using the Taylor expansion, more specifically, the binomial expansion) for $|\mathbf r'|/r\ll1$, and retain the first nonzero term. For the dipole, the two $1/r$ terms cancel because the net charge is zero. the potential becomes

$$\boxed{\phi_{\rm dip}(\mathbf r)\simeq\frac{\mathbf p\cdot\hat{\mathbf r}}{4\pi\varepsilon_0r^2}}.$$

Applying $-\nabla$ recovers the dipole field already derived from the forces. The gain is clear: one scalar formula generates all components of the field.

For a general localised charge distribution, applying that same source-size expansion at large $r$ gives

$$\phi(\mathbf r)=\frac1{4\pi\varepsilon_0}\int_V{\rho(\mathbf r')}\left[\frac{1}{r}+\frac{(\hat{\mathbf r}\cdot\mathbf r')}{r^2}+O(r^{-3})\right]\,d^3r'=\frac1{4\pi\varepsilon_0}\left[\frac Qr+\frac{\mathbf p\cdot\hat{\mathbf r}}{r^2}+O(r^{-3})\right],$$

where $Q=\int\rho\,dV$ and $\mathbf p=\int\mathbf r'\rho(\mathbf r')\,dV'$. If $Q\neq0$, the monopole dominates. If $Q=0$ but $\mathbf p\neq0$, the dipole dominates. The next term describes quadrupole structure; its full tensor expression is not needed yet. A non-neutral source has an origin-dependent dipole moment, so always state the expansion centre.

## 3.6 Energy of a collection of charges

Imagine assembling fixed charges by bringing them from infinity, one at a time. The first requires no interaction work, the second works against the first, the third against the first two, and so on. Each pair is counted exactly once:

$$\boxed{U_{\rm int}=\frac1{4\pi\varepsilon_0}\sum_{i<j}\frac{q_iq_j}{r_{ij}}}.$$

The value can be positive or negative because charges of opposite signs lower the interaction energy. It does not include the infinite self-energy that results if ideal point charges are treated as fields extending all the way to $r=0$.

## 3.7 Energy in a continuous electric field

The work needed to assemble a continuous distribution can be written as $\frac12\int\rho\phi\,dV$. The factor $1/2$ prevents counting every pair twice(consider 2 charges $q_1$ and $q_2$, $U_{sum}=q_1\phi(\mathbf r_1)+q_2\phi(\mathbf r_2)=2U$, in fact, describing the interaction between two charges twice), assuming linear electrostatics and using the total potential generated by the distribution:

$$U=\frac12\int_V\rho\phi\,dV.$$

Gauss's law gives $\rho=\varepsilon_0\nabla\cdot\mathbf E$. Use the product rule together with $\nabla\phi=-\mathbf E$:

$$\nabla\cdot(\phi\mathbf E)=\phi\nabla\cdot\mathbf E+\mathbf E\cdot\nabla\phi=\phi\nabla\cdot\mathbf E-E^2.$$

Hence over a region $V$,

$$U=\frac{\varepsilon_0}{2}\int_VE^2\,dV+\frac{\varepsilon_0}{2}\oint_{\partial V}\phi\mathbf E\cdot d\mathbf S.$$

For regular localised sources integrated over all space, the boundary term vanishes at infinity, leaving

$$\boxed{U=\frac{\varepsilon_0}{2}\int_{\mathbb R^3}E^2\,dV},\qquad\boxed{u_E=\frac{\varepsilon_0E^2}{2}}.$$

Here $u_E$ is energy per unit volume ($\mathrm{J/m^3}$). This form suggests that energy is distributed throughout the field, not simply attached to each pair of charges. The distinction between field energy and renormalised pair interaction energy matters for ideal point charges, whose individual self-energies diverge.

## 3.8 Poisson's and Laplace's equations

We now have two equations: $\nabla\cdot\mathbf E=\rho/\varepsilon_0$ and $\mathbf E=-\nabla\phi$. Eliminating $\mathbf E$ gives

$$-\nabla\cdot(\nabla\phi)=\frac\rho{\varepsilon_0}\quad\Rightarrow\quad\boxed{\nabla^2\phi=-\frac\rho{\varepsilon_0}}\qquad\text{(Poisson)}.$$

Where there is no charge, $\rho=0$ and

$$\boxed{\nabla^2\phi=0}\qquad\text{(Laplace)}.$$

The source density specifies the equation; conductors or surrounding materials supply *boundary conditions*. Knowing both turns electrostatics into a well-posed problem. Chapter 4 uses that idea to explain a method that initially looks like a trick: imaginary image charges.

---
**Reference.** R. Shankar, *Fundamentals of Physics II: Electromagnetism, Optics, and Quantum Mechanics*, Chapter 5 and §§6.1–6.3, 6.7, 7.1;  David Halliday, Robert Resnick and Jearl Walker, *Fundamentals of Physics*, 12th ed., Chapters 24–25; David J. Griffiths, *Introduction to Electrodynamics*, 5th ed., Chapters 2–3.
