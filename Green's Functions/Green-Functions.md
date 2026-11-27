# Green's Functions: From Impulse Response to Convolution

The idea of a Green's function can be developed from the motion of a damped harmonic oscillator. We first consider the response to a single instantaneous impulse, and then use this response to construct the motion under a continuous external force. This gives a physical interpretation of both convolution and the Green's function method.

## 1. Equation of motion and the differential operator

Consider a mass $m$ attached to a spring of stiffness $k$, with viscous damping coefficient $b$. Let $x(t)$ be its displacement from equilibrium and $F(t)$ the applied external force. Newton's second law gives

$$
m\ddot{x}+b\dot{x}+kx=F(t).
$$

Define the linear differential operator

$$
\mathcal L=m\frac{d^2}{dt^2}+b\frac{d}{dt}+k,
\qquad \mathcal Lx=F(t).
$$

Given a displacement history $x(t)$, applying $\mathcal L$ gives the external force required to produce that motion. Usually, however, we know the force and wish to determine the displacement. In this sense, $F(t)$ is the input to the system and $x(t)$ is its response.

We take $m>0$, $k>0$ and $b\geq0$ to be constant. For now, suppose that the mass is initially at rest at equilibrium and that no external force acts before $t=0$. Non-zero initial conditions will be considered later.

## 2. An instantaneous impulse

Imagine striking the mass with a hammer. The applied force may be large, but it acts over a very short time. The impulse delivered by the external force is defined as

$$
J=\int_{t_1}^{t_2}F(t)\,dt,
$$

which has the same units as momentum, $\mathrm{N\,s}$. To understand why an instantaneous impact can be described by its impulse, we first consider its effect on the equation of motion.

### 2.1 The change in position and momentum

Suppose the external force $F_\varepsilon(t)$ acts only during the interval $[\tau,\tau+\varepsilon]$. Integrating the equation of motion over this interval gives

$$
m\int_\tau^{\tau+\varepsilon}\ddot{x}(t)\,dt
+b\int_\tau^{\tau+\varepsilon}\dot{x}(t)\,dt
+k\int_\tau^{\tau+\varepsilon}x(t)\,dt
=\int_\tau^{\tau+\varepsilon}F_\varepsilon(t)\,dt=J.
$$

The first two integrals can be evaluated directly:

$$
\begin{aligned}
m[\dot{x}(\tau+\varepsilon)-\dot{x}(\tau)]
+b[x(\tau+\varepsilon)-x(\tau)]
+k\int_\tau^{\tau+\varepsilon}x(t)\,dt=J.
\end{aligned}
$$

Now let $\varepsilon\to0^+$ while keeping the external impulse $J$ fixed. For an ordinary impact of finite impulse, the velocity remains bounded during the increasingly short collision, although its acceleration need not remain finite. The change in displacement therefore tends to zero:

$$
x(\tau^+)-x(\tau^-)
=\lim_{\varepsilon\to0^+}\int_\tau^{\tau+\varepsilon}\dot{x}(t)\,dt=0.
$$

Here $\tau^-$ and $\tau^+$ denote the instants immediately before and after the idealised impact. Since the displacement remains bounded, the integrated spring force also tends to zero:

$$
b[x(\tau+\varepsilon)-x(\tau)]\to0,
\qquad
k\int_\tau^{\tau+\varepsilon}x(t)\,dt\to0.
$$

Taking the limit in the integrated equation of motion, we obtain

$$
\boxed{m[\dot{x}(\tau^+)-\dot{x}(\tau^-)]=J,\qquad
x(\tau^+)=x(\tau^-).}
$$

For a force of finite duration, the spring and damping forces also contribute to the change in momentum. In the instantaneous limit, however, their integrated contributions vanish, and the change in momentum is determined entirely by the external impulse $J$. The detailed variation of the applied force during the collision is no longer needed to determine the subsequent motion: the position is unchanged and the velocity increases by $J/m$ (with the sign determined by $J$).

