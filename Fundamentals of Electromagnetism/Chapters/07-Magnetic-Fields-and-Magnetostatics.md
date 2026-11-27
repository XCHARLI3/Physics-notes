# Chapter 7 — Magnetic Fields and Magnetostatics

Electric forces act on charges whether or not they move. Experiments by Ørsted and others found a new effect: a current deflects a compass needle, and moving charges experience a velocity-dependent force. This motivates a second field, $\mathbf B$, whose static sources are steady currents.

## 7.1 The magnetic force

A particle of charge $q$ (coulombs) moving with velocity $\mathbf v$ ($\mathrm{m/s}$) in electric and magnetic fields $\mathbf E$ ($\mathrm{V/m}$) and $\mathbf B$ (tesla, $\mathrm T$) experiences the experimentally established **Lorentz force**:

```math
\boxed{\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B)}.
```

The magnetic part is perpendicular to the motion, because $\mathbf v\cdot(\mathbf v\times\mathbf B)=0$. Consequently,

```math
\frac{d}{dt}\left(\tfrac12mv^2\right)=\mathbf F\cdot\mathbf v=q\mathbf E\cdot\mathbf v.
```

A magnetic field alone changes the *direction* of nonrelativistic velocity, not its speed. In the kinetic-energy equation $m$ is particle mass (kilograms) and $v=|\mathbf v|$; $1\,\mathrm T=1\,\mathrm{N/(A\,m)}$.


## 7.2 Motion in uniform fields

Consider a particle of charge $q$ and mass $m$ moving in a uniform magnetic field $\mathbf B$, with no electric field present. Since the magnetic force is always perpendicular to the velocity, it changes the direction of motion but not the speed of the particle.

If $\mathbf v\perp\mathbf B$, the magnetic force acts as the centripetal force, causing the particle to move in a circular orbit:

```math
|q|v_\perp B=\frac{mv_\perp^2}{r}.
```

Rearranging and using $\omega_c=v_\perp/r$, we obtain

```math
\boxed{r=\frac{mv_\perp}{|q|B}},\qquad
\boxed{\omega_c=\frac{|q|B}{m}}.
```

Here $r$ is the radius of the circular orbit (metres), $v_\perp$ is the speed perpendicular to the magnetic field, and $\omega_c$ is the cyclotron angular frequency ($\mathrm{rad/s}$). The sign of $q$ determines the direction of rotation, while the angular frequency is independent of the particle's speed in the nonrelativistic regime.

If the particle also has a velocity component $v_\parallel$ parallel to $\mathbf B$, this component remains unchanged because the magnetic force acts only on the perpendicular component. The combination of circular motion perpendicular to the field and uniform motion along the field produces a helical trajectory. Since each revolution takes a period $T=2\pi/\omega_c$, the distance travelled along the field during one revolution, known as the *pitch*, is

```math
\boxed{h=|v_\parallel|T=\frac{2\pi|v_\parallel|}{\omega_c}}.
```

### Velocity selector

When both electric and magnetic fields are present, the total force on a charged particle is given by the Lorentz force:

```math
\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B).
```

If $\mathbf E\perp\mathbf B$ and the particle travels perpendicular to both fields in the appropriate direction, the electric and magnetic forces oppose each other. The particle passes through without deflection when

```math
\mathbf E+\mathbf v\times\mathbf B=0.
```

Equating the magnitudes of the two forces gives

```math
|q|E=|q|vB,
```

and hence

```math
\boxed{v=\frac{E}{B}}.
```

This is the principle of a *velocity selector*: only particles travelling at the selected speed along the chosen direction experience no net force.

### Hall effect

The Hall effect arises from a similar balance between electric and magnetic forces.

Consider a rectangular conducting slab carrying a current $I$ along the $x$-direction, with a uniform magnetic field $\mathbf B$ along the $z$-direction. The slab has width $w$ along $y$ and thickness $t$ along $z$.

