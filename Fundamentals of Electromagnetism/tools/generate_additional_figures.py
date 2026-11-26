from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
OUT=Path(__file__).resolve().parents[1]/'figures'; OUT.mkdir(exist_ok=True)
blue='#225c81'; teal='#11775d'; red='#b84e45'; txt='#263746'; grey='#a1aeb9'
plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
# 02. Gaussian sphere: the outward normal of a sphere is radial; symmetry step is visually faithful.
fig,ax=plt.subplots(figsize=(7,3.7)); ax.axis('off'); ax.set_aspect('equal')
center=np.array([0.,0.]);rad=1.1
ax.add_patch(Circle(center,rad,facecolor='#edf3f8',edgecolor=blue,lw=1.7,linestyle='--'))
ax.add_patch(Circle(center,.10,facecolor=red))
ax.text(.11,.16,'$+q$',color=red)
for a in np.linspace(0,2*np.pi,10,endpoint=False):
 u=np.array([np.cos(a),np.sin(a)])
 ax.annotate('',u*1.46,u*.2,arrowprops={'arrowstyle':'->','lw':1.25,'color':teal})
ax.plot([0,rad],[0,0],c=txt,lw=.85,ls='--');ax.text(.5,.09,'$r$',color=txt)
a=.38; loc=rad*np.array([np.cos(a),np.sin(a)]); norm=np.array([np.cos(a),np.sin(a)])
ax.plot([loc[0]-.18*norm[1],loc[0]+.18*norm[1]],[loc[1]+.18*norm[0],loc[1]-.18*norm[0]],c=red,lw=5,solid_capstyle='round')
ax.annotate('',loc+.45*norm,loc,arrowprops={'arrowstyle':'->','lw':2,'color':red})
ax.text(*(loc+.47*norm+np.array([.03,.1])),r'$\hat{\mathbf{n}}=\hat{\mathbf{r}}$',color=red,fontsize=12)
ax.text(-4.55,1.32,'Gaussian sphere',color=txt,fontsize=11)
ax.text(-4.55,.96,'Outward flux',color=txt,fontsize=10)
ax.text(-4.55,.6,r'$\Phi_E=E(r)\,4\pi r^2$',color=txt,fontsize=12)
ax.text(-4.55,.2,'With spherical symmetry',color=txt,fontsize=10)
ax.text(-4.55,-.1,'E is radial and constant',color=txt,fontsize=10)

ax.set_xlim(-4.8,2.15);ax.set_ylim(-1.75,1.8)
fig.savefig(OUT/'02-gaussian-sphere.svg',bbox_inches='tight',facecolor='white');plt.close(fig)
# 04. Capacitor plates long parallel approximation; E direction and +,- sheet charges
fig,ax=plt.subplots(figsize=(7.4,3.45));ax.axis('off');ax.set_aspect('equal')
left,right=1.2,4.6
ax.add_patch(Rectangle((left,.25),.16,2.25,facecolor='#dc7964',edgecolor=red))
ax.add_patch(Rectangle((right,.25),.16,2.25,facecolor='#7aa5c5',edgecolor=blue))
for y in np.linspace(.45,2.26,5):
 ax.text(left-.21,y,'+',color=red,ha='center',va='center',fontsize=14)
 ax.text(right+.36,y,'−',color=blue,ha='center',va='center',fontsize=14)
 ax.annotate('',(right-.12,y),(left+.31,y),arrowprops={'arrowstyle':'->','lw':1.35,'color':teal})
ax.text(3.02,2.68,r'$\mathbf{E}\simeq\sigma\hat{\mathbf{x}}/\varepsilon_0$',color=teal,ha='center',fontsize=13)
ax.annotate('',(right,.03),(left+.16,.03),arrowprops={'arrowstyle':'<->','lw':1.25,'color':txt})
ax.text(2.98,-.2,'$d$',ha='center',fontsize=12,color=txt)
ax.text(.7,1.36,r'$+Q$',fontsize=13,color=red);ax.text(5.0,1.36,r'$-Q$',fontsize=13,color=blue)
ax.text(2.98,-.6,'Ideal wide-plate approximation: fringing neglected',ha='center',fontsize=10,color=txt)
ax.set_xlim(.2,5.8);ax.set_ylim(-.85,3.05)
fig.savefig(OUT/'04-parallel-plate-capacitor.svg',bbox_inches='tight',facecolor='white');plt.close(fig)
# 06. Circuit battery R and capacitor, diagram with clear node/loop and current direction
fig,ax=plt.subplots(figsize=(7.6,3.3));ax.set_aspect('equal');ax.axis('off')
ax.plot([.5,1.4],[2.3,2.3],c=txt,lw=1.8)
zigx=np.linspace(1.4,2.45,9)
zigy=np.array([2.3,2.5,2.1,2.5,2.1,2.5,2.1,2.5,2.3])
ax.plot(zigx,zigy,c=txt,lw=1.7)
ax.plot([2.45,4.1],[2.3,2.3],c=txt,lw=1.8)
ax.plot([4.1,4.1],[2.3,1.62],c=txt,lw=1.8)
ax.plot([3.75,4.45],[1.62,1.62],c=red,lw=2.8)
ax.plot([3.75,4.45],[1.30,1.30],c=blue,lw=2.8)
ax.plot([4.1,4.1],[1.30,.43],c=txt,lw=1.8)
ax.plot([4.1,.5],[.43,.43],c=txt,lw=1.8)
ax.plot([.5,.5],[.43,1.13],c=txt,lw=1.8)
ax.plot([.5,.5],[1.57,2.3],c=txt,lw=1.8)
ax.plot([.28,.72],[1.57,1.57],c=red,lw=3)
ax.plot([.39,.61],[1.13,1.13],c=blue,lw=3)
ax.text(.8,1.64,'+',color=red);ax.text(.8,1.14,'−',color=blue)
ax.text(1.9,2.71,r'$R$',fontsize=13,color=txt,ha='center')
ax.text(4.63,1.46,r'$C$',fontsize=13,color=txt)
ax.text(.01,1.35,r'$\mathcal{E}$',fontsize=13,color=txt,ha='right')
ax.annotate('',(3.52,2.63),(2.85,2.63),arrowprops={'arrowstyle':'->','color':teal,'lw':1.8})
ax.text(3.18,2.84,r'$I(t)$',ha='center',color=teal)
ax.text(2.28,-.03,'The resistor carries the charging current;',fontsize=10,ha='center',color=txt)
ax.text(2.28,-.28,'the capacitor plate charge changes with time.',fontsize=10,ha='center',color=txt)
ax.set_xlim(-.4,5.2);ax.set_ylim(-.65,3.2)
fig.savefig(OUT/'06-rc-charging.svg',bbox_inches='tight',facecolor='white');plt.close(fig)
print('Added diagrams:',[p.name for p in OUT.glob('0*.svg')])