### 2.2 Why represent the force by a Dirac delta?

We now seek an idealised external force that retains the two relevant properties of the impact: it acts only at $t=\tau$, and its integral over time equals the original impulse $J$.

The Dirac delta distribution $\delta(t-\tau)$ is concentrated at $t=\tau$ and is normalised so that

$$
\int_{-\infty}^{\infty}\delta(t-\tau)\,dt=1.
$$

Multiplying it by $J$ gives the required total impulse:

$$
\int_{-\infty}^{\infty}J\delta(t-\tau)\,dt=J.
$$

The idealised instantaneous force is therefore represented by

$$
\boxed{F(t)=J\delta(t-\tau).}
$$

The delta distribution specifies when the impulse is applied, while its coefficient $J$ is determined by the integral of the actual external force, not by the parameters of the oscillator.

To see how this representation arises as a limit, consider a rectangular force pulse of duration $\varepsilon$:

$$
F_\varepsilon(t)=
\begin{cases}
J/\varepsilon, & \tau\leq t<\tau+\varepsilon,\\
0, & \text{otherwise}.
\end{cases}
$$

Its total impulse is

$$
\int_\tau^{\tau+\varepsilon}F_\varepsilon(t)\,dt
=\frac{J}{\varepsilon}\varepsilon=J.
$$

As $\varepsilon\to0^+$, the pulse becomes narrower and its magnitude increases (for non-zero $J$), while the impulse remains unchanged. For any smooth test function $\phi(t)$,

$$
\lim_{\varepsilon\to0^+}
\int_{-\infty}^{\infty}F_\varepsilon(t)\phi(t)\,dt
=J\lim_{\varepsilon\to0^+}\frac{1}{\varepsilon}
\int_\tau^{\tau+\varepsilon}\phi(t)\,dt
=J\phi(\tau).
$$

This is precisely the sifting property of the Dirac delta,

$$
\int_{-\infty}^{\infty}\phi(t)\delta(t-\tau)\,dt=\phi(\tau).
$$

Hence $F_\varepsilon\to J\delta(t-\tau)$ in the sense of distributions, rather than pointwise. For a real force pulse whose duration is short compared with the characteristic times of the oscillator, $J\delta(t-\tau)$ provides an approximation to the input that preserves its impulse and, in the short-duration limit, its effect on the subsequent motion.

## 3. The unit impulse response

Consider a unit impulse applied at $t=0$, represented by $F(t)=\delta(t)$. Denote the response per unit impulse of the initially stationary oscillator by $w(t)$. The notation $F(t)=\delta(t)$ suppresses the unit impulse coefficient; with this normalisation, $w$ satisfies

$$
\mathcal Lw=m\ddot{w}+b\dot{w}+kw=\delta(t),
\qquad w(t)=0\quad(t<0).
$$

From the continuity of displacement and the momentum jump derived above,

$$
w(0^+)=0,
\qquad m\big[\dot{w}(0^+)-\dot{w}(0^-)\big]
=\lim_{\eta\to0^+}\int_{-\eta}^{\eta}\delta(t)\,dt=1.
$$

Since the system is at rest before the impulse, $\dot{w}(0^-)=0$. The conditions immediately after the impulse are therefore

$$
\boxed{w(0^+)=0,\qquad \dot{w}(0^+)=\frac{1}{m}.}
$$

For $t>0$, the impulse has ended and the subsequent motion satisfies the homogeneous equation

$$
m\ddot{w}+b\dot{w}+kw=0.
$$

Define

$$
\gamma=\frac{b}{2m},\qquad \omega_0=\sqrt{\frac{k}{m}},
\qquad \omega_d=\sqrt{\omega_0^2-\gamma^2}.
$$

In the underdamped case ($0<\gamma<\omega_0$), the characteristic roots are $-\gamma\pm i\omega_d$. For $t>0$,