As the charge carriers move through the conductor, the magnetic force deflects them sideways. This causes charge to accumulate on opposite sides of the slab, creating a transverse electric field $\mathbf E_H$, known as the *Hall field*.

As more charge accumulates, the Hall field becomes stronger until the electric force balances the magnetic force:

```math
q(\mathbf E_H+\mathbf v_d\times\mathbf B)=0.
```

Since the drift velocity is perpendicular to the magnetic field, the magnitudes satisfy

```math
|q|E_H=|q|v_dB,
```

giving

```math
E_H=v_dB.
```

The resulting potential difference across the width of the slab is called the *Hall voltage*. Its magnitude is

```math
|V_H|=E_Hw=v_dBw.
```

Using the relation between current and drift speed,

```math
I=n|q|v_dA=n|q|v_dwt,
```

we eliminate $v_d$ to obtain

```math
\boxed{|V_H|=\frac{IB}{n|q|t}}.
```

Here $n$ is the number density of charge carriers ($\mathrm{m^{-3}}$), $v_d$ is their drift speed ($\mathrm{m/s}$), and $V_H$ is the Hall voltage (volts).

For a fixed current direction and magnetic field, the polarity of the Hall voltage reveals whether the dominant charge carriers are positive or negative, while its magnitude can be used to determine their number density in the single-carrier model.

### Mass spectrometer

A mass spectrometer makes use of the dependence of the circular orbit radius on the mass and charge of a particle:

```math
r=\frac{mv}{|q|B}.
```

For particles entering a uniform magnetic field perpendicularly with the same speed, different mass-to-charge ratios produce different orbit radii. Measuring these radii therefore allows the particles to be distinguished according to their mass-to-charge ratios:

```math
\boxed{\frac{m}{|q|}=\frac{Br}{v}}.
```


## 7.3 From Single Carriers to Forces on Wires

Each charge carrier experiences a magnetic force $\mathbf F=q\mathbf v_d\times\mathbf B$. For a wire of cross-sectional area $A$ and carrier number density $n$, a short segment of length $d\ell$ contains $dN=nA\,d\ell$ carriers.

Assuming the magnetic field is approximately uniform across this segment, their forces add to give

```math
d\mathbf F=dN(q\mathbf v_d\times\mathbf B)
=nA\,d\ell(q\mathbf v_d\times\mathbf B).
```

Let $d\boldsymbol\ell=\hat{\mathbf t}\,d\ell$ point along the conventional current, and write $\mathbf v_d=v_\parallel\hat{\mathbf t}$, where $v_\parallel$ is signed. Since $I=nqAv_\parallel$, we obtain

```math
d\mathbf F=nqAv_\parallel\,d\boldsymbol\ell\times\mathbf B
=I\,d\boldsymbol\ell\times\mathbf B.
```

Integrating along the wire,

```math
\boxed{d\mathbf F=I\,d\boldsymbol\ell\times\mathbf B},
\qquad
\boxed{\mathbf F=I\int_Cd\boldsymbol\ell\times\mathbf B}.
```

The result is independent of the sign of the carriers because conventional current already accounts for their direction of motion.

For a closed loop in a **uniform** magnetic field, $\mathbf B$ can be taken outside the integral:

```math
\mathbf F=I\left(\oint_Cd\boldsymbol\ell\right)\times\mathbf B=0,
```

since the total displacement around a closed path is zero. However, forces acting at different positions may still produce a **torque**, even when the net force vanishes.



## 7.4 A Current Loop Is a Magnetic Dipole

Consider a rectangular current loop with side lengths $a$ and $b$, carrying current $I$ in a uniform magnetic field $\mathbf B$. Its area is $A=ab$.

From the force on a current-carrying wire,

```math
d\mathbf F=I\,d\boldsymbol\ell\times\mathbf B,
```

the two opposite sides of length $a$, chosen perpendicular to $\mathbf B$, experience equal and opposite forces of magnitude

```math
F=IaB.
```

