# Chapter 1: Electric Charge and Fields
## Introduction
We begin our study with electrostatics, where charge distributions are independent of time. Starting from the fundamental properties of electric charge, we introduce the electric field as an alternative to describing interactions directly between particles.
## 1.1 Properties of Electric Charge
### 1.1.1 Electric Charge and Electric Interactions
Many experiments can reveal the existance of a new force. For instance, a comb will attract bits of paper after being run through your hair, and will not attract the paper after being dipped in water and removed. Clearly, the force between the comb and paper is not the gravitational force, since gravity doesn't care whether the object is run through hair or not.

Now, let us consider at a qualitative level by considering two situations:
a plastic rod is rubbed with fur and a glass rod is rubbed with silk. By bringing two rods together, we can see:    
- two rubbed glass rods repel each other;
- two rubbed plastic rods repel each other;
- a rubbed plastic rod and a glass rod attract each other.

When different materials are rubbed and brought close to the two rods, 3 possible outcomes are observed: attraction, repulsion, or no detectable interaction. By systematically testing pairs of objects under controlled condtions, we find those interactions can be classified into 2 distinct groups: 
- objects within the same group repel one another,
- while objects belonging to different groups attract one another. 

These observations suggest the existance of two distinct types of electric charge, the underlying physical property the two groups possess, named by the American scientist and statesman Benjamin Franklin as positive and negative charge.

It is helpful to think about it in microscopic view that everything is made of atoms. The atom has a nucleus consisting of protons and neutrons. Electrons, some very light particles, are surrounding the nucleus. Two protons will repel each other, as will two electrons, while the proton and electron will attract each other. A neutron will do nothing with another neutron, proton or electron. By convention, the proton has positive charge and electron has negative charge. Like charges repel and unlike charges attract. A system made of an equal amount of positive and negative charges will appear neutral, at least from a distance when internal structure can be negligible.

### 1.1.2 Quantisation of Charge
Now, we will consider 2 fundamental properties of charge: it's quantized and conserved.  We now talk about the first property firstly. "Quantized" means the electrical charge does not take a continuum of possible values, all the charges are integral multiples of a basic unit, $e=1.6 \cdot 10^{-19} C$. (Quarks are exception with quantized charge as a fraction of e.)  This was found by Millikan through oil-drop experiment. (In the experiment,tiny charged oil droplets are introduced between two parrallel metal plates by balancing the electric force against gravity. Millikan found that the charges of numerous droplets were always integer multiples of fundamental charge e.)

### 1.1.3 Conservation of Charge
The hypothesis of conservation of charge, first put forward by Benjamin Franklin, has stood up under close examination, both for large-scale charged bodies and for atoms, nuclei, and elementary particles. No exceptions have ever been found. Thus, we add electric charge to our list of quantities, including energy and both linear momentum and angular momentum, that obey a conservation law. Importantly, the conservation is local, hence, the charge doesn't just disappear at one place and reappear somewhere else. It just moves around. Otherwise, if the charge disappears in one part of the world and reappears instantaneously in anthoer, without following an interpolating trajectory, such situation cannot survive relativity.

## 1.2 Coulomb's Law
### 1.2.1 What is Coulomb's Law
Now we shall learn about a quantitative description of charges : *Coulomb's Law*. (*Charles-Augustin de Coulomb*'s experiments in 1785 led him to it.) 

Coulomb's Law says the force between two charges $q_1$ and $q_2$, located at points $\vec{r_1}$ and $\vec{r_2}$, is 
$$ \vec{F_{21}}=-\vec{F_{12}}= \frac{q_1 q_2}{4 \pi \varepsilon_0 {r_{12}}^2} \vec{e_{12}} $$
where $r_{12}= |{\vec{r_2}-\vec{r_1}}|$ and $\vec{e_{12}}=\frac{\vec{r_2}-\vec{r_1}}{|{\vec{r_2}-\vec{r_1}}|}$ is a unit vector from $r_1$ to $r_2$.

In the formula $\vec{F_{21}}(=-\vec{F_{12}})$ is the force on charge 2, due to charge 1.

### 1.2.2 Superposition principle
The electrostatic force must obey the superposition principle of force. Suppose we have n charges near a chosen charge called charge 1; then the net force on charge 1 is given by the vector sum
$$\vec{F}_{1,net}=\vec{F}_{12}+\vec{F}_{13}+\vec{F}_{14}+...+\vec{F}_{1n}.$$

### 1.2.3 Coulomb's law for continuous charge density
Often, we consider problems where charges are continuous.(In real world, everything is discrete, but at macroscopic scale, the charge will be looked like continuous.) To solve the variation in such situation: we replace sums by integrals.

Consider a circular wire of radius $R$ with $\lambda$ coulombs per meter, lying in the xy-plane with its centre at the origin. If I want to find the electric force which acts on a test point charge $q$ located at a height z on the z-axis. By dividing the loop into tiny segments of length $dl$, each segment can be treated as a point charge $\lambda dl$. It exerts a force $d\vec{F}$ of magnitude
$$|d\vec{F}|=\frac{q\cdot dl}{d\pi\varepsilon_0(R^2+Z^2)}.$$
$$|d\vec{F}|=\frac{q\cdot \lambda dl}{4\pi\varepsilon_0(R^2+Z^2)}.$$
We only need to keep the vertical part, since the horizontal part will be canceled by the segment at the diametrically opposite point. The total vertical force has a magnitude given by integration:
$$F_z=\int{dF_z}=\int{\frac{q\cdot\lambda dl}{4\pi\varepsilon_0(R^2+z^2)}\times\frac{z}{\sqrt{R^2+z^2}}}$$
$$=\frac{q\cdot\lambda\cdot2\pi\cdot Rz}{4\pi\varepsilon_0 (R^2+z^2)^\frac{3}{2}}.$$