$$
w(t)=e^{-\gamma t}\left(A\cos\omega_dt+B\sin\omega_dt\right).
$$

Applying the conditions at $t=0^+$,

$$
A=0,\qquad -\gamma A+\omega_d B=\frac{1}{m},
\qquad B=\frac{1}{m\omega_d}.
$$

Including the Heaviside step function $H(t)$, which is zero for $t<0$ and one for $t>0$, we can write the response for all times as

$$
\boxed{w(t)=H(t)\frac{e^{-\gamma t}\sin(\omega_dt)}{m\omega_d}.}
$$

This is the unit impulse response. The Heaviside factor expresses causality: there is no response before the impulse is applied. Although the expression above is specific to the underdamped oscillator (and includes the undamped case by setting $\gamma=0$), the construction that follows does not depend on the damping regime.

### 3.1 An impulse applied at an arbitrary time

We have so far considered only a unit impulse at $t=0$. Suppose instead that an impulse of magnitude $J$ is applied at $t=\tau$,

$$
F(t)=J\delta(t-\tau).
$$

There are two changes to the original input. First, since $\mathcal L$ is linear, multiplying the impulse by $J$ multiplies the response by the same factor. Second, since the coefficients of $\mathcal L$ are constant, the motion following the impulse is independent of the absolute time at which it is applied. This property is called time-translation invariance.

The original response $w(t)$ measures the motion after an impulse at $t=0$. If the impulse is instead applied at $t=\tau$, the elapsed time at the observation time $t$ is $t-\tau$. Thus

$$
\boxed{x_J(t)=Jw(t-\tau).}
$$

Indeed, differentiating with respect to $t$ while holding $\tau$ fixed gives

$$
\mathcal L_t[Jw(t-\tau)]=J\delta(t-\tau).
$$

For example, an impulse at $\tau=2\,\mathrm{s}$ observed at $t=5\,\mathrm{s}$ contributes $Jw(3\,\mathrm{s})$ to the displacement. The response is evaluated three seconds after the impulse, rather than at the absolute time of five seconds.

## 4. From a single impulse to a continuous external force

Now suppose that the external force is a continuous function $F(t)$. Rather than solving a new differential equation for this force, we can divide its history into small time intervals and consider the impulse delivered during each interval.

### 4.1 Dividing the force into small impulses

Fix an observation time $t>0$. Divide $[0,t]$ into $N$ intervals of equal width $\Delta\tau=t/N$, with endpoints $s_0=0,s_1,\ldots,s_N=t$. Choose a representative time $\tau_i\in[s_{i-1},s_i]$ in the $i$-th interval.

For sufficiently small $\Delta\tau$, the force varies little within an interval. The impulse delivered during that interval is

$$
\Delta J_i=\int_{s_{i-1}}^{s_i}F(s)\,ds
\approx F(\tau_i)\Delta\tau.
$$

We may approximate this short force pulse by an instantaneous impulse of the same approximate magnitude, applied at $\tau_i$. Writing $s$ for the time variable of the input, the corresponding force is

$$
F(\tau_i)\Delta\tau\,\delta(s-\tau_i).
$$

The factor $\Delta\tau$ is essential: $F(\tau_i)$ is a force, whereas $F(\tau_i)\Delta\tau$ is an impulse. At finite interval widths, replacing a force pulse by a single impulse is only an approximation. The full sequence of impulses recovers the continuous input in the distributional limit.

### 4.2 The contribution of each impulse at the observation time

From Section 3.1, an impulse $\Delta J_i$ applied at $\tau_i$ produces the response $\Delta J_i w(t-\tau_i)$. Its contribution to the displacement at the fixed observation time $t$ is therefore approximately

$$
\boxed{\Delta x_i(t)\approx F(\tau_i)\Delta\tau\,w(t-\tau_i).}
$$