Their net force is zero, but they form a couple. If $\theta$ is the angle between the loop's normal and $\mathbf B$, the perpendicular distance between the forces' lines of action is $b\sin\theta$. Hence,

```math
\tau=F(b\sin\theta)
=IabB\sin\theta
=IAB\sin\theta.
```

This motivates the **magnetic dipole moment** $\mathbf m$ (units $\mathrm{A\,m^2}$), defined by

```math
\boxed{\mathbf m=IA\hat{\mathbf n}},
```

where $\hat{\mathbf n}$ is the unit normal determined by the right-hand rule along the conventional current.

The torque can therefore be written in vector form as

```math
\boxed{\boldsymbol\tau=\mathbf m\times\mathbf B}.
```

The torque tends to align $\mathbf m$ with $\mathbf B$, just as an electric field aligns an electric dipole.

To obtain the potential energy, recall that $dU=-dW_{\mathrm{field}}$. Since the magnetic torque tends to **decrease** $\theta$, its work during a small angular displacement $d\theta$ is

```math
dW_{\mathrm{field}}=-mB\sin\theta\,d\theta.
```

Therefore,

```math
dU=mB\sin\theta\,d\theta.
```

Choosing $U=0$ at $\theta=\pi/2$ and integrating,

```math
U(\theta)=\int_{\pi/2}^{\theta}mB\sin\theta'\,d\theta'
=-mB\cos\theta.
```

Thus,

```math
\boxed{U=-\mathbf m\cdot\mathbf B}.
```

The energy is lowest when the magnetic moment is aligned with the field.

In a **nonuniform field**, the forces on opposite sides need not cancel. For a sufficiently small dipole with fixed moment $\mathbf m$, in a current-free region,

```math
\mathbf F=-\nabla U
\quad\Rightarrow\quad
\boxed{\mathbf F\simeq\nabla(\mathbf m\cdot\mathbf B)}.
```

A uniform field can therefore produce torque without net force, while a nonuniform field can also produce a net force. These principles underlie simple electric motors and provide the basis for magnetic matter in Chapter 8.


## 7.5 Currents as Sources of Magnetic Field

Ørsted's compass experiment showed that an electric current produces a magnetic field. Biot and Savart subsequently investigated how this magnetic effect depends on the current and the geometry of the conductor, leading to the **Biot–Savart law** for steady currents.

Consider a small wire element $d\boldsymbol\ell'$ carrying current $I$. Its contribution to the magnetic field at an observation point $\mathbf r$ is

```math
d\mathbf B(\mathbf r)
=\frac{\mu_0 I}{4\pi}
\frac{d\boldsymbol\ell'\times(\mathbf r-\mathbf r')}
{|\mathbf r-\mathbf r'|^3}.
```

Here $\mathbf r'$ is the source position, $d\boldsymbol\ell'$ points along the conventional current, and $\mu_0$ is the vacuum permeability ($\mathrm{H/m}$).

Writing $\mathbf R=\mathbf r-\mathbf r'$ and $\hat{\mathbf R}=\mathbf R/R$ gives

```math
d\mathbf B=\frac{\mu_0 I}{4\pi}
\frac{d\boldsymbol\ell'\times\hat{\mathbf R}}{R^2}.
```

The magnitude is proportional to $I\,d\ell'\sin\theta/R^2$, where $\theta$ is the angle between the current element and $\mathbf R$. The cross product gives the direction by the right-hand rule.

By superposition, the total field is obtained by integrating over the entire wire:

```math
\boxed{
\mathbf B(\mathbf r)=\frac{\mu_0 I}{4\pi}
\int_C\frac{d\boldsymbol\ell'\times(\mathbf r-\mathbf r')}
{|\mathbf r-\mathbf r'|^3}
}.
```

For a continuous three-dimensional current distribution, divide the conductor into narrow current tubes. A tube with cross-sectional area $dA$ perpendicular to the current carries $dI=J\,dA$, where $\mathbf J$ is the current density ($\mathrm{A/m^2}$). Since $dV=dA\,d\ell'$, the contribution $I\,d\boldsymbol\ell'$ generalises to $\mathbf J\,dV$.

