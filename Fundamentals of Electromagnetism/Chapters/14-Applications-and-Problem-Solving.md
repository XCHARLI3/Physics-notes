# 14. Applications and Problem-Solving in Electromagnetism

After going through the basic laws of electromagnetism, it is worth taking a step back and looking at how we actually use them. A question may look unfamiliar simply because the shape of the charge distribution or the arrangement of the conductors has changed. The physics behind it is often exactly the same.

For many problems, once we have worked out the geometry and written down the correct integral, the rest is just calculus. The harder part is deciding what to integrate, what can be simplified, and sometimes whether we need to integrate at all.

The purpose of this chapter is to bring the earlier chapters together rather than introduce another set of laws to remember. We will use a few examples to see how the same way of thinking works in electrostatics, magnetostatics, materials, induction and circuits.

Unless stated otherwise, we use SI units, idealised geometries and the usual electrostatic, magnetostatic or lumped-circuit approximations as appropriate.

## 14.1 What kind of problem are we solving?

Before looking for a formula, ask what is given and what is actually unknown. Most of the problems in these notes fall into four groups.

**We know the source and want the field.** If the charge distribution is given, we can find the electric field or potential. If a steady current distribution is given, we can find the magnetic field or vector potential.

$$
\rho(\mathbf r')\longrightarrow V(\mathbf r),\,\mathbf E(\mathbf r),
\qquad
\mathbf J(\mathbf r')\longrightarrow\mathbf A(\mathbf r),\,\mathbf B(\mathbf r).
$$

**We know the boundary conditions but not all the sources.** A point charge near a grounded conductor is a good example. We know the point charge, but we do not know how the charge on the conductor redistributes. We cannot simply integrate over an unknown surface charge density. Instead, we solve for the potential using Poisson's or Laplace's equation and the conditions on the conductor.

**We know the field and want to know what it does.** This could mean finding the force on a wire, the torque on a dipole, the energy stored in a field, or the emf induced in a coil. There is usually no need to calculate the field again if it is already given.

**We want to know how a system changes with time.** Charging a capacitor, switching on an inductor and the oscillations of an LC circuit are examples. The physical laws give us a differential equation. Initial conditions tell us which solution describes the actual system.

These categories often overlap. A question about a capacitor may ask us to find the field first, then the capacitance, and finally the force between its plates. It helps to see the question as a sequence of small problems instead of trying to find one formula for everything.

## 14.2 Get the geometry right first

### Source point and observation point

In a field calculation, there are usually two different positions. Keep them separate:

- $\mathbf r'$ is the position of the source element.
- $\mathbf r$ is the position where we want to find the field.

The displacement from the source to the observation point is

$$
\mathbf R=\mathbf r-\mathbf r',\qquad
R=|\mathbf R|,\qquad
\hat{\mathbf R}=\frac{\mathbf R}{R}.
$$

When integrating over the source, $\mathbf r$ stays fixed while $\mathbf r'$ changes. When differentiating the resulting field with respect to the observation coordinates, it is the other way round: the source coordinates are held fixed.

This is the same idea behind both Coulomb's law and the Biot–Savart law:

$$
\mathbf E(\mathbf r)=\frac{1}{4\pi\varepsilon_0}\int\frac{\hat{\mathbf R}}{R^2}\,dq,
$$

$$
\mathbf B(\mathbf r)=\frac{\mu_0 I}{4\pi}\int_C\frac{d\mathbf l'\times\hat{\mathbf R}}{R^2}.
$$

Here $\varepsilon_0$ is the vacuum permittivity (F/m), $\mu_0$ is the vacuum permeability (H/m), $dq$ is a charge element (C), and $I$ is the steady current (A). The second expression is for a thin wire carrying a steady current.

### Separate the magnitude from the direction

A vector integral is often easier if we treat its magnitude and direction separately. For example, we can write

$$
\hat{\mathbf R}=\frac{R_x\hat{\mathbf x}+R_y\hat{\mathbf y}+R_z\hat{\mathbf z}}{\sqrt{R_x^2+R_y^2+R_z^2}}.
$$

Once the geometry gives us $R_x,R_y,R_z$, the electric field calculation becomes three scalar integrals:

$$
E_i=\frac{1}{4\pi\varepsilon_0}\int\frac{R_i}{R^3}\,dq,
\qquad i=x,y,z.
$$

For a current element, write $d\mathbf l'=\hat{\mathbf t}'\,dl'$, where $\hat{\mathbf t}'$ points along the current. Then

$$
d\mathbf B=\frac{\mu_0 I}{4\pi R^2}\,dl'\,(\hat{\mathbf t}'\times\hat{\mathbf R}).
$$

If $\theta$ is the angle between these two unit vectors, we can also write

$$
d\mathbf B=\frac{\mu_0 I}{4\pi}\frac{\sin\theta}{R^2}\,dl'\,\hat{\mathbf n},
$$

where $\hat{\mathbf n}$ is the direction of the cross product whenever it is non-zero. If the two vectors are parallel, that contribution is zero.

The point is not to avoid vectors altogether. It is to deal with the vector geometry first and leave the scalar part to calculus.

One thing to watch out for: **a unit vector is not necessarily constant.** In cylindrical coordinates,

$$
\hat{\mathbf s}=\cos\phi\,\hat{\mathbf x}+\sin\phi\,\hat{\mathbf y},
\qquad
\hat{\boldsymbol\phi}=-\sin\phi\,\hat{\mathbf x}+\cos\phi\,\hat{\mathbf y}.
$$

Therefore

$$
\frac{\partial\hat{\mathbf s}}{\partial\phi}=\hat{\boldsymbol\phi},\qquad
\frac{\partial\hat{\boldsymbol\phi}}{\partial\phi}=-\hat{\mathbf s}.
$$

We cannot take a position-dependent unit vector outside an integral or ignore its derivative. If we are unsure, writing everything in the fixed Cartesian basis is usually a safe option.

### Example: electric field on the axis of a charged ring

Take a ring of radius $a$ (m) with total charge $Q$ (C), uniformly distributed around the ring. Put the ring in the $xy$ plane and find the field at a point on the $z$ axis.

We can describe a source point and the observation point as

$$
\mathbf r'=a\cos\phi\,\hat{\mathbf x}+a\sin\phi\,\hat{\mathbf y},
\qquad \mathbf r=z\hat{\mathbf z}.
$$

Hence

$$
\mathbf R=-a\cos\phi\,\hat{\mathbf x}-a\sin\phi\,\hat{\mathbf y}+z\hat{\mathbf z},
\qquad R=\sqrt{a^2+z^2}.
$$

The line charge density is $\lambda=Q/(2\pi a)$ (C/m). Since the arc length is $dl'=a\,d\phi$,

$$
dq=\lambda a\,d\phi=\frac{Q}{2\pi}\,d\phi.
$$

Putting everything into Coulomb's law gives

$$
\begin{aligned}
\mathbf E(z)&=\frac{1}{4\pi\varepsilon_0}\int_0^{2\pi}\frac{\mathbf R}{R^3}\,dq\\
&=\frac{Q}{8\pi^2\varepsilon_0(a^2+z^2)^{3/2}}
\int_0^{2\pi}(-a\cos\phi\,\hat{\mathbf x}-a\sin\phi\,\hat{\mathbf y}+z\hat{\mathbf z})\,d\phi.
\end{aligned}
$$

The integrals of sine and cosine over a full circle are zero. The integral of $z$ is $2\pi z$. We are left with

$$
\boxed{\mathbf E(z)=\frac{Qz}{4\pi\varepsilon_0(a^2+z^2)^{3/2}}\hat{\mathbf z}.}
$$

We could have saved some work by noticing that opposite points on the ring give cancelling transverse components. The remaining component is simply

$$
dE_z=\frac{dq}{4\pi\varepsilon_0R^2}\frac{z}{R}.
$$

This is the same calculation, with the symmetry used before the integration rather than afterwards. The signed factor $z/R$ also gives the correct direction below the ring.

Related example: [OpenStax, *University Physics Volume 2*, §5.5 — Calculating Electric Fields of Charge Distributions](https://openstax.org/books/university-physics-volume-2/pages/5-5-calculating-electric-fields-of-charge-distributions).

## 14.3 Choose the integration element carefully

The integration variable should describe the object we are integrating over. For example, a line charge density is charge per unit length, so it must be multiplied by a length element, not just by an angle.

| Charge distribution | Charge element | Density unit |
| --- | --- | --- |
| Point charges | $q_i$ (sum over charges) | C for each charge |
| Line | $dq=\lambda\,dl'$ | C/m |
| Surface | $dq=\sigma\,dS'$ | C/m² |
| Volume | $dq=\rho\,dV'$ | C/m³ |

For a steady current, the corresponding source elements in the Biot–Savart integral are:

| Current distribution | Source element | Density unit |
| --- | --- | --- |
| Thin wire | $I\,d\mathbf l'$ | A for $I$ |
| Surface current | $\mathbf K\,dS'$ | A/m |
| Volume current | $\mathbf J\,dV'$ | A/m² |

Each magnetic source element has units of A m. Do not confuse $\mathbf J\,dV'$ with the current through a surface, which is instead $dI=\mathbf J\cdot d\mathbf S'$.

The coordinate system should follow the shape of the system whenever possible. Using $s$ for the cylindrical radius and $r$ for the spherical radius, the usual elements are:

| Coordinates | Displacement element $d\mathbf l$ | Volume element $dV$ |
| --- | --- | --- |
| Cartesian | $dx\,\hat{\mathbf x}+dy\,\hat{\mathbf y}+dz\,\hat{\mathbf z}$ | $dx\,dy\,dz$ |
| Cylindrical | $ds\,\hat{\mathbf s}+s\,d\phi\,\hat{\boldsymbol\phi}+dz\,\hat{\mathbf z}$ | $s\,ds\,d\phi\,dz$ |
| Spherical | $dr\,\hat{\mathbf r}+r\,d\theta\,\hat{\boldsymbol\theta}+r\sin\theta\,d\phi\,\hat{\boldsymbol\phi}$ | $r^2\sin\theta\,dr\,d\theta\,d\phi$ |

Here $\theta$ is the polar angle measured from the positive $z$ axis, and $\phi$ is the azimuthal angle.

For surface integrals, use the area element of the actual surface. A few useful cases are

$$
\begin{aligned}
\text{Flat disc: } &dS=s\,ds\,d\phi,\\
\text{Cylinder side: } &dS=s\,d\phi\,dz\quad(s\text{ fixed}),\\
\text{Sphere: } &dS=r^2\sin\theta\,d\theta\,d\phi\quad(r\text{ fixed}).
\end{aligned}
$$

For a flux integral we also need the normal, $d\mathbf S=\hat{\mathbf n}\,dS$. For a line integral we need the direction along the path. A useful way of remembering the factors of $r$ or $s$ is that a small angular change is not a small length until it is multiplied by the appropriate radius.

### Example: a charged disc as a collection of rings

Instead of starting again with a double integral, we can use the result for the ring. Let a disc of radius $a$ have uniform surface charge density $\sigma$ (C/m²). Find the electric field at height $z>0$ on the axis.

Split the disc into thin concentric rings. A ring of radius $s$ and width $ds$ has area and charge

$$
dS=2\pi s\,ds,\qquad dq=2\pi\sigma s\,ds.
$$

The field due to that ring is already known:

$$
dE_z=\frac{1}{4\pi\varepsilon_0}\frac{z\,dq}{(s^2+z^2)^{3/2}}.
$$

All we need now is to add up the rings from the centre to the edge:

$$
\begin{aligned}
E_z&=\frac{\sigma z}{2\varepsilon_0}\int_0^a\frac{s\,ds}{(s^2+z^2)^{3/2}}\\
&=\frac{\sigma z}{2\varepsilon_0}\left[-\frac{1}{\sqrt{s^2+z^2}}\right]_0^a\\
&=\frac{\sigma z}{2\varepsilon_0}\left(\frac{1}{z}-\frac{1}{\sqrt{a^2+z^2}}\right).
\end{aligned}
$$

Therefore, above the disc,

$$
\boxed{\mathbf E(z)=\frac{\sigma}{2\varepsilon_0}\left(1-\frac{z}{\sqrt{a^2+z^2}}\right)\hat{\mathbf z}.}
$$

Below the disc the field is obtained by reflection, $E_z(-z)=-E_z(z)$. At the charged surface itself, the two one-sided limits differ.

This way of splitting an object into smaller objects whose fields we already know is useful in many other problems:

- A disc is a collection of rings.
- A solid cylinder is a collection of discs.
- A solenoid is a collection of current loops.
- A polarised material can be thought of as a distribution of small electric dipoles.

This is just superposition. For prescribed sources in vacuum, the total field is the sum of their individual fields. We do not always have to start from point sources if a simpler building block is already available.

Related example: [OpenStax §5.5 — Calculating Electric Fields of Charge Distributions](https://openstax.org/books/university-physics-volume-2/pages/5-5-calculating-electric-fields-of-charge-distributions).

## 14.4 Use symmetry before doing the integral

Symmetry is one of the easiest ways to reduce the amount of calculation. Ask three questions:

1. Which directions can the field point in?
2. Which coordinates can it depend on?
3. Where must its magnitude or components be the same?

The answers must come from the symmetry of the whole physical system, including any boundaries and other sources, not just the shape of one object.

For example, a spherically symmetric charge density in otherwise empty space gives $\mathbf E=E(r)\hat{\mathbf r}$. An infinitely long, uniformly charged cylinder gives $\mathbf E=E(s)\hat{\mathbf s}$. A uniform infinite charged plane gives $\mathbf E=E(z)\hat{\mathbf z}$. In the case of an infinitely long circular wire carrying axial current, the magnetic field is instead azimuthal, $\mathbf B=B(s)\hat{\boldsymbol\phi}$.

Notice that a finite cylinder and an infinite cylinder do not have the same symmetry. A finite cylinder has ends, so its field may depend on both $s$ and $z$. Simply seeing a circular cross-section does not justify treating the field as a function of $s$ alone.

### Example: a sphere with non-uniform charge density

Consider a solid sphere of radius $a$ with

$$
\rho(r)=\rho_0\frac{r}{a},\qquad 0\leq r\leq a,
$$

and no charge outside. Here $\rho_0$ has units C/m³. The charge density is not uniform, but it is still spherically symmetric: every point at the same distance from the centre has the same density.

Choose a spherical Gaussian surface of radius $r$. Gauss's law becomes

$$
\oint_S\mathbf E\cdot d\mathbf S=4\pi r^2E(r)=\frac{Q_{\mathrm{enc}}}{\varepsilon_0}.
$$

**Inside the sphere**, the amount of enclosed charge depends on $r$. Using $u$ as the integration variable so that we do not confuse it with the radius of the Gaussian surface,

$$
\begin{aligned}
Q_{\mathrm{enc}}(r)&=\int_0^r\rho(u)4\pi u^2\,du\\
&=\frac{4\pi\rho_0}{a}\int_0^r u^3\,du=\frac{\pi\rho_0r^4}{a}.
\end{aligned}
$$

Substituting this into Gauss's law gives

$$
E_{\mathrm{in}}(r)=\frac{\rho_0r^2}{4\varepsilon_0a}.
$$

**Outside the sphere**, increasing the radius of the Gaussian surface does not enclose any more charge. Thus $Q_{\mathrm{enc}}=Q=\pi\rho_0a^3$ and

$$
E_{\mathrm{out}}(r)=\frac{\rho_0a^3}{4\varepsilon_0r^2}.
$$

Putting the two regions together,

$$
\boxed{
\mathbf E(r)=\begin{cases}
\dfrac{\rho_0r^2}{4\varepsilon_0a}\hat{\mathbf r},&0<r<a,\\[6pt]
\dfrac{\rho_0a^3}{4\varepsilon_0r^2}\hat{\mathbf r},&r\geq a.
\end{cases}}
$$

At the centre, $\mathbf E=0$. For positive $\rho_0$, the field grows as $r^2$ inside and decreases as $1/r^2$ outside. Both expressions give the same value at $r=a$, as expected when there is no additional surface charge.

The only integral we needed was the one for the enclosed charge. We did not have to integrate the electric field from every source point.

This is a variation on the spherical symmetry examples in [OpenStax §6.3 — Applying Gauss's Law](https://openstax.org/books/university-physics-volume-2/pages/6-3-applying-gausss-law).

### When do Gauss's law and Ampère's law actually help?

Gauss's law relates the electric flux through a closed surface to the enclosed charge. It does not, by itself, give the electric field at a particular point. Similarly, the magnetostatic form of Ampère's law relates the circulation of the magnetic field to the net current passing through the spanning surface.

$$
\oint_S\mathbf E\cdot d\mathbf S=\frac{Q_{\mathrm{enc}}}{\varepsilon_0},\qquad
\oint_C\mathbf B\cdot d\mathbf l=\mu_0 I_{\mathrm{enc}}.
$$

These laws do not stop being true when we lose symmetry. We simply lose the ability to take the field out of the integral.

For example, consider two parallel infinite wires and a circular Ampèrian loop around only the first wire. The second wire contributes to the magnetic field at almost every point on the loop, but its contribution to the circulation is zero. To see why, for an infinite wire we can write

$$
\mathbf B\cdot d\mathbf l=\frac{\mu_0 I}{2\pi s}\hat{\boldsymbol\phi}\cdot(d s\,\hat{\mathbf s}+s\,d\phi\,\hat{\boldsymbol\phi})=\frac{\mu_0 I}{2\pi}\,d\phi.
$$

Here the polar coordinates are measured from that wire, not from the centre of the chosen loop. If the loop does not surround the wire, the net change in polar angle is zero. The positive and negative contributions cancel.

$$
\oint_C\mathbf B_{\mathrm{out}}\cdot d\mathbf l=0.
$$

This does not mean $\mathbf B_{\mathrm{out}}=0$. The total field may no longer be constant or tangential around the chosen circle. In that case we cannot write $B_{\mathrm{total}}2\pi s=\mu_0 I_{\mathrm{enc}}$.

The general magnetostatic version follows from Stokes' theorem and $\nabla\times\mathbf B=\mu_0\mathbf J$: only the net current crossing the surface contributes to the circulation. An analogous distinction applies to Gauss's law: external charges can affect the local electric field without contributing net flux through a closed surface.

See [OpenStax §12.5 — Ampère's Law](https://openstax.org/books/university-physics-volume-2/pages/12-5-amperes-law).

## 14.5 Choose a law that makes the calculation easier

There is often more than one way to solve the same problem. The choice depends on what is known and how much symmetry we have.

| System | A good starting point |
| --- | --- |
| Finite line charge | Coulomb's law or electric potential |
| Charged ring or disc, on the axis | Coulomb's law or electric potential |
| Infinite line charge or cylinder | Gauss's law |
| Spherically symmetric charge | Gauss's law |
| Infinite uniform charged plane | Gauss's law |
| Finite straight segment of a steady-current circuit | Biot–Savart law (include the rest of the circuit if required) |
| Circular current loop, on the axis | Biot–Savart law |
| Infinite straight wire | Ampère's law |
| Ideal infinitely long solenoid or toroidal solenoid | Ampère's law, using the appropriate symmetry |
| Grounded conductor with an external charge | Poisson/Laplace equation and boundary conditions |

### Sometimes it is easier to calculate the potential first

In electrostatics, instead of directly calculating the vector field, we can use the scalar potential

$$
V(\mathbf r)=\frac{1}{4\pi\varepsilon_0}\int\frac{dq}{R},\qquad \mathbf E=-\nabla V.
$$

The integral formula assumes a localised prescribed charge distribution in free space with the potential reference at infinity. For infinite charge distributions we may need a finite reference point or potential difference instead.

Let us return to the charged ring in Section 14.2. All points on the ring are the same distance from the observation point on the axis, so

$$
V(z)=\frac{1}{4\pi\varepsilon_0\sqrt{a^2+z^2}}\int dq
=\frac{Q}{4\pi\varepsilon_0\sqrt{a^2+z^2}}.
$$

Differentiating,

$$
\begin{aligned}
E_z&=-\frac{dV}{dz}\\
&=-\frac{Q}{4\pi\varepsilon_0}\left(-\frac12\right)(a^2+z^2)^{-3/2}(2z)\\
&=\frac{Qz}{4\pi\varepsilon_0(a^2+z^2)^{3/2}}.
\end{aligned}
$$

This is the same result, without a vector integral. The symmetry of the ring tells us that the other components are zero on the axis. Knowing the potential only along the axis would not in general be enough to find the transverse derivatives.

Related material: [OpenStax §7.3 — Calculations of Electric Potential](https://openstax.org/books/university-physics-volume-2/pages/7-3-calculations-of-electric-potential).

There is a similar idea in magnetostatics. In free space, for a localised steady current distribution, we can use the vector potential

$$
\mathbf A(\mathbf r)=\frac{\mu_0}{4\pi}\int\frac{\mathbf J(\mathbf r')}{R}\,dV',\qquad \mathbf B=\nabla\times\mathbf A.
$$

Unlike $V$, $\mathbf A$ (T m) is a vector, but in some geometries it is simpler to calculate than $\mathbf B$ directly.

### Example: a wire with non-uniform current density

Take an infinitely long cylindrical wire of radius $a$ with current density

$$
\mathbf J(s)=J_0\frac{s}{a}\hat{\mathbf z},\qquad 0\leq s\leq a,
$$

where $J_0$ is measured in A/m². There is no current outside the wire.

The system has cylindrical symmetry and the magnetic field has the form $\mathbf B=B(s)\hat{\boldsymbol\phi}$. Choose a circular Ampèrian loop of radius $s$. Then

$$
\oint_C\mathbf B\cdot d\mathbf l=2\pi sB(s).
$$

Inside the wire,

$$
\begin{aligned}
I_{\mathrm{enc}}(s)&=\int_S\mathbf J\cdot d\mathbf S\\
&=\int_0^s J_0\frac{u}{a}2\pi u\,du=\frac{2\pi J_0s^3}{3a}.
\end{aligned}
$$

Therefore,

$$
B_{\mathrm{in}}(s)=\frac{\mu_0 I_{\mathrm{enc}}(s)}{2\pi s}=\frac{\mu_0J_0s^2}{3a}.
$$

Outside, the enclosed current is the total current $2\pi J_0a^2/3$, giving

$$
\boxed{\mathbf B(s)=\begin{cases}
\dfrac{\mu_0J_0s^2}{3a}\hat{\boldsymbol\phi},&0<s<a,\\[6pt]
\dfrac{\mu_0J_0a^2}{3s}\hat{\boldsymbol\phi},&s\geq a.
\end{cases}}
$$

At the centre, $\mathbf B=0$. Compare this with the non-uniform sphere. We have done exactly the same kind of calculation: use symmetry, choose a surface or loop, calculate how much source is enclosed, and treat the inside and outside separately.

This power-law example is a variation of the non-uniform wire problem in [MIT 8.02 — Problem Solving](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/problem-solving/).

## 14.6 Divide the system into regions and match the boundaries

If the material or the source changes from one region to another, the expression for the field may also change. We saw this in the sphere and the wire. The key is to solve each region using its own equations and then connect the solutions at the interfaces.

At an ordinary interface, let $\hat{\mathbf n}$ point from region 1 to region 2. The four macroscopic Maxwell boundary conditions are

$$
\begin{aligned}
\hat{\mathbf n}\cdot(\mathbf D_2-\mathbf D_1)&=\sigma_f,\\
\hat{\mathbf n}\times(\mathbf E_2-\mathbf E_1)&=0,\\
\hat{\mathbf n}\cdot(\mathbf B_2-\mathbf B_1)&=0,\\
\hat{\mathbf n}\times(\mathbf H_2-\mathbf H_1)&=\mathbf K_f.
\end{aligned}
$$

Here $\mathbf D$ is the electric displacement (C/m²), $\mathbf H$ is the auxiliary magnetic field (A/m), $\sigma_f$ is the free surface charge density (C/m²), and $\mathbf K_f$ is the free surface current density (A/m). We assume ordinary fields with no singular time-varying flux contributions as the integration surface or loop shrinks.

There is no need to remember these as four unrelated facts. The normal conditions come from applying the two Gauss laws to a thin pillbox across the interface. The tangential conditions come from applying Faraday's law and the Ampère–Maxwell law to a thin rectangular loop across it. As the thickness tends to zero, only the appropriate normal or tangential terms remain.

A common mistake is assuming that all components of $\mathbf E$ and $\mathbf B$ are continuous. We must check which component the boundary condition actually refers to. In particular, in vacuum the normal electric field jumps by $\sigma/\varepsilon_0$ across a surface carrying total charge density $\sigma$.

### Example: a capacitor filled with two layers of dielectric

Consider a parallel-plate capacitor of plate area $A$ (m²). Between the plates are two dielectric layers stacked along the field, of thicknesses $d_1,d_2$ (m) and permittivities $\varepsilon_1,\varepsilon_2$ (F/m). Take the field direction from the positive plate to the negative plate. Assume linear isotropic dielectrics, no free charge at their interface, and negligible edge effects.

In each region,

$$
D_1=\varepsilon_1E_1,\qquad D_2=\varepsilon_2E_2.
$$

Because there is no free surface charge at the interface, the normal component of $\mathbf D$ is continuous. From the free charge $Q$ on the positive plate,

$$
D_1=D_2=\frac{Q}{A}.
$$

The electric fields are therefore

$$
E_1=\frac{Q}{A\varepsilon_1},\qquad E_2=\frac{Q}{A\varepsilon_2}.
$$

Notice that the two electric fields are generally different even though $D$ is the same. The voltage across the whole capacitor is the sum of the voltage drops through the two layers:

$$
V=E_1d_1+E_2d_2=\frac{Q}{A}\left(\frac{d_1}{\varepsilon_1}+\frac{d_2}{\varepsilon_2}\right).
$$

Using the definition of capacitance $C=Q/V$ (F),

$$
\boxed{C=\frac{A}{d_1/\varepsilon_1+d_2/\varepsilon_2}.}
$$

This is the same as two capacitors in series, each with capacitance $\varepsilon_i A/d_i$. We did not need to assume the series formula; it came directly from the field and boundary conditions. If the layers were placed side by side rather than stacked along the field, the voltage would be common and the capacitances would add, neglecting fringing fields.

### Example: a point charge above a grounded conducting plane

Now consider a different kind of boundary problem. A charge $q$ sits at $z=a>0$, above an infinite grounded conducting plane at $z=0$. The conductor must be at zero potential, but its induced surface charge distribution is not given.

Rather than trying to guess that charge distribution, use the potential equation in the region $z>0$:

$$
\nabla^2V=-\frac{\rho}{\varepsilon_0},\qquad V(s,0)=0,
$$

where the source in this region is the point charge. The potential tends to zero at infinity. Away from the point charge, the equation is simply $\nabla^2V=0$.

Imagine placing a fictitious charge $-q$ at $z=-a$. Its potential cancels the potential of $q$ everywhere on the plane, since each point on the plane is equally far from the two charges. This gives the candidate solution

$$
V(s,z)=\frac{q}{4\pi\varepsilon_0}\left[\frac{1}{\sqrt{s^2+(z-a)^2}}-\frac{1}{\sqrt{s^2+(z+a)^2}}\right],\qquad z>0.
$$

It has the correct source in the physical region, satisfies the boundary value $V(s,0)=0$, and vanishes at infinity. The uniqueness theorem tells us that this is the solution in the region above the plane. The fictitious charge is a mathematical device, not a real charge inside the conductor.

We can now calculate the actual surface charge. The normal pointing out of the conductor is $\hat{\mathbf z}$, so

$$
\begin{aligned}
E_z(s,z)&=-\frac{\partial V}{\partial z}\\
&=\frac{q}{4\pi\varepsilon_0}\left[\frac{z-a}{(s^2+(z-a)^2)^{3/2}}-\frac{z+a}{(s^2+(z+a)^2)^{3/2}}\right].
\end{aligned}
$$

Just above the surface, $E_z(s,0^+)=-qa/[2\pi\varepsilon_0(s^2+a^2)^{3/2}]$. Since the electrostatic field inside the conductor is zero,

$$
\boxed{\sigma(s)=\varepsilon_0E_z(s,0^+)=-\frac{qa}{2\pi(s^2+a^2)^{3/2}}.}
$$

So the charge distribution we could not initially integrate over has become an output of the calculation. This is why boundary conditions are so useful.

For more on boundary conditions, electrostatic uniqueness and image charges, see [David Tong, *Lectures on Electromagnetism*](https://www.damtp.cam.ac.uk/user/tong/justem.html) and [MIT 6.013 — Electromagnetics and Applications, Lecture Notes](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-fall-2005/pages/lecture-notes/).

## 14.7 Connect the physical quantities instead of memorising separate formulas

Once we know the field, there are several things we can do with it. A useful habit is to write down a short chain showing how we get from what is given to what is asked for.

| Starting point | What we want | How to get there |
| --- | --- | --- |
| Charge distribution | Electric field or potential | Coulomb, Gauss, Poisson |
| Steady current distribution | Magnetic field | Biot–Savart or Ampère |
| Electric field | Potential difference | $V_b-V_a=-\int_a^b\mathbf E\cdot d\mathbf l$ (electrostatics) |
| Magnetic field | Magnetic flux | $\Phi_B=\int_S\mathbf B\cdot d\mathbf S$ |
| Magnetic flux linkage | Induced emf | $\mathcal E=-d\lambda/dt$ |
| Electric and magnetic fields | Force | $\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B)$ |
| Fields | Stored energy | Integrate the appropriate energy density |

The same calculation can appear in several different forms. To find capacitance, for instance, we normally go from charge to electric field, then to voltage, and finally to capacitance:

$$
Q\longrightarrow\mathbf E\longrightarrow V\longrightarrow C=\frac{Q}{V}.
$$

To find a self-inductance or mutual inductance, the corresponding chain is

$$
I\longrightarrow\mathbf B\longrightarrow\Phi_B\longrightarrow\lambda\longrightarrow L\text{ or }M.
$$

In both cases the coefficient is a way of describing the response of a particular structure, rather than an extra law of electromagnetism.

### Example: mutual inductance between two coaxial coils

Take a long air-core solenoid of length $l$, radius $a$ and $N_1$ turns. Around it is another coil with $N_2$ turns and radius $b>a$. Assume that all the turns of the outer coil lie in the region where the long-solenoid approximation is valid.

We want to find the mutual inductance $M_{21}$ (H). Start with the current $I_1$ in the inner solenoid. Ampère's law gives

$$
B_1=\mu_0\frac{N_1}{l}I_1
$$

inside the solenoid, and approximately zero outside it. The next step is to find the flux through one turn of the outer coil. Although its area is $\pi b^2$, the field is only appreciable over the area $\pi a^2$. Hence

$$
\Phi_{21}=\int_{S_2}\mathbf B_1\cdot d\mathbf S_2=B_1\pi a^2.
$$

The total flux linkage in the second coil due to the first is

$$
\lambda_{21}=N_2\Phi_{21}=\mu_0\frac{N_1N_2\pi a^2}{l}I_1.
$$

Taking the positive orientations of both coils to be aligned,

$$
\boxed{M_{21}=\frac{\lambda_{21}}{I_1}=\frac{\mu_0N_1N_2\pi a^2}{l}.}
$$

What does this coefficient actually tell us? It combines two things: how effectively the first coil produces a magnetic field, and how much of that field is linked with the second coil. Changing the shape, position or orientation of either coil can change $M$. In a linear system with fixed geometry and material properties, it does not depend on the value of $I_1$.

If the current changes with time, Faraday's law gives

$$
\mathcal E_2=-\frac{d\lambda_{21}}{dt}=-M_{21}\frac{dI_1}{dt},
$$

provided $M_{21}$ is constant. If the coils move relative to each other, then $M$ may change as well, and the derivative becomes

$$
\mathcal E_2=-M_{21}\frac{dI_1}{dt}-I_1\frac{dM_{21}}{dt}.
$$

This is one reason it is better to start from the flux linkage than to memorise only the final emf formula. For self-inductance the same idea applies, except that we calculate the flux linkage of the original coil with its own field.

Related example: [OpenStax §14.1 — Mutual Inductance](https://openstax.org/books/university-physics-volume-2/pages/14-1-mutual-inductance).

### Example: an induced electric field inside and outside a solenoid

Suppose a very long solenoid of radius $a$ produces a time-dependent, approximately uniform axial magnetic field $\mathbf B=B(t)\hat{\mathbf z}$ inside, with negligible field outside. We use the quasistatic approximation, with no additional applied electric field.

We want the electric field, not just the emf in a particular wire. Because of the cylindrical symmetry of the induction problem, the induced field is azimuthal:

$$
\mathbf E=E_\phi(s,t)\hat{\boldsymbol\phi}.
$$

Choose a stationary circular path of radius $s$, oriented anticlockwise when viewed from the positive $z$ axis. Faraday's law becomes

$$
\oint_C\mathbf E\cdot d\mathbf l=-\frac{d}{dt}\int_S\mathbf B\cdot d\mathbf S,
\qquad
2\pi sE_\phi=-\frac{d\Phi_B}{dt}.
$$

The area on the right is not always the same as the area enclosed by the path. We need to work out where the magnetic field actually exists.

Inside the solenoid ($s<a$), the whole circular surface contains magnetic field:

$$
\Phi_B=\pi s^2 B(t),\qquad
2\pi sE_\phi=-\pi s^2\frac{dB}{dt}.
$$

Outside ($s>a$), only the central disc of radius $a$ contributes appreciably to the flux:

$$
\Phi_B=\pi a^2B(t),\qquad
2\pi sE_\phi=-\pi a^2\frac{dB}{dt}.
$$

Putting the results together,

$$
\boxed{\mathbf E(s,t)=\begin{cases}
-\dfrac{s}{2}\dfrac{dB}{dt}\hat{\boldsymbol\phi},&0<s<a,\\[7pt]
-\dfrac{a^2}{2s}\dfrac{dB}{dt}\hat{\boldsymbol\phi},&s\geq a.
\end{cases}}
$$

The electric field is zero at the centre and the two expressions agree at $s=a$. If $B$ increases in the positive $z$ direction, $E_\phi$ is negative, which agrees with Lenz's law.

What is interesting here is that there can be an electric field outside the solenoid even when the local magnetic field there is negligible. Faraday's law relates the circulation of the electric field to the rate of change of the flux through the surface. It does not say that the electric field depends only on the magnetic field at that particular point.

The induced electric field is also different from an electrostatic field. Its integral around a closed path can be non-zero, so in general we cannot describe it using only $\mathbf E=-\nabla V$. In the time-dependent case the more general relation is

$$
\mathbf E=-\nabla V-\frac{\partial\mathbf A}{\partial t}.
$$

Related example: [OpenStax §13.4 — Induced Electric Fields](https://openstax.org/books/university-physics-volume-2/pages/13-4-induced-electric-fields).

### A note on moving conductors

When a conducting rod moves in a magnetic field, its charges experience the magnetic part of the Lorentz force. For a moving circuit, the emf around the instantaneous circuit is

$$
\mathcal E=\oint_{C(t)}(\mathbf E+\mathbf u\times\mathbf B)\cdot d\mathbf l
=-\frac{d}{dt}\int_{S(t)}\mathbf B\cdot d\mathbf S,
$$

where $\mathbf u$ is the local velocity of the circuit element (m/s), and the last equality is the flux rule for a smoothly moving closed circuit. A change in magnetic flux can come from a changing field, a moving boundary, a changing area, or a combination of these. The magnetic force on a charge is perpendicular to its actual velocity and does no work on that charge; in a generator, the energy supplied to the circuit ultimately comes from mechanical work.

For a straight rod of length $l$ moving with speed $u$ perpendicular to a uniform magnetic field $B$, with the rod along $\mathbf u\times\mathbf B$, the magnitude of the motional emf across the rod is $Blu$. Rather than remembering this as a separate law, it is easier to see it as the integral of the motional term along the rod.

## 14.8 Sometimes energy is an easier route to the force

If we need the force on an object, we could try adding up the forces on all its charges or current elements. But if we already know how the energy depends on the position of the object, that can be a much shorter route.

In vacuum, the electric and magnetic field energies are

$$
U_E=\frac{\varepsilon_0}{2}\int E^2\,dV,\qquad
U_B=\frac{1}{2\mu_0}\int B^2\,dV.
$$

Both are in joules (J). For a system described by a potential energy $U(x)$, the conservative force along the coordinate $x$ is

$$
F_x=-\frac{\partial U}{\partial x}.
$$

But the energy we use must be appropriate to the constraints of the system. For instance, a battery can take energy from a capacitor or supply energy to it. If we ignore the battery while the voltage is held fixed, we can even get the wrong direction for the force.

### Example: pulling apart the plates of a capacitor

Take two parallel plates of area $A$, separated by a distance $d$. Neglect edge effects, so that

$$
C(d)=\frac{\varepsilon_0 A}{d}.
$$

Let $F_d$ denote the electric force in the direction of increasing plate separation. A negative result means that the plates attract.

**Case 1: the battery is disconnected.** The charge $Q$ on each plate remains fixed. The stored electric energy is

$$
U_C=\frac{Q^2}{2C}=\frac{Q^2d}{2\varepsilon_0A}.
$$

Therefore,

$$
\boxed{F_d=-\left.\frac{\partial U_C}{\partial d}\right|_Q=-\frac{Q^2}{2\varepsilon_0A}.}
$$

As we pull the plates apart, the field energy increases. The work we do against the attraction goes into that energy.

**Case 2: the battery remains connected.** The voltage $V$ stays fixed but the charge changes. The capacitor energy is now

$$
U_C=\frac12CV^2.
$$

It is tempting to differentiate this directly and put a minus sign in front. That would predict repulsion, which is not right. The problem is that the capacitor is no longer an isolated system.

For a small change in charge $dQ$, the energy transferred from the battery to the capacitor is $V\,dQ$. When $dQ<0$, energy is transferred back to the battery instead. If the plates move quasistatically, the work done by the external force satisfies

$$
dW_{\mathrm{ext}}+V\,dQ=dU_C.
$$

At fixed voltage,

$$
dQ=V\,dC,\qquad dU_C=\frac12V^2\,dC.
$$

So

$$
\begin{aligned}
dW_{\mathrm{ext}}&=dU_C-V\,dQ\\
&=\frac12V^2\,dC-V^2\,dC\\
&=-\frac12V^2\,dC.
\end{aligned}
$$

Now $dC/dd=-\varepsilon_0 A/d^2$. The electric force is opposite to the quasistatic external force, and hence

$$
\boxed{F_d=\frac12V^2\frac{dC}{dd}=-\frac{\varepsilon_0AV^2}{2d^2}.}
$$

The force is attractive in both cases. In fact, at the same instantaneous charge and separation the two expressions agree, since $Q=CV$. The difference is how the charge and field change as the separation changes.

We can also check the result directly. The field produced by one infinite charged plate has magnitude $\sigma/(2\varepsilon_0)$, so the force on the other plate has magnitude $Q\sigma/(2\varepsilon_0)=Q^2/(2\varepsilon_0A)$. We must use the field of the *other* plate, not the total field between the plates, because a plate does not exert a net force on itself.

The general lesson is to decide what is held constant — charge, voltage, current or flux linkage — before differentiating an energy expression. With magnetic systems and maintained currents, the power supplied by the current sources also matters; the field energy alone is not always the mechanical potential energy.

Related material: [OpenStax §8.3 — Energy Stored in a Capacitor](https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor).

## 14.9 Check the answer before moving on

Even if we do not know the correct answer, we can often tell whether our own answer makes sense. There are a few simple checks that are worth doing every time.

### Units

Take the self-inductance of a long air-core solenoid:

$$
L=\frac{\mu_0 N^2 A}{l}.
$$

The number of turns $N$ is dimensionless. Since $[\mu_0]=\mathrm{H/m}$, the units are

$$
[L]=\frac{\mathrm H}{\mathrm m}\frac{\mathrm m^2}{\mathrm m}=\mathrm H.
$$

If we had forgotten a factor of length or area somewhere in the calculation, the units might have revealed the mistake. The following are useful units to have in mind:

| Quantity | SI unit |
| --- | --- |
| Electric field $\mathbf E$ | V/m or N/C |
| Electric potential $V$ | V |
| Magnetic field $\mathbf B$ | T |
| Electric displacement $\mathbf D$ | C/m² |
| Auxiliary magnetic field $\mathbf H$ | A/m |
| Polarisation $\mathbf P$ | C/m² |
| Magnetisation $\mathbf M$ | A/m |
| Magnetic flux $\Phi_B$ | Wb |
| Capacitance $C$ | F |
| Self-inductance $L$, mutual inductance $M$ | H |
| Energy density | J/m³ |

### Limiting cases

A more useful check is to ask what happens in a familiar limit. Take the electric field above the charged disc from Section 14.3:

$$
E_z=\frac{\sigma}{2\varepsilon_0}\left(1-\frac{z}{\sqrt{z^2+a^2}}\right),\qquad z>0.
$$

If $a\to\infty$ while $\sigma$ and $z$ stay fixed, then

$$
E_z\to\frac{\sigma}{2\varepsilon_0}.
$$

This is the field of an infinite charged plane. If instead $z\gg a$, keeping the disc itself fixed, use the expansion

$$
\frac{z}{\sqrt{z^2+a^2}}=\left(1+\frac{a^2}{z^2}\right)^{-1/2}
\approx1-\frac{a^2}{2z^2}.
$$

It follows that

$$
E_z\approx\frac{\sigma a^2}{4\varepsilon_0z^2}=\frac{Q}{4\pi\varepsilon_0z^2},
\qquad Q=\sigma\pi a^2.
$$

From far away, the disc looks like a point charge. Both limits agree with results we already know. Checking them takes much less time than repeating the original integration.

The same idea works for many systems. A finite localised charge distribution with non-zero total charge looks like a point charge to leading order at large distances. If its total charge vanishes, the leading term may instead be a dipole or a higher multipole. An ideal infinite wire or infinite plane is not a localised source, so we should not expect the same far-field behaviour.

### Behaviour at interfaces

For the non-uniform charged sphere, we found two different expressions for the electric field, depending on whether we were inside or outside. At $r=a$ both give

$$
E(a)=\frac{\rho_0a}{4\varepsilon_0}.
$$

This makes sense because there is no extra surface charge at the boundary. For a charged spherical shell, on the other hand, the normal electric field has a jump. In vacuum,

$$
E_{2n}-E_{1n}=\frac{\sigma}{\varepsilon_0}.
$$

Do not try to force all the expressions to be continuous. Check the boundary condition first.

### Direction, signs and overall behaviour

Before finishing, ask whether the direction agrees with what we expect. Does the field due to a positive point charge point away from it? Does the magnetic field follow the right-hand rule? Does the induced emf have the sign expected from Lenz's law? If a component is forbidden by symmetry, has it disappeared from the answer?

It also helps to look at the overall shape of an answer. For the non-uniform sphere, $E$ grows as $r^2$ inside, reaches its surface value and then falls as $1/r^2$. For the cylindrical wire considered earlier, $B$ grows as $s^2$ inside and then falls as $1/s$. The different powers outside come from their different geometries.

A quick check using a differential equation can be useful too. For a spherically symmetric electrostatic field,

$$
\nabla\cdot\mathbf E=\frac{1}{r^2}\frac{d}{dr}(r^2E_r).
$$

Inserting the interior result $E_r=\rho_0r^2/(4\varepsilon_0a)$ gives

$$
\nabla\cdot\mathbf E=\frac{\rho_0r}{\varepsilon_0a}=\frac{\rho(r)}{\varepsilon_0},
$$

as required by Gauss's law. Outside, $r^2E_r$ is constant, so the divergence is zero. This connects the integral calculation back to the local field equation.

## 14.10 Putting fields, materials and circuits together

### Many of our coefficients are response coefficients

We have introduced quite a few quantities throughout these notes. They look different, but several of them serve a similar purpose: they tell us how one quantity responds to another.

| Coefficient | Linear relation | What it tells us |
| --- | --- | --- |
| Capacitance $C$ (F) | $Q=CV$ | How much charge is stored for a given voltage |
| Resistance $R$ (Ω) | $V=RI$ | How much voltage drop is needed for a given current |
| Conductance $G$ (S) | $I=GV$ | How much current flows for a given voltage |
| Self-inductance $L$ (H) | $\lambda=LI$ | How much flux linkage a circuit produces in itself |
| Mutual inductance $M$ (H) | $\lambda_{21}=M_{21}I_1$ | How much flux linkage one circuit produces in another |
| Electric susceptibility $\chi_e$ | $\mathbf P=\varepsilon_0\chi_e\mathbf E$ | How the material polarises in response to the local electric field |
| Magnetic susceptibility $\chi_m$ | $\mathbf M=\chi_m\mathbf H$ | How the material magnetises in response to the auxiliary field |
| Conductivity $\sigma_c$ (S/m) | $\mathbf J=\sigma_c\mathbf E$ | How a material conducts in response to an electric field |

Here $\chi_e$ and $\chi_m$ are dimensionless, and the material relations assume a local, linear, isotropic response. The subscript on $\sigma_c$ is used here to distinguish conductivity from surface charge density.

Some of these coefficients depend on the overall geometry, while others are material parameters within a particular model. For example, for a uniform ohmic wire of length $l$ and cross-sectional area $A$,

$$
J=\sigma_cE,\qquad I=JA,\qquad V=El.
$$

Combining these gives

$$
\boxed{R=\frac{V}{I}=\frac{l}{\sigma_c A}.}
$$

We started with a local material law and ended up with a single number describing a whole piece of wire. Finding $C$, $L$ or $M$ is often the same kind of calculation, only with a different physical response.

For several coupled coils, the same idea can be written as a matrix:

$$
\begin{pmatrix}\lambda_1\\\lambda_2\end{pmatrix}
=\begin{pmatrix}L_1&M_{12}\\M_{21}&L_2\end{pmatrix}
\begin{pmatrix}I_1\\I_2\end{pmatrix}.
$$

The diagonal terms describe the response to a coil's own current; the off-diagonal terms describe its coupling to the other coil. In a linear reciprocal magnetic system, $M_{12}=M_{21}$. More generally, the differential response can be written as $L_{ij}=\partial\lambda_i/\partial I_j$. Thinking this way makes the relationship between self-inductance and mutual inductance quite natural.

### Circuit questions are often differential equation questions

The field equations tell us why capacitors and inductors behave as they do. Once we have a lumped-circuit model, we can often express the whole system using just the current, charge and voltage, together with the relevant circuit parameters.

For example, consider a resistor $R$ and an inductor $L$ in series, connected to a constant source $V_0$ at $t=0$. Choose a reference direction for the current. In that direction the resistor has a voltage drop $RI$ and the inductor has a voltage drop $L\,dI/dt$. Kirchhoff's loop equation gives

$$
V_0-RI-L\frac{dI}{dt}=0.
$$

Rearranging,

$$
\frac{dI}{dt}+\frac{R}{L}I=\frac{V_0}{L}.
$$

This is a first-order linear ODE. Multiply both sides by the integrating factor $e^{Rt/L}$:

$$
\frac{d}{dt}(Ie^{Rt/L})=\frac{V_0}{L}e^{Rt/L}.
$$

With $I(0)=0$, integration from $0$ to $t$ gives

$$
\begin{aligned}
I(t)e^{Rt/L}&=\frac{V_0}{L}\int_0^t e^{Rt'/L}\,dt'\\
&=\frac{V_0}{R}(e^{Rt/L}-1).
\end{aligned}
$$

Hence

$$
\boxed{I(t)=\frac{V_0}{R}(1-e^{-t/\tau}),\qquad \tau=\frac{L}{R}.}
$$

The time constant $\tau$ is measured in seconds. At the moment the switch is closed, $I=0$ but $dI/dt=V_0/L$. The inductor initially takes the whole voltage drop. After a long time the current approaches $V_0/R$ and $dI/dt\to0$. A larger inductance makes the current rise more slowly, but it does not change the final current in this ideal DC circuit.

Related example: [OpenStax §14.4 — RL Circuits](https://openstax.org/books/university-physics-volume-2/pages/14-4-rl-circuits).

For a series RLC circuit, write $I=\dot Q$, with $Q$ the signed charge on the chosen capacitor plate. Using the three voltage drops gives

$$
\boxed{L\ddot Q+R\dot Q+\frac{1}{C}Q=V(t).}
$$

This is exactly the same mathematical form as a driven mechanical oscillator:

$$
m\ddot x+b\dot x+kx=F(t).
$$

| Mechanical oscillator | RLC circuit |
| --- | --- |
| Position $x$ | Charge $Q$ |
| Velocity $\dot x$ | Current $I=\dot Q$ |
| Mass $m$ | Inductance $L$ |
| Damping $b$ | Resistance $R$ |
| Spring constant $k$ | Inverse capacitance $1/C$ |
| Driving force $F(t)$ | Applied voltage $V(t)$ |

The analogy is useful because we do not have to relearn the mathematics. Homogeneous and particular solutions, initial conditions, resonance, Fourier methods and Green functions all work in the same way. For example, with $R=0$ and no driving voltage, the natural angular frequency is $\omega_0=1/\sqrt{LC}$, just as the mechanical oscillator has $\omega_0=\sqrt{k/m}$.

The energy relation also follows the analogy:

$$
U=\frac12 LI^2+\frac{Q^2}{2C}.
$$

Taking its time derivative and using the circuit equation,

$$
\begin{aligned}
\frac{dU}{dt}&=LI\dot I+\frac{Q}{C}\dot Q\\
&=I\left(L\dot I+\frac{Q}{C}\right)\\
&=V(t)I-RI^2.
\end{aligned}
$$

The source supplies power $VI$, the resistor dissipates power $RI^2$, and the rest changes the energy in the capacitor and inductor. In an ideal undriven LC circuit, the total energy is constant.

## 14.11 A quick guide to choosing a method

The table below is not meant to be another set of formulas to memorise. It is a way of deciding where to start. The assumptions matter: Coulomb's law in the form used here is electrostatic, and the simple form of Ampère's law is magnetostatic. For genuinely time-dependent electromagnetic fields, use the full Maxwell equations.

| If the question asks for ... | Start with ... |
| --- | --- |
| Electric field from a known charge distribution | Check symmetry first; use Gauss if possible, otherwise Coulomb or potential |
| Electric potential from a known charge distribution | Integrate $dq/(4\pi\varepsilon_0 R)$, with a suitable reference |
| Electrostatic field from a known potential | $\mathbf E=-\nabla V$ |
| Total charge density from an electric field | $\rho=\varepsilon_0\nabla\cdot\mathbf E$ |
| Magnetic field from a steady current | Check symmetry; use Ampère if possible, otherwise Biot–Savart |
| Steady total current density from a magnetic field | $\mathbf J=(\nabla\times\mathbf B)/\mu_0$ |
| Field near a conductor with unknown surface charge | Poisson/Laplace and boundary conditions |
| Capacitance | $Q\to E\to V\to C$ |
| Resistance of a material or structure | Constitutive relation and current/voltage integrals |
| Self-inductance or mutual inductance | $I\to B\to\Phi_B\to\lambda$, then divide by the source current |
| Induced emf | $\mathcal E=-d\lambda/dt$, including changes of field or geometry |
| Induced electric field | Faraday's law and symmetry (or the full field equations) |
| Force on a charge | Lorentz force |
| Force on a wire | $I\int d\mathbf l\times\mathbf B$, using the relevant external field |
| Electric or magnetic dipole torque | $\boldsymbol\tau=\mathbf p\times\mathbf E$ or $\mathbf m\times\mathbf B$ |
| Force between circuit components | Direct field force or an energy method with the correct constraints |
| Fields in materials | Constitutive relations, $\mathbf D$ and $\mathbf H$, boundary conditions |
| Transient circuit behaviour | Kirchhoff's laws and an ODE with initial conditions |
| Electromagnetic wave propagation | Maxwell's equations, wave equations and boundary conditions |

Here $\mathbf p$ (C m) is the electric dipole moment and $\mathbf m$ (A m²) is the magnetic dipole moment. The simple torque expressions refer to dipoles in uniform fields, or sufficiently small dipoles in fields that vary slowly across them.

### A checklist for a new question

1. Write down what is given and what is unknown. Is it a field problem, a boundary problem, a force/energy problem, or a time-dependent problem?
2. Choose a coordinate system. Distinguish the source point from the observation point. Draw the geometry if it helps.
3. Use symmetry to decide the possible direction of the field and the variables it can depend on. Check that the entire system has the symmetry being assumed.
4. Decide which law gives the shortest route. Can Gauss or Ampère replace a direct integral? Would it be easier to calculate a potential first?
5. Divide the problem into regions if necessary. Make clear what is held constant and which boundary or initial conditions apply.
6. Write the correct source element, distance, unit vectors, integration limits and normal or tangent direction.
7. Carry out the remaining integration or differential equation. Convert the result to the quantity actually asked for.
8. Check the units, signs, limiting cases and boundary behaviour.

The order is not rigid. Sometimes the geometry immediately tells us which law to use; sometimes we have to try two different methods before deciding. The important thing is to make these decisions before spending time on a long calculation.

## 14.12 Further reading and practice

The examples in this chapter are intended to illustrate the method, not to form a separate problem set. The non-uniform sphere and wire examples are variations on standard textbook problems; other calculations have been rewritten to fit the approach used in these notes.

- [MIT 8.02, *Physics II: Electricity and Magnetism* — Problem Solving](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/problem-solving/). A useful collection of topic-based problems covering charges, currents, fields and circuits. Particularly good for practising how to set up a problem before calculating.
- [OpenStax, *University Physics Volume 2*](https://openstax.org/books/university-physics-volume-2/pages/1-introduction). Chapters 5–14 provide accessible worked examples on electrostatics, current, magnetostatics, induction and inductance.
- [David Tong, *Lectures on Electromagnetism*, University of Cambridge](https://www.damtp.cam.ac.uk/user/tong/justem.html). A good next step for understanding Maxwell's equations, potentials, waves and the more theoretical side of electromagnetism. The course also includes example sheets.
- [MIT 6.013, *Electromagnetics and Applications* — Lecture Notes](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-fall-2005/pages/lecture-notes/). Useful when working on boundary-value problems, fields in materials and electromagnetic waves.

For revision, I would go through the topics in roughly this order:

| Stage | What to revisit | Main point |
| --- | --- | --- |
| 1 | Line charges, rings and discs | Source coordinates, distance, direction and integration elements |
| 2 | Spheres, infinite cylinders and planes | Symmetry, Gauss's law and separate regions |
| 3 | Potentials, conductors and capacitors | Scalar methods and boundary conditions |
| 4 | Wires, current loops and solenoids | Biot–Savart, Ampère and magnetic geometry |
| 5 | Dielectrics, magnetisation, self- and mutual inductance | Material laws and response coefficients |
| 6 | Induction, moving conductors and RL/RLC circuits | Flux changes, signs and time evolution |
| 7 | Mixed problems | Choosing a method independently and checking the result |

## 14.13 The bigger picture

A lot of electromagnetism comes back to a small number of mathematical ideas:

| Idea | Where it appears |
| --- | --- |
| Superposition | Adding the fields of many prescribed sources |
| Symmetry | Reducing the number of field components or independent variables |
| Vector calculus | Gradient, divergence, curl, flux and circulation |
| Boundary-value problems | Conductors, interfaces, potentials and uniqueness |
| Response theory | Green functions, capacitance, inductance and material response |

For instance, Coulomb's law is closely related to the Green function for Poisson's equation. In free space, with the potential vanishing at infinity,

$$
-\nabla^2V=\frac{\rho}{\varepsilon_0},\qquad
-\nabla^2G(\mathbf r,\mathbf r')=\delta^{(3)}(\mathbf r-\mathbf r').
$$

The Green function is

$$
G(\mathbf r,\mathbf r')=\frac{1}{4\pi|\mathbf r-\mathbf r'|}.
$$

Superposing the responses to individual source points gives

$$
V(\mathbf r)=\frac{1}{\varepsilon_0}\int G(\mathbf r,\mathbf r')\rho(\mathbf r')\,dV'.
$$

This is the usual electrostatic potential integral. It is also the same idea we use when solving a driven harmonic oscillator with Green functions: find the response to a unit source, then add up the responses to the actual source distribution. Here the integration is over space rather than time. Different boundary conditions generally require a different Green function.

Ultimately, the electromagnetic fields obey Maxwell's equations. Written using the total charge and current densities, they are

$$
\boxed{\begin{aligned}
\nabla\cdot\mathbf E&=\frac{\rho}{\varepsilon_0},\\
\nabla\cdot\mathbf B&=0,\\
\nabla\times\mathbf E&=-\frac{\partial\mathbf B}{\partial t},\\
\nabla\times\mathbf B&=\mu_0\mathbf J+\mu_0\varepsilon_0\frac{\partial\mathbf E}{\partial t}.
\end{aligned}}
$$

To see how the approach changes for waves, take a source-free region in vacuum. Taking the curl of Faraday's law gives

$$
\nabla\times(\nabla\times\mathbf E)=-\frac{\partial}{\partial t}(\nabla\times\mathbf B)
=-\mu_0\varepsilon_0\frac{\partial^2\mathbf E}{\partial t^2}.
$$

Using $\nabla\times(\nabla\times\mathbf E)=\nabla(\nabla\cdot\mathbf E)-\nabla^2\mathbf E$ and $\nabla\cdot\mathbf E=0$, we obtain

$$
\nabla^2\mathbf E-\mu_0\varepsilon_0\frac{\partial^2\mathbf E}{\partial t^2}=0.
$$

The problem is now a wave equation, with solutions determined by boundary and initial conditions. The familiar integral methods are therefore not the only way of solving electromagnetic problems. For a prescribed static source, integration may be the easiest approach. When the source or field is itself unknown, or when we are dealing with wave propagation, differential equations and boundary conditions are often the better starting point.

In the end, the habit I find most useful is to work out what the physics tells us about the answer before trying to calculate it. Determine the geometry, use the symmetry, choose a law and set the constraints. Only then do the mathematics that is still necessary.