It is worth distinguishing the two times in this expression. The force is evaluated at $\tau_i$, when the impulse is delivered; the response is evaluated at $t-\tau_i$, the time elapsed since that impulse. All contributions are evaluated at the same observation time $t$, even though the impulses occur at different times.

### 4.3 Superposition and the continuous limit

Since $\mathcal L$ is linear, the responses to the individual impulses can be added. More explicitly, if $\mathcal Lx_i=F_i$, then

$$
\mathcal L\left(\sum_i x_i\right)=\sum_i\mathcal Lx_i=\sum_i F_i.
$$

The total response to the approximating sequence of impulses is consequently

$$
x_N(t)=\sum_{i=1}^N F(\tau_i)w(t-\tau_i)\Delta\tau.
$$

For continuous $F$ and the oscillator response considered here, the sum converges to a Riemann integral as $N\to\infty$ and $\Delta\tau\to0$:

$$
\boxed{
\begin{aligned}
x(t)&=\lim_{N\to\infty}\sum_{i=1}^N F(\tau_i)w(t-\tau_i)\Delta\tau\\
&=\int_0^t F(\tau)w(t-\tau)\,d\tau.
\end{aligned}}
$$

The integrand may be understood as the contribution from the force acting during an infinitesimal interval around $\tau$:

$$
\underbrace{F(\tau)\,d\tau}_{\text{infinitesimal impulse}}
\;\underbrace{w(t-\tau)}_{\text{response per unit impulse}}.
$$

The integral adds these contributions over the entire history of the applied force up to time $t$. It is this step that makes the unit impulse response useful: once $w$ is known, the response to a continuous external force follows by integration. A direct verification of the integral is given in Section 5.1.

## 5. Connection to convolution

The convolution of two functions on the real line is defined, when the integral exists, by

$$
(f*g)(t)=\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\,d\tau.
$$

In the present problem, $F(\tau)=0$ for $\tau<0$ and $w(t-\tau)=0$ for $\tau>t$. The first restriction follows from the choice of starting time; the second follows from causality. Therefore, for $t\geq0$,

$$
(F*w)(t)=\int_0^tF(\tau)w(t-\tau)\,d\tau,
\qquad \boxed{x=F*w.}
$$

In this context, convolution is the continuous superposition of shifted impulse responses, each weighted by the impulse delivered at the corresponding time. Substituting the explicit response of the underdamped oscillator gives

$$
x(t)=\frac{1}{m\omega_d}\int_0^t
F(\tau)e^{-\gamma(t-\tau)}\sin[\omega_d(t-\tau)]\,d\tau.
$$

The connection with the Dirac delta can also be seen directly from its sifting property:

$$
F(t)=\int_{-\infty}^{\infty}F(\tau)\delta(t-\tau)\,d\tau.
$$

This identity expresses the force itself as a continuous superposition of instantaneous impulses. In particular, $F*\delta=F$, so the delta distribution is the identity for convolution. Other useful identities, where the convolutions are defined, are

$$
F*w=w*F,\qquad (F_1+F_2)*w=F_1*w+F_2*w,
$$

$$
(F*\delta(\cdot-a))(t)=F(t-a).
$$

### 5.1 Verification in the original equation of motion

Write $x_p(t)=\int_0^tF(\tau)w(t-\tau)\,d\tau$. For continuous $F$, differentiation using Leibniz's rule gives

$$
\begin{aligned}
\dot{x}_p(t)&=F(t)w(0^+)+\int_0^t F(\tau)\dot{w}(t-\tau)\,d\tau\\
&=\int_0^tF(\tau)\dot{w}(t-\tau)\,d\tau,
\end{aligned}
$$

since $w(0^+)=0$. Differentiating again, and using $\dot{w}(0^+)=1/m$, we find

$$
\ddot{x}_p(t)=\frac{F(t)}{m}+\int_0^tF(\tau)\ddot{w}(t-\tau)\,d\tau.
$$