Therefore,

```math
\boxed{
\mathbf B(\mathbf r)=\frac{\mu_0}{4\pi}
\int_V
\frac{\mathbf J(\mathbf r')\times(\mathbf r-\mathbf r')}
{|\mathbf r-\mathbf r'|^3}\,d^3r'
}.
```

Similarly, for a surface current, replace $\mathbf J\,dV$ with $\mathbf K\,dS$, where $\mathbf K$ is the surface current density ($\mathrm{A/m}$).

The Biot–Savart law applies to **steady currents**. For time-dependent sources, changes in the electromagnetic field propagate at finite speed, requiring a more general treatment.


## 7.6 Symmetry Makes the Integrals Manageable

The Biot–Savart law gives the magnetic field of any steady current distribution. For symmetric geometries, we can simplify the vector integral by identifying which components cancel or reinforce one another.

### 7.6.1 Infinite Straight Wire

Consider an infinitely long wire carrying current $I$ along the positive $z$-axis. We want the magnetic field at a perpendicular distance $r$ from the wire.

Take a source element at height $z'$:

```math
d\boldsymbol\ell'=dz'\,\hat{\mathbf z}.
```

The displacement from the source element to the observation point is

```math
\mathbf R=\mathbf r-\mathbf r'
=r\hat{\mathbf r}-z'\hat{\mathbf z},
\qquad
R=\sqrt{r^2+z'^2}.
```

Using the Biot–Savart law,

```math
d\mathbf B=\frac{\mu_0 I}{4\pi}
\frac{d\boldsymbol\ell'\times\mathbf R}{R^3}.
```

Since $\hat{\mathbf z}\times\hat{\mathbf r}=\hat{\boldsymbol\phi}$,

```math
d\boldsymbol\ell'\times\mathbf R
=r\,dz'\,\hat{\boldsymbol\phi}.
```

Thus every current element contributes in the same azimuthal direction, $\hat{\boldsymbol\phi}$, tangent to a circle around the wire. Integrating along the entire wire,

```math
B_\phi=\frac{\mu_0 I}{4\pi}
\int_{-\infty}^{\infty}
\frac{r\,dz'}{(r^2+z'^2)^{3/2}}.
```

Using

```math
\int\frac{dz'}{(r^2+z'^2)^{3/2}}
=\frac{z'}{r^2\sqrt{r^2+z'^2}},
```

we obtain

```math
B_\phi=\frac{\mu_0 I}{4\pi}
\left[\frac{z'}{r\sqrt{r^2+z'^2}}\right]_{-\infty}^{\infty}.
```

Therefore,

```math
\boxed{\mathbf B=\frac{\mu_0 I}{2\pi r}\hat{\boldsymbol\phi}}.
```

The field circles the wire according to the right-hand rule, and its magnitude decreases as $1/r$.

### 7.6.2 Circular Current Loop

Consider a circular loop of radius $a$ carrying current $I$ in the $xy$-plane. We calculate the magnetic field at height $z$ on its symmetry axis.

For any source element, the distance to the observation point is the same:

```math
R=\sqrt{a^2+z^2}.
```

Let $\phi$ specify the position of a current element around the loop. Then

```math
d\boldsymbol\ell'=a\,d\phi\,\hat{\boldsymbol\phi},
\qquad
\mathbf R=z\hat{\mathbf z}-a\hat{\mathbf r}.
```

Their cross product is

```math
d\boldsymbol\ell'\times\mathbf R
=a\,d\phi\,(z\hat{\mathbf r}+a\hat{\mathbf z}).
```

The radial components cancel between opposite elements, while their axial components add. Therefore, only the $z$-component survives:

```math
dB_z=\frac{\mu_0 I}{4\pi}
\frac{a^2\,d\phi}{(a^2+z^2)^{3/2}}.
```

All elements have the same axial contribution, so integrating around the loop gives

