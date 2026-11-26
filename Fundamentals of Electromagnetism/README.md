# Fundamentals of Electromagnetism

**— From Electric Charge to Maxwell's Equations**

> A personal collection of physics notes, organised from my own perspective to bridge gaps in textbook explanations, explore the origins and motivations behind concepts, and develop understanding and intuition through coherent reasoning without pursuing mathematical rigour for its own sake.

These are **concise explanatory notes**, not a replacement for textbooks. The goal is to keep the steps that establish *why* an equation is written and *when* it may be used, while omitting lengthy algebra that adds no conceptual insight. A derivation is never shortened by silently changing assumptions. Examples appear only when they illuminate a principle; there are no exercises.

## Contents

- [Chapters](#chapters)
- [Editorial approach](#editorial-approach)
- [Authorship and AI assistance](#authorship-and-ai-assistance)
- [References](#references)
- [Figures: assumptions and precision](#figures-assumptions-and-precision)
- [Symbols and units](#symbols-and-units)
- [Review and reproducibility](#review-and-reproducibility)

## Chapters

- **Chapter 1 — Electric Charge and Fields**: [`01-Electric-Charge-and-Fields.md`](chapters/01-Electric-Charge-and-Fields.md)
- **Chapter 2 — Gauss's Law**: [`02-Gauss-Law.md`](chapters/02-Gauss-Law.md)
- **Chapter 3 — Electric Potential and Energy**: [`03-Electric-Potential-and-Energy.md`](chapters/03-Electric-Potential-and-Energy.md)
- **Chapter 4 — Conductors and Capacitance**: [`04-Conductors-and-Capacitance.md`](chapters/04-Conductors-and-Capacitance.md)
- **Chapter 5 — Dielectrics and Polarisation**: [`05-Dielectrics-and-Polarisation.md`](chapters/05-Dielectrics-and-Polarisation.md)
- **Chapter 6 — Electric Currents and DC Circuits**: [`06-Electric-Currents-and-DC-Circuits.md`](chapters/06-Electric-Currents-and-DC-Circuits.md)
- **Chapter 7 — Magnetic Fields and Magnetostatics**: [`07-Magnetic-Fields-and-Magnetostatics.md`](chapters/07-Magnetic-Fields-and-Magnetostatics.md)
- **Chapter 8 — Magnetisation and Magnetic Materials**: [`08-Magnetisation-and-Magnetic-Materials.md`](chapters/08-Magnetisation-and-Magnetic-Materials.md)
- **Chapter 9 — Electromagnetic Induction and Inductance**: [`09-Electromagnetic-Induction-and-Inductance.md`](chapters/09-Electromagnetic-Induction-and-Inductance.md)
- **Chapter 10 — Electromagnetic Oscillations and AC Circuits**: [`10-Electromagnetic-Oscillations-and-AC-Circuits.md`](chapters/10-Electromagnetic-Oscillations-and-AC-Circuits.md)
- **Chapter 11 — Maxwell's Equations and Conservation Laws**: [`11-Maxwells-Equations-and-Conservation-Laws.md`](chapters/11-Maxwells-Equations-and-Conservation-Laws.md)
- **Chapter 12 — Electromagnetic Waves**: [`12-Electromagnetic-Waves.md`](chapters/12-Electromagnetic-Waves.md)
- **Chapter 13 — Electromagnetism and Special Relativity (Optional)**: [`13-Electromagnetism-and-Special-Relativity-Optional.md`](chapters/13-Electromagnetism-and-Special-Relativity-Optional.md)

## Editorial approach

- Coulomb's law and the Lorentz force law begin with experiments. They are not derived from unrelated mathematics.
- The integral → differential form of a field law is explained using flux or circulation and the relevant calculus theorem.
- A material law is not the same thing as a definition or Maxwell equation: this is emphasised in polarisation and magnetisation.
- When a model is approximated (large distance, uniform field, linear response, quasistatic circuit, lossless medium), the small parameter or excluded effect is stated.
- Repeated long algebra, full multipole tensor theory, advanced gauge solutions, complex boundaries and radiation from accelerating charges are left to a later electrodynamics volume.

The full source titles and relevant sections are given at the end of each chapter. Publication details are collected under [References](#references).

## Authorship and AI assistance

These notes are organised around my own understanding, conceptual priorities and explanations of the knowledges. The selection of topics, connections between ideas and overall presentation reflect the approach I want to develop through studies.

As English is not my first language, I have used AI tools to help check for possible errors, refine wording and grammar, and reduce ambiguity. AI assistance has also been involved in preparing outline, diagrams and code. The notes are a personal study guide, not a substitute for a systematic textbook.

## References

### Primary sources

- **R. Shankar**, *Fundamentals of Physics II: Electromagnetism, Optics, and Quantum Mechanics*. Yale University Press, 2016. The main explanation sequence for introductory electric and magnetic fields, circuits, Maxwell's equations and the optional relativity chapter. The 2016 edition informs the structure and explanations of these notes.
- **David Halliday, Robert Resnick and Jearl Walker**, *Fundamentals of Physics*, 12th edition. Wiley. Chapters 21–33 used as the breadth checklist for introductory electricity, magnetism and electromagnetic waves; relativity chapter used only as optional context. Chapter references use the standard edition structure.

### Targeted theoretical supplements

- **David J. Griffiths**, *Introduction to Electrodynamics*, 5th edition. Cambridge University Press. Primarily Chapters 1–9, with selective material from Chapters 10 and 12. Used for the mathematical statements that introductory treatments tend to abbreviate, especially boundary conditions, the uniqueness theorem, bound sources, potentials and field energy.
- **Richard P. Feynman, Robert B. Leighton and Matthew Sands**, *The Feynman Lectures on Physics, Volume II: Mainly Electromagnetism and Matter*. New Millennium Edition. Used selectively for conceptual cross-checks; not an additional required reading route.

### Source and copyright note

These notes present a personal synthesis and interpretation of the cited sources. No scanned textbook illustrations are included. Equations describing general laws are standard mathematical statements; experimental and modelling claims are described rather than quoted at length.

## Figures: assumptions and precision

Figures are located in [`figures/`](figures/) and embedded using relative Markdown paths. The Python scripts used to generate them are under [`tools/`](tools/). **Schematic diagrams should not be interpreted as quantitative field plots unless specifically identified as such.**

All figures are original, editable SVGs, not textbook reproductions. A diagram is used only where geometry, a sign convention or a change of physical interpretation helps. **The figures do not replace the equations and their stated assumptions.**

| Figure | What is represented faithfully | Simplification / limitation |
|---|---|---|
| `01-dipole-torque.svg` | Equal opposite point charges, uniform $\mathbf E$, forces $\pm q\mathbf E$, a dipole vector from $-q$ to $+q$, angle $\theta$ between $\mathbf p$ and $\mathbf E$ | The angular motion is quasistatic; line length is illustrative, not an energy scale |
| `02-gaussian-sphere.svg` | Point charge at the centre of a spherical Gaussian surface; $\mathbf E$ radial and parallel to the outward normal | Constant magnitude at fixed radius uses spherical symmetry; it is **not** true for a general surface or source |
| `04-parallel-plate-capacitor.svg` | $+Q$ and $-Q$ plates, field directed from positive to negative, plate separation $d$ | Wide parallel plate / negligible-fringing approximation; true finite plates have edge fields |
| `05-polarised-slab.svg` | Polarisation $\mathbf P$ to the right; positive effective bound charge on right, negative on left; cancellation in the bulk for uniform $\mathbf P$ | Microscopic charge displacements and boundary layers are highly magnified; the sketch is not an atomistic model |
| `06-rc-charging.svg` | Battery positive at top, conventional charging current through resistor into the **positive** capacitor plate | Ideal lumped circuit; no fringing or lead inductance |
| `08-magnetisation-loops.svg` | Identically oriented small loop currents cancel on shared edges, leaving equivalent boundary circulation; $\mathbf M$ is perpendicular to the page for counterclockwise loops | Discrete rectangular loops are a visual approximation, not real quantum electron orbits |
| `09-motional-emf.svg` | Rightward velocity $\mathbf v$ and field **into** page give $\mathbf v\times\mathbf B$ upward; area of sliding loop increases | Perfect conductive rails/bar, low speed, uniform static field, neglected contact loss |
| `10-rlc-response.svg` | Exact numerical evaluation of analytic undriven series-RLC charge responses $L=C=1$ and $R=0.5,2,3$ with $Q(0)=1,\dot Q(0)=0$ | Normalised units are used, not a chosen physical component scale |
| `11-charging-capacitor.svg` | Illustrates the same Ampèrian boundary admitting different spanning surfaces; charging gap has changing electric flux | **Two panels illustrate two related ideas schematically**. This is not a perspective-accurate depiction of both surfaces simultaneously draped around a physical capacitor |
| `12-plane-wave.svg` | In-phase cosine $E_x/E_0$ and $cB_y/E_0$ against **the same** $kz$ coordinate, at one fixed time, with $+z$ propagation | Separate component plots deliberately avoid a potentially misleading 3D ribbon drawing |


## Symbols and units

Each symbol is explained in context at first use in the relevant chapter. This short index is for searching **after** reading the explanatory passage, not a substitute for it. SI units are assumed.

<details>
<summary>Show the symbols and SI units table</summary>

| Quantity | Symbol | SI unit | Meaning and context |
|---|---|---|---|
| Electric charge | $q$, $Q$ | C | Charge on a particle or a body |
| Elementary charge magnitude | $e$ | C | Positive magnitude of proton/electron charge |
| Force | $\mathbf F$ | N | Force vector; $F$ is its magnitude |
| Position, separation | $\mathbf r$, $\mathbf R$ | m | Position vector or source-to-observation displacement |
| Electric field | $\mathbf E$ | N/C = V/m | Force per unit test charge |
| Vacuum permittivity | $\varepsilon_0$ | F/m | Vacuum electric coefficient |
| Linear charge density | $\lambda$ | C/m | Charge per line length |
| Surface charge density | $\sigma$ | C/m² | Charge per physical surface area |
| Volume charge density | $\rho$ | C/m³ | Charge per volume; subscripts $f,b$ mean free,bound |
| Electric flux | $\Phi_E$ | N·m²/C | Oriented surface integral of electric field |
| Magnetic flux | $\Phi_B$ | Wb = T·m² | Oriented surface integral of magnetic field |
| Electric dipole moment | $\mathbf p$ | C·m | Charge times vector from negative to positive charge |
| Electric potential | $\phi$ | V | Potential energy per test charge |
| Work, energy | $W$, $U$ | J | Work or energy (not the same as potential $\phi$) |
| Electric energy density | $u_E$ | J/m³ | Energy per volume |
| Capacitance | $C$ | F = C/V | Charge per voltage difference; distinguishes roman unit C (coulomb) |
| Electric current | $I$ | A = C/s | Charge crossing a surface per time |
| Current density | $\mathbf J$ | A/m² | Current per oriented area |
| Number density | $n$ | 1/m³ | Particles per volume (unless $n$ means turns/m or refractive index) |
| Drift velocity | $\mathbf v_d$ | m/s | Mean velocity of carriers |
| Electrical conductivity | $\sigma$ | S/m | Appears in current chapter, not surface-charge density |
| Resistivity | $\rho_{\rm res}$ | Ω·m | Inverse of conductivity, not electric charge density |
| Resistance | $R$ | Ω | Voltage divided by current (not radius $R$ in geometric examples) |
| Electromotive force | $\mathcal E$ | V | Non-electrostatic source work per unit charge or induced circuit emf |
| Electric power | $P$ | W | Energy transferred per second (not polarisation vector $\mathbf P$) |
| Magnetic field | $\mathbf B$ | T | Magnetic flux density in Lorentz force |
| Vacuum permeability | $\mu_0$ | H/m | Vacuum magnetic coefficient |
| Magnetic moment | $\mathbf m$ | A·m² = J/T | Current times oriented area or microscopic moment |
| Angular momentum | $\mathbf L$ | kg·m²/s | Particle's orbital angular momentum (not inductance $L$) |
| Polarisation | $\mathbf P$ | C/m² | Electric dipole moment per unit volume |
| Electric displacement | $\mathbf D$ | C/m² | $\varepsilon_0\mathbf E+\mathbf P$ |
| Electric susceptibility | $\chi_e$ | 1 | Linear material coefficient in $\mathbf P=\varepsilon_0\chi_e\mathbf E$ |
| Permittivity | $\varepsilon$ | F/m | Material electric coefficient; $\varepsilon_r=\varepsilon/\varepsilon_0$ |
| Magnetisation | $\mathbf M$ | A/m | Magnetic dipole moment per volume |
| Magnetic field strength | $\mathbf H$ | A/m | $\mathbf B/\mu_0-\mathbf M$ |
| Magnetic susceptibility | $\chi_m$ | 1 | Linear magnetic material coefficient |
| Permeability | $\mu$ | H/m | Material magnetic coefficient |
| Surface current density | $\mathbf K$ | A/m | Current per transverse width, free or bound |
| Inductance, mutual inductance | $L$, $M$ | H = V·s/A | Flux linkage per current |
| Angular frequency | $\omega$ | rad/s | $2\pi$ times frequency in Hz |
| Circuit impedance | $Z$ | Ω | Complex voltage/current amplitude ratio |
| Admittance | $Y$ | S | Reciprocal of impedance |
| Poynting vector | $\mathbf S$ | W/m² | Electromagnetic energy flux |
| Electromagnetic momentum density | $\mathbf g$ | kg/(m²·s) | Field momentum per volume |
| Wavevector | $\mathbf k$ | rad/m | Phase variation per length |
| Refractive index | $n$ | 1 | Phase speed ratio $c/v$, Chapter 12 |
| Wave impedance | $\eta$ | Ω | Ratio $E/H$ in a simple medium |
| Intensity | $I$ | W/m² | Time-averaged energy flux for a wave (not current in circuits) |
| Radiation pressure | $p_{\rm rad}$ | Pa | Normal momentum flux into a surface |
| Lorentz factor | $\gamma$ | 1 | $(1-v^2/c^2)^{-1/2}$, optional relativity chapter |

**Geometry conventions.** $d\mathbf S=\hat{\mathbf n}\,dS$ points outward on closed surfaces. A circulation direction fixes the associated positive normal by the right-hand rule. Source position $\mathbf r'$ and observation position $\mathbf r$ must not be interchanged. Greek $\theta$ is generally an angle in radians unless stated otherwise.

</details>

## Review and reproducibility

The [`tools/`](tools/) directory contains `generate_core_figures.py` and `generate_additional_figures.py` (using NumPy and Matplotlib to generate editable SVG diagrams), as well as `validate_notes.py` (basic automated checks of chapter coverage, Markdown, links and selected equations; SymPy is used for symbolic checks, and CairoSVG for optional SVG render checks).

Run these scripts from the repository root, after installing their dependencies. The figures are also included as ready-to-use SVG files, so readers do **not** need Python to view the notes.

The [QA report](QA-REPORT.md) describes the checks performed for the prepared edition. Automated validation is useful for catching mistakes but does not establish that every physics argument is correct.