The derivatives of $w$ in these integrals refer to the ordinary derivatives of its positive-time branch. Substitution into the original equation yields

$$
\begin{aligned}
m\ddot{x}_p+b\dot{x}_p+kx_p
&=F(t)+\int_0^t F(\tau)
\underbrace{[m\ddot{w}+b\dot{w}+kw](t-\tau)}_{=0\text{ for }\tau<t}\,d\tau\\
&=F(t).
\end{aligned}
$$

Also, $x_p(0)=\dot{x}_p(0)=0$. The convolution therefore solves the original initial-value problem. Notice that the external force $F(t)$ reappears through the boundary term containing $\dot{w}(0^+)$; the rest of the integral consists of homogeneous responses to earlier impulses.

## 6. From impulse response to Green's function

The preceding construction can be extended to other linear differential equations. Consider

$$
\mathcal L_t x(t)=F(t).
$$

Instead of requiring that a unit impulse be applied at $t=0$, introduce a function $G(t,\tau)$ describing the response at time $t$ to a unit impulse applied at time $\tau$. It satisfies

$$
\boxed{\mathcal L_tG(t,\tau)=\delta(t-\tau).}
$$

This is the defining equation of a Green's function. The subscript $t$ indicates that the operator differentiates with respect to the first argument while the source time $\tau$ is held fixed. The equation must be supplemented by the appropriate initial or boundary conditions. For the causal initial-value problem considered here, we require $G(t,\tau)=0$ for $t<\tau$.

For the constant-coefficient oscillator, time-translation invariance gives

$$
G(t,\tau)=w(t-\tau)
=H(t-\tau)\frac{e^{-\gamma(t-\tau)}\sin[\omega_d(t-\tau)]}{m\omega_d}.
$$

By the same impulse superposition argument, the response with zero initial conditions is

$$
\boxed{x_p(t)=\int_0^t G(t,\tau)F(\tau)\,d\tau.}
$$

We can obtain the same result directly from the defining equation. Extending the causal input and response to the real line and using distributional differentiation,

$$
\begin{aligned}
\mathcal L_t x_p(t)
&=\mathcal L_t\int_{-\infty}^{\infty}G(t,\tau)F(\tau)\,d\tau\\
&=\int_{-\infty}^{\infty}[\mathcal L_tG(t,\tau)]F(\tau)\,d\tau\\
&=\int_{-\infty}^{\infty}\delta(t-\tau)F(\tau)\,d\tau\\
&=F(t).
\end{aligned}
$$

The full-line integral avoids having to assign a value to a delta distribution at a moving integration endpoint. Causality then reduces it to the integral from $0$ to $t$.

### 6.1 Linearity and time-translation invariance

These two properties have different roles. Linearity allows the responses to individual impulses to be added. Time-translation invariance allows all of those responses to be obtained by shifting a single function $w(t)$.

For instance, if the stiffness of the oscillator depends on time, the differential equation can still be linear, but an impulse applied at one time may produce a different subsequent motion from an identical impulse applied at another time. In general,

$$
G(t,\tau)\neq w(t-\tau).
$$

The Green's function representation remains available under suitable conditions, but the integral is no longer necessarily a convolution. Similarly, nonlinear equations do not in general permit the superposition of impulse responses.

### 6.2 Green's function as an inverse operator

Returning to the notation in Section 1, the differential operator maps a response to its corresponding input:

$$
x\xrightarrow{\ \mathcal L\ }F,
\qquad F\xrightarrow{\ \mathcal L^{-1}\ }x.
$$

When the prescribed conditions make the operator invertible, its inverse can be represented by an integral,

$$
(\mathcal L^{-1}F)(t)=\int G(t,\tau)F(\tau)\,d\tau,
$$

with the limits determined by the problem. The Green's function is the integral kernel of this inverse operator. This is analogous to an inverse matrix: each column describes the response to a unit input in one coordinate, and the complete response follows by adding the columns weighted by the corresponding input components.