```math
B_z=\frac{\mu_0 I}{4\pi}
\int_0^{2\pi}
\frac{a^2\,d\phi}{(a^2+z^2)^{3/2}}.
```

Hence,

```math
\boxed{B_z(z)=\frac{\mu_0 Ia^2}{2(a^2+z^2)^{3/2}}}.
```

The positive direction corresponds to counterclockwise current when viewed from the positive $z$-axis.

At the centre, $z=0$:

```math
\boxed{B(0)=\frac{\mu_0 I}{2a}}.
```

Far from the loop, $|z|\gg a$, we can neglect $a^2$ compared with $z^2$ in the denominator:

```math
(a^2+z^2)^{3/2}\approx |z|^3.
```

Therefore,

```math
B_z\approx\frac{\mu_0 Ia^2}{2|z|^3}.
```

Using the magnetic dipole moment $m=IA=I\pi a^2$ from Section 7.4,

```math
\boxed{B_z\approx\frac{\mu_0 m}{2\pi|z|^3}}.
```

Thus, at sufficiently large distances, the loop behaves as a **magnetic dipole**, with an axial field decreasing as $1/|z|^3$ rather than the $1/r$ dependence of an infinite straight wire.





## 7.7 Ampère's Law

### 7.7.1 Origin and General Derivation

Ørsted's experiment showed that electric currents produce magnetic fields. The Biot–Savart law describes this quantitatively for steady currents, while Ampère's law expresses the same relationship through the **circulation of the magnetic field**.

Starting from the general Biot–Savart law,

```math
\mathbf B(\mathbf r)=\frac{\mu_0}{4\pi}
\int_V\mathbf J(\mathbf r')\times
\frac{\mathbf R}{R^3}\,d^3r',
\qquad \mathbf R=\mathbf r-\mathbf r',
```

where $\mathbf J$ is the current density ($\mathrm{A/m^2}$), take the curl with respect to the observation position $\mathbf r$. Since $\mathbf J(\mathbf r')$ is independent of $\mathbf r$, the vector identity simplifies to

```math
\nabla\times\left(\mathbf J\times\frac{\mathbf R}{R^3}\right)
=
\mathbf J\nabla\cdot\left(\frac{\mathbf R}{R^3}\right)
-(\mathbf J\cdot\nabla)\frac{\mathbf R}{R^3}.
```

We evaluate these two terms separately.

**First term.** Recall the identity

```math
\nabla\cdot\frac{\mathbf R}{R^3}
=4\pi\delta^{(3)}(\mathbf R).
```

The divergence is zero everywhere except at the source, but the flux through any sphere surrounding it is $4\pi$. The delta function represents this concentrated contribution.

Using its sampling property,

```math
\begin{aligned}
\int_V\mathbf J(\mathbf r')
\nabla\cdot\left(\frac{\mathbf R}{R^3}\right)d^3r'
&=4\pi\int_V\mathbf J(\mathbf r')
\delta^{(3)}(\mathbf r-\mathbf r')\,d^3r'\\
&=4\pi\mathbf J(\mathbf r).
\end{aligned}
```

**Second term.** Since $\mathbf R=\mathbf r-\mathbf r'$, differentiation with respect to the source position reverses the sign:

```math
\nabla\left(\frac{\mathbf R}{R^3}\right)
=-\nabla'\left(\frac{\mathbf R}{R^3}\right).
```

Let $\mathbf K=\mathbf R/R^3$. Applying the product rule componentwise gives

```math
(\mathbf J\cdot\nabla')\mathbf K
=\nabla'\cdot(\mathbf K\otimes\mathbf J)
-\mathbf K(\nabla'\cdot\mathbf J).
```

Here $\otimes$ denotes the **dyadic (outer) product**, a second-order tensor with components $(\mathbf K\otimes\mathbf J)_{ij}=K_iJ_j$. Its divergence is defined by contraction over the second index:

```math
\big[\nabla'\cdot(\mathbf K\otimes\mathbf J)\big]_i
=\sum_{j=1}^{3}\frac{\partial(K_iJ_j)}{\partial r'_j}
=\sum_{j=1}^{3}J_j\frac{\partial K_i}{\partial r'_j}
+K_i\sum_{j=1}^{3}\frac{\partial J_j}{\partial r'_j}.
```

The first sum is $[(\mathbf J\cdot\nabla')\mathbf K]_i$, while the second is $K_i(\nabla'\cdot\mathbf J)$, which explains the identity without assuming any special current geometry. Integrating over the source volume and applying the divergence theorem gives

```math
\begin{aligned}
\int_V(\mathbf J\cdot\nabla)\mathbf K\,d^3r'
&=-\int_V(\mathbf J\cdot\nabla')\mathbf K\,d^3r'\\
&=-\oint_{\partial V}\mathbf K
(\mathbf J\cdot d\mathbf S')
+\int_V\mathbf K(\nabla'\cdot\mathbf J)\,d^3r'.
\end{aligned}
```

For localised steady currents, the boundary term vanishes when the integration surface lies outside the current distribution. Charge conservation also gives

```math
\frac{\partial\rho}{\partial t}
+\nabla'\cdot\mathbf J=0
\quad\Rightarrow\quad
\nabla'\cdot\mathbf J=0.
```

Therefore, the second term vanishes, leaving

```math
\nabla\times\mathbf B
=\frac{\mu_0}{4\pi}(4\pi\mathbf J).
```

Thus, the **differential form of Ampère's law** is

```math
\boxed{\nabla\times\mathbf B=\mu_0\mathbf J}
\qquad\text{(magnetostatics)}.
```

Stokes' theorem converts this local relation into a closed-path integral:

```math
\begin{aligned}
\oint_C\mathbf B\cdot d\boldsymbol\ell
&=\int_S(\nabla\times\mathbf B)\cdot d\mathbf S\\
&=\mu_0\int_S\mathbf J\cdot d\mathbf S.
\end{aligned}
```

Since the last integral is the enclosed current,

```math
\boxed{\oint_C\mathbf B\cdot d\boldsymbol\ell=\mu_0I_{\mathrm{enc}}}.
```

The positive current direction is determined by the right-hand rule relative to the chosen loop orientation.

Like Gauss's law, Ampère's law is general for steady currents, but it simplifies field calculations only when symmetry makes the circulation easy to evaluate.

The vector-calculus machinery in this derivation goes beyond what is normally required in introductory notes; it is included to preserve a **continuous logical connection** from the Biot–Savart law to Ampère's law. A shorter general route introduces the **magnetic vector potential** $\mathbf B=\nabla\times\mathbf A$: in Coulomb gauge, $\nabla\cdot\mathbf A=0$, its Poisson equation $\nabla^2\mathbf A=-\mu_0\mathbf J$ and the curl-of-a-curl identity immediately give $\nabla\times\mathbf B=\mu_0\mathbf J$. The vector potential is introduced in Section 7.8.

### 7.7.2 Long Solenoid

Consider a long, closely wound solenoid carrying current $I$, with $n$ turns per unit length ($\mathrm{m^{-1}}$).

An ideal infinitely long solenoid can be treated as a cylindrical surface current. Its symmetry gives an axial field $\mathbf B=B_z(r)\hat{\mathbf z}$, independent of position along the axis.

**First, calculate the internal field.**

Choose a rectangular Ampèrian loop with one axial side of length $\ell$ inside the solenoid and the other parallel side at a very large radial distance, where $B\to0$ in the absence of an applied external field.

The two perpendicular sides contribute nothing because $\mathbf B\cdot d\boldsymbol\ell=0$. The distant side also contributes nothing in the limit. Thus,

```math
\oint_C\mathbf B\cdot d\boldsymbol\ell
=B_{\mathrm{inside}}\ell.
```

The enclosed surface is crossed by $n\ell$ turns, each carrying current $I$:

```math
I_{\mathrm{enc}}=n\ell I.
```

Ampère's law therefore gives

```math
B_{\mathrm{inside}}\ell=\mu_0n\ell I
\quad\Rightarrow\quad
\boxed{B_{\mathrm{inside}}=\mu_0nI}.
```

**Now, calculate the external field.**

Choose another rectangle entirely outside the solenoid, with one axial side at a finite radius $r$ and the other at a very large radius where $B\to0$.

No current crosses this surface, so $I_{\mathrm{enc}}=0$. Again, only the two parallel sides can contribute:

```math
B_{\mathrm{outside}}(r)\ell-B_{\infty}\ell=0.
```

Since $B_{\infty}=0$,

```math
\boxed{B_{\mathrm{outside}}(r)=0}.
```

Because $r$ can be any radius outside the solenoid, the field vanishes everywhere outside an **ideal infinite solenoid**.

Notice that Ampère's law alone determines the difference between the fields on the two sides of the loop; the condition $B\to0$ at large radial distance is needed to determine their individual values.

For a **finite** solenoid, the symmetry is imperfect: magnetic field lines bend around its ends, producing a nonzero external field. The ideal result remains a good approximation far from the ends of a sufficiently long solenoid.

### 7.7.3 Toroid

A toroid is a solenoid bent into a ring. For an ideal toroid with $N$ turns, rotational symmetry makes the field circular around its central axis.

Choose a circular Ampèrian path of radius $r$ within the winding region. The enclosed current is $NI$, so

```math
B(r)(2\pi r)=\mu_0NI.
```

Hence,

```math
\boxed{B(r)\simeq\frac{\mu_0NI}{2\pi r}}.
```

The field decreases with radius and is negligible outside an ideal closely wound toroid.

### 7.7.4 Force Between Parallel Currents

Two long parallel wires carry currents $I_1$ and $I_2$ and are separated by distance $d$.

The first wire produces a field at the second:

```math
B_1=\frac{\mu_0I_1}{2\pi d}.
```

From the magnetic force on a wire, $F=I_2LB_1$ for a length $L$, since the wire is perpendicular to the field. Thus,

```math
\boxed{\frac{F}{L}=\frac{\mu_0|I_1I_2|}{2\pi d}}.
```

The right-hand rule shows that **parallel currents attract, while opposite currents repel**.

### 7.7.5 Infinite Current Sheet

Consider an infinite sheet carrying uniform surface current density $\mathbf K$ ($\mathrm{A/m}$). Symmetry gives equal magnetic-field magnitudes on both sides, with opposite tangential directions.

Choose a rectangular Ampèrian loop crossing the sheet, with two sides of length $\ell$ parallel to the field. Both contribute equally to the circulation, while the perpendicular sides contribute zero.

The enclosed current is $K\ell$, so

```math
2B\ell=\mu_0K\ell.
```

Therefore,

```math
\boxed{B=\frac{\mu_0K}{2}}.
```

The two fields have opposite directions, determined by the right-hand rule.

These examples illustrate the main advantage of Ampère's law: **symmetry can replace a complicated Biot–Savart integral with a simple relation between magnetic circulation and enclosed current.**



## 7.8 No Magnetic Monopoles; the Vector Potential

Unlike electric field lines, magnetic field lines have no observed isolated beginning or end. Experimentally, the net magnetic flux through any closed surface is zero:

```math
\boxed{\oint_{\partial V}\mathbf B\cdot d\mathbf S=0}.
```

Using the divergence theorem,

```math
\oint_{\partial V}\mathbf B\cdot d\mathbf S
=\int_V(\nabla\cdot\mathbf B)\,dV=0.
```

Since this holds for any volume,

```math
\boxed{\nabla\cdot\mathbf B=0}.
```

Recall the vector identity $\nabla\cdot(\nabla\times\mathbf A)=0$: **the divergence of any curl is zero**. This motivates expressing the magnetic field as the curl of a vector potential $\mathbf A$ (units $\mathrm{T\,m}=\mathrm{Wb/m}$):

```math
\boxed{\mathbf B=\nabla\times\mathbf A}.
```

A divergence-free field can locally be written in this form. To construct $\mathbf A$ explicitly, recall the Biot–Savart law and use

```math
\nabla\left(\frac1R\right)=-\frac{\mathbf R}{R^3},
\qquad \mathbf R=\mathbf r-\mathbf r'.
```

Since $\mathbf J(\mathbf r')$ is independent of the observation position $\mathbf r$,

```math
\nabla\times\left(\frac{\mathbf J(\mathbf r')}{R}\right)
=\nabla\left(\frac1R\right)\times\mathbf J(\mathbf r')
=\frac{\mathbf J(\mathbf r')\times\mathbf R}{R^3}.
```

Comparing this with the Biot–Savart law, one convenient choice for steady localised currents is

```math
\boxed{
\mathbf A(\mathbf r)=\frac{\mu_0}{4\pi}
\int_V\frac{\mathbf J(\mathbf r')}{|\mathbf r-\mathbf r'|}\,d^3r'
},
```

in Coulomb gauge under the usual boundary assumptions.

The vector potential is not unique: adding any gradient $\nabla\chi$ leaves $\mathbf B$ unchanged because $\nabla\times\nabla\chi=0$. This is called **gauge freedom**.

## 7.9 Boundary Conditions and the Static Pair of Theories

At an interface, let $\hat{\mathbf n}$ point from side 1 to side 2.

First, take a very thin Gaussian pillbox crossing the interface. As its height approaches zero, the side contribution vanishes, leaving only its two faces, whose outward normals are opposite:

```math
\oint_{\partial V}\mathbf B\cdot d\mathbf S
=(\mathbf B_2-\mathbf B_1)\cdot\hat{\mathbf n}\,A=0.
```

Therefore,

```math
\boxed{\hat{\mathbf n}\cdot(\mathbf B_2-\mathbf B_1)=0}.
```

**The normal component of $\mathbf B$ is continuous.**

Next, choose a thin rectangular Ampèrian loop crossing a surface current $\mathbf K$ ($\mathrm{A/m}$), with its long sides of length $\ell$ parallel to the interface.

As the loop height approaches zero, the two short sides contribute nothing. If $\hat{\mathbf t}$ is a unit tangent along the upper side, the circulation becomes

```math
\oint_C\mathbf B\cdot d\boldsymbol\ell
=(\mathbf B_2-\mathbf B_1)\cdot\hat{\mathbf t}\,\ell.
```

The enclosed current is the surface current crossing the loop's spanning surface:

```math
I_{\mathrm{enc}}
=\mathbf K\cdot(\hat{\mathbf n}\times\hat{\mathbf t})\,\ell.
```

Applying Ampère's law and cancelling $\ell$ gives

```math
(\mathbf B_2-\mathbf B_1)\cdot\hat{\mathbf t}
=\mu_0\mathbf K\cdot(\hat{\mathbf n}\times\hat{\mathbf t}).
```

Since this holds for any tangent direction,

```math
\boxed{\hat{\mathbf n}\times(\mathbf B_2-\mathbf B_1)=\mu_0\mathbf K}
\qquad\text{(total surface current in vacuum)}.
```

**The tangential component of $\mathbf B$ changes across a surface current.**

We now have parallel static theories: electrostatics uses charge density as a divergence source and has $\nabla\times\mathbf E=0$; magnetostatics uses steady current density as a curl source and has $\nabla\cdot\mathbf B=0$. Time-dependent fields will couple the two in Chapters 9–11.



---
**Reference.** R. Shankar, *Fundamentals of Physics II: Electromagnetism, Optics, and Quantum Mechanics*, Chapters 8–9 and §§10.1–10.2; David Halliday, Robert Resnick and Jearl Walker, *Fundamentals of Physics*, 12th ed., Chapters 28–29 and 32 (applications); David J. Griffiths, *Introduction to Electrodynamics*, 5th ed., Chapter 5.