The impulse interpretation here is specific to a causal time-dependent problem. In a spatial boundary-value problem, the delta distribution represents a point source in space rather than an instantaneous force, but the mathematical construction is similar.

## 7. Non-zero initial conditions

The integral above describes the response due to the external force alone, assuming zero initial displacement and velocity. If $x(0)=x_0$ and $\dot{x}(0)=v_0$, we must also include the motion arising from the initial state:

$$
\boxed{x(t)=x_h(t)+\int_0^tG(t,\tau)F(\tau)\,d\tau,}
$$

where $\mathcal Lx_h=0$, $x_h(0)=x_0$ and $\dot{x}_h(0)=v_0$. For the underdamped oscillator,

$$
x_h(t)=e^{-\gamma t}\left[x_0\cos(\omega_dt)
+\frac{v_0+\gamma x_0}{\omega_d}\sin(\omega_dt)\right].
$$

This is the familiar decomposition into the complementary function and a particular integral. The Green's function selects a particular solution with zero initial conditions, leaving the homogeneous solution to account for the initial state.

## 8. Example: a constant force switched on at $t=0$

Consider an undamped oscillator ($b=0$) initially at rest. Its unit impulse response is

$$
w(t)=H(t)\frac{\sin(\omega_0t)}{m\omega_0},\qquad \omega_0^2=\frac{k}{m}.
$$

For a step force $F(t)=F_0H(t)$, the displacement at $t\geq0$ is

$$
\begin{aligned}
x(t)&=\frac{F_0}{m\omega_0}\int_0^t\sin[\omega_0(t-\tau)]\,d\tau\\
&=\frac{F_0}{m\omega_0^2}[1-\cos(\omega_0t)]\\
&=\boxed{\frac{F_0}{k}[1-\cos(\omega_0t)]}.
\end{aligned}
$$

The result satisfies $x(0)=\dot{x}(0)=0$ and $m\ddot{x}+kx=F_0$ for $t>0$. In the absence of damping, the mass oscillates about the new equilibrium position $F_0/k$ rather than settling at it.

## 9. Connection to Laplace and Fourier transforms

The same impulse response can be obtained using integral transforms. With zero initial conditions, the unilateral Laplace transform of the equation of motion gives

$$
(ms^2+bs+k)X(s)=\widetilde F(s).
$$

Hence

$$
X(s)=\frac{1}{ms^2+bs+k}\widetilde F(s).
$$

Since $x=F*w$, the convolution theorem gives

$$
X(s)=\widetilde F(s)\widetilde w(s),\qquad
\boxed{\widetilde w(s)=\frac{1}{ms^2+bs+k}.}
$$

Completing the square in the denominator,

$$
\widetilde w(s)=\frac{1}{m[(s+\gamma)^2+\omega_d^2]}.
$$

Taking the inverse Laplace transform recovers

$$
w(t)=H(t)\frac{e^{-\gamma t}\sin(\omega_dt)}{m\omega_d}.
$$

For a damped oscillator ($b>0$), the Fourier transform of the causal impulse response also exists. With the convention $\widehat f(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt$, the transformed equation gives, for inputs admitting the relevant transforms,

$$
\widehat x(\omega)=\chi(\omega)\widehat F(\omega),
\qquad \chi(\omega)=\widehat w(\omega)=\frac{1}{k-m\omega^2+ib\omega}.
$$

The function $\chi$ is the frequency response (or susceptibility). Its magnitude and phase describe how the oscillator responds to the individual frequency components of the external force. The undamped case requires a distributional or suitable limiting treatment at resonance.

## 10. Connection to variation of parameters and the Wronskian

The Green's function can also be identified in the method of variation of parameters. Let $y_1,y_2$ be linearly independent solutions of the homogeneous equation and define their Wronskian by

$$
W(t)=y_1(t)\dot y_2(t)-\dot y_1(t)y_2(t).
$$

For the equation $m\ddot{x}+b\dot{x}+kx=F(t)$, variation of parameters gives the particular solution with zero initial conditions

$$
\begin{aligned}
x_p(t)={}&-y_1(t)\int_0^t\frac{y_2(\tau)F(\tau)}{mW(\tau)}\,d\tau\\
&+y_2(t)\int_0^t\frac{y_1(\tau)F(\tau)}{mW(\tau)}\,d\tau.
\end{aligned}
$$

Combining the two integrals,

$$
x_p(t)=\int_0^t
\underbrace{\frac{y_1(\tau)y_2(t)-y_2(\tau)y_1(t)}{mW(\tau)}}_{G(t,\tau)\text{ for }t>\tau}
F(\tau)\,d\tau.
$$

The kernel in the integral is precisely the causal Green's function for $t>\tau$; it is extended by zero for $t<\tau$. For the underdamped oscillator, choose

$$
y_1(t)=e^{-\gamma t}\cos(\omega_dt),\qquad
y_2(t)=e^{-\gamma t}\sin(\omega_dt).
$$

Their Wronskian is $W(t)=\omega_d e^{-2\gamma t}$. Using the sine subtraction identity in the numerator,

$$
\begin{aligned}
G(t,\tau)
&=H(t-\tau)\frac{e^{-\gamma(t+\tau)}\sin[\omega_d(t-\tau)]}{m\omega_d e^{-2\gamma\tau}}\\
&=H(t-\tau)\frac{e^{-\gamma(t-\tau)}\sin[\omega_d(t-\tau)]}{m\omega_d}.
\end{aligned}
$$

This recovers the response originally obtained from the instantaneous impulse. Variation of parameters and the Green's function method therefore give the same particular integral, though they arrive at it from different starting points.

## 11. Further physical checks

### Dimensions

The delta distribution has units $\mathrm{s^{-1}}$, so $J\delta(t-\tau)$ has units of force. The unit impulse response $w$ has units of displacement per impulse,

$$
[w]=\frac{\mathrm m}{\mathrm{N\,s}}=\frac{\mathrm s}{\mathrm{kg}}.
$$

Consequently $F(\tau)w(t-\tau)\,d\tau$ has units of displacement, as required.

### Energy balance

For an ordinary external force, multiplying the equation of motion by $\dot{x}$ gives

$$
\frac{d}{dt}\left(\frac12m\dot{x}^2+\frac12kx^2\right)=F\dot{x}-b\dot{x}^2.
$$

The first term on the right is the power transferred by the external force; the second is the power dissipated by damping. After an isolated impulse, $F=0$ and the mechanical energy decreases when $b>0$, consistent with the decaying envelope of the impulse response.

## References and further reading

1. MIT OpenCourseWare, **18.03SC, “Second Order Unit Impulse Response”**, especially pp. 1–3: [PDF](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/dc47b92b968a26da6b7d3b14036feb51_MIT18_03SCF11_s25_7text.pdf). Covers momentum jumps, continuity of position, and the damped mass–spring model.
2. MIT OpenCourseWare, **18.03 Supplementary Notes, Chapter 19, “Convolution”**, especially §§19.1–19.3: [PDF](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/07ca3d2b4f226e772efb5b8be9703dac_MIT18_03S10_chapter_19.pdf). Develops force packets, impulse superposition, and the convolution integral.
3. MIT OpenCourseWare, **18.03 Notes and Exercises, Chapter I, “Impulse Response and Convolution”**, especially pp. 3–4: [PDF](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/818b2c29b6337e30a2e963d00787373b_MIT18_03S10_i.pdf). Connects convolution with second-order ODE solutions and zero initial conditions.
4. Gilbert Strang, MIT OpenCourseWare, **“Impulse Response and Step Response”**: [video page](https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/resources/impulse-response-and-step-response/).
