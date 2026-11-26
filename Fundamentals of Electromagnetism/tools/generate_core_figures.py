import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Polygon, Ellipse
import numpy as np
from pathlib import Path
out=Path(__file__).resolve().parents[1]/'figures'; out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':11,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False})
C1='#225c81'; C2='#b84e45'; C3='#11775d'; BK='#263746'; GR='#a6b1bc'
def save(fig,name):
 fig.savefig(out/name,format='svg',bbox_inches='tight',facecolor='white');plt.close(fig)
def init(w=7,h=3.4):
 fig,ax=plt.subplots(figsize=(w,h)); ax.set_aspect('equal');ax.axis('off');return fig,ax
# dipole at angle theta in E field
fig,ax=init(7,3.8)
theta=np.deg2rad(40); a=1.05; v=np.array([np.cos(theta),np.sin(theta)])
for yy in np.linspace(-1.3,1.3,5): ax.annotate('',(3.25,yy),(-3.25,yy),arrowprops={'arrowstyle':'->','color':'#8bc3df','lw':1.05})
ax.text(-3.3,1.53,'Uniform $\\mathbf{E}$',color=C1)
for sg,col,lab in [(-1,C1,'$-q$'),(1,C2,'$+q$')]:
 p=sg*a*v;ax.add_patch(Circle(p,.15,facecolor=col,zorder=4));ax.text(*(p+np.array([0,.26])),lab,ha='center',va='bottom',color=col)
 # forces + charge to right; - to left
 ax.annotate('',p+np.array([sg*.72,0]),p,arrowprops={'arrowstyle':'->','lw':2,'color':C3})
ax.plot([-a*v[0],a*v[0]],[-a*v[1],a*v[1]],color=BK,lw=1.6,zorder=3)
ax.annotate('',(a*.6*v[0],a*.6*v[1]),(-a*.6*v[0],-a*.6*v[1]),arrowprops={'arrowstyle':'->','color':'#9b62ad','lw':1.5})
ax.text(.1,.65,'$\\mathbf{p}$',color='#9b62ad')
ang=np.linspace(0,theta,55);ax.plot(.48*np.cos(ang),.48*np.sin(ang),color=C2,lw=1.3)
ax.text(.58,.16,'$\\theta$',color=C2)
ax.scatter([0],[0],s=18,c=BK,zorder=5);ax.text(-.18,-.24,'centre',color=BK)
ax.set_xlim(-3.5,3.55);ax.set_ylim(-1.75,1.9)
save(fig,'01-dipole-torque.svg')
# polarised dielectric slab, simplified microscopics + surface sheets
fig,ax=init(7.8,3.5)
ax.add_patch(Rectangle((-.1,-.95),4.5,2.05,facecolor='#e9f4fa',edgecolor=C1,lw=1.5))
for xx in np.linspace(.38,3.95,7):
 for yy in [-.6,0,.6]:
  ax.plot([xx-.13,xx+.13],[yy,yy],c=GR,lw=1)
  ax.add_patch(Circle((xx-.13,yy),.045,color=C1))
  ax.add_patch(Circle((xx+.13,yy),.045,color=C2))
for yy in np.linspace(-.75,.85,7):
 ax.text(-.15,yy,'-',color=C1,fontsize=14,va='center',ha='right')
 ax.text(4.45,yy,'+',color=C2,fontsize=14,va='center',ha='left')
ax.annotate('',(3.55,1.53),(.82,1.53),arrowprops={'arrowstyle':'->','lw':2.2,'color':C3});ax.text(2.2,1.68,'$\\mathbf{P}$',color=C3,ha='center',fontsize=13)
ax.text(-.12,-1.28,r'$\sigma_b=-P$',ha='center',color=C1);ax.text(4.44,-1.28,r'$\sigma_b=+P$',ha='center',color=C2)
ax.annotate('',(5.4,.5),(4.44,.5),arrowprops={'arrowstyle':'->','color':BK,'lw':1.2});ax.text(5.46,.52,'$\\hat{\\mathbf{n}}$',color=BK,va='center')
ax.text(2.15,-1.55,'Cancellation of opposite dipole ends in the bulk',ha='center',fontsize=10,color=BK)
ax.set_xlim(-1.5,6.75);ax.set_ylim(-1.8,2.05)
save(fig,'05-polarised-slab.svg')
# Magnetization current loops, shared edge cancellation
fig,ax=init(6.8,3.7)
for ix in range(3):
 for iy in range(2):
  x=ix*1.05;y=iy*1.0
  ax.add_patch(Rectangle((x,y),1.05,1.0,fill=False,edgecolor=GR,lw=.95))
  # drawn CCW: rightward on bottom, upward on right, leftward on top, downward left
  for xy1,xy2 in [((x+.28,y+.04),(x+.75,y+.04)),((x+1.0,y+.2),(x+1.0,y+.8)),((x+.77,y+.96),(x+.3,y+.96)),((x+.05,y+.78),(x+.05,y+.2))]:
   ax.annotate('',xy2,xy1,arrowprops={'arrowstyle':'->','lw':1.2,'color':C1})
# show boundary current along outer rectangle, represents equivalent
ax.add_patch(Rectangle((-.13,-.13),3.41,2.26,fill=False,edgecolor=C2,lw=1.8))
ax.annotate('',(3.28,1.8),(3.28,.7),arrowprops={'arrowstyle':'->','lw':2.1,'color':C2})
ax.annotate('',(.45,-.13),(1.1,-.13),arrowprops={'arrowstyle':'->','lw':2.1,'color':C2})
ax.text(3.55,1.15,r'$\mathbf{K}_b$',color=C2,fontsize=14)
ax.text(1.55,2.53,'All microscopic loops circulate counterclockwise',ha='center',color=BK,fontsize=10)
ax.text(1.55,-.55,'Shared-edge currents cancel',ha='center',color=BK,fontsize=10)
ax.set_xlim(-.7,5.2);ax.set_ylim(-.8,2.85)
save(fig,'08-magnetisation-loops.svg')
# Motional emf: rails and bar
fig,ax=init(7.5,4)
left=0;right=5.2;top=2.15;bottom=.25;rod=4.0
for y in [top,bottom]:ax.plot([left,right],[y,y],c=BK,lw=2.1)
# left resistor zigzag vertical
zig=np.column_stack([np.array([0,0,-.12,.12,-.12,.12,-.12,.12,0,0]),np.linspace(bottom,top,10)])
ax.plot(zig[:,0],zig[:,1],color=BK,lw=1.5)
ax.plot([rod,rod],[bottom,top],c=C2,lw=4)
ax.annotate('',(rod+1.05,1.5),(rod+.25,1.5),arrowprops={'arrowstyle':'->','lw':2.1,'color':C3});ax.text(rod+.57,1.66,'$v$',color=C3)
ax.annotate('',(rod-.25,1.95),(rod-.25,.45),arrowprops={'arrowstyle':'->','lw':2,'color':C2});ax.text(rod-.6,1.15,r'$q(\mathbf{v}\times\mathbf{B})$',rotation=90,color=C2,ha='center',va='center',fontsize=9)
for x in np.arange(.6,5.1,.72):
 for y in np.arange(.52,2.02,.55):
  ax.plot([x-.095,x+.095],[y-.095,y+.095],c=C1,lw=1.5)
  ax.plot([x-.095,x+.095],[y+.095,y-.095],c=C1,lw=1.5)
ax.text(5.4,.6,r'$\mathbf{B}$ into page ($\otimes$)',color=C1,fontsize=11)
ax.text(1.65,-.07,'loop area increases',ha='center',color=BK)
ax.text(-.38,1.27,'$R$',color=BK);ax.text(rod,2.32,'sliding bar',color=C2,ha='center')
ax.annotate('',(2.1,top+.03),(3.05,top+.03),arrowprops={'arrowstyle':'<-','lw':1.8,'color':C3})
ax.set_xlim(-.65,8.2);ax.set_ylim(-.38,2.72)
save(fig,'09-motional-emf.svg')
# RLC analytical response all initial charge=1, initial current=0
fig,ax=plt.subplots(figsize=(7.3,3.7))
t=np.linspace(0,11,1200)
for R,c,lbl in [(0.5,C1,'underdamped: R=0.5'),(2.0,C3,'critical: R=2'),(3.0,C2,'overdamped: R=3')]:
 gam=R/2
 if gam<1:
  w=(1-gam**2)**.5; q=np.exp(-gam*t)*(np.cos(w*t)+gam/w*np.sin(w*t))
 elif gam==1:q=(1+t)*np.exp(-t)
 else:
  d=np.sqrt(gam**2-1);a=(-gam+d);b=(-gam-d);q=(-b*np.exp(a*t)+a*np.exp(b*t))/(a-b)
 ax.plot(t,q,lw=1.9,c=c,label=lbl)
ax.axhline(0,lw=.8,c=GR);ax.set_xlim(0,11);ax.set_ylim(-.4,1.07);ax.set_xlabel('Time  t  (L = C = 1)');ax.set_ylabel('Charge  Q(t) / Q(0)');ax.legend(frameon=False,loc='upper right',fontsize=9);ax.grid(alpha=.18)
save(fig,'10-rlc-response.svg')
# Fig 11 2 panels with careful distinct purposes
fig=plt.figure(figsize=(9.2,3.6)); ax=fig.add_subplot(121); ax2=fig.add_subplot(122)
for a in (ax,ax2):a.axis('off');a.set_aspect('equal')
# left: side on capacitor with one wire and gap
ax.plot([.4,1.55],[1.7,1.7],c=BK,lw=2);ax.plot([2.35,3.5],[1.7,1.7],c=BK,lw=2)
ax.plot([1.55,1.55],[.8,2.6],c=C2,lw=5);ax.plot([2.35,2.35],[.8,2.6],c=C1,lw=5)
for y in [1.05,1.4,1.75,2.1,2.45]:ax.annotate('',(2.22,y),(1.7,y),arrowprops={'arrowstyle':'->','lw':1.2,'color':C3})
ax.annotate('',(1.15,1.7),(.65,1.7),arrowprops={'arrowstyle':'->','lw':1.5,'color':C2})
ax.text(1.96,2.9,'Changing electric flux',color=C3,ha='center',fontsize=9)
ax.text(1,2.03,'current $I$',color=C2,ha='center',fontsize=9)
ax.text(1.55,.45,'$+Q$',color=C2,ha='center');ax.text(2.35,.45,'$-Q$',color=C1,ha='center')
ax.set_xlim(.1,3.9);ax.set_ylim(.2,3.2)
ax.set_title('A. Charging capacitor',fontsize=10)
# right: 3D flattened representations of two surfaces sharing oriented boundary, cylinder projection
th=np.linspace(0,2*np.pi,180);cx,cy=1.85,1.6;rx=1.35;ry=.45
x=cx+rx*np.cos(th);y=cy+ry*np.sin(th)
ax2.fill(x,y,color='#b5d8e3',alpha=.35);ax2.plot(x,y,color=BK,lw=1.8)
# curved cap mesh z offset upward in depiction; illustrates same boundary only
for rr in [.25,.5,.75]:
 x2=cx+rx*rr*np.cos(th);y2=cy+ry*rr*np.sin(th)+.8*(1-rr*rr)
 ax2.plot(x2,y2,c=C3,lw=.85,alpha=.8)
for aa in np.linspace(0,2*np.pi,11):
 rr=np.linspace(0,1,24)
 xx=cx+rx*rr*np.cos(aa);yy=cy+ry*rr*np.sin(aa)+.8*(1-rr*rr)
 ax2.plot(xx,yy,c=C3,lw=.6,alpha=.65)
ax2.text(cx,2.68,'Curved spanning surface $S_2$',ha='center',color=C3,fontsize=9)
ax2.text(cx,.77,'Flat spanning surface $S_1$',ha='center',color=C1,fontsize=9)
ax2.text(cx+1.55,1.37,'$C$',color=BK)
ax2.text(cx, .31,'Both have the SAME boundary C',ha='center',fontsize=9,color=BK)
ax2.set_xlim(.1,4.0);ax2.set_ylim(.1,3.05);ax2.set_title('B. Surface independence (geometric sketch)',fontsize=10)
save(fig,'11-charging-capacitor.svg')
# 12 two stacked same-phase curves; no misleading 3D
fig,axes=plt.subplots(2,1,figsize=(7.2,3.85),sharex=True)
phase=np.linspace(0,4*np.pi,600)
axes[0].plot(phase,np.cos(phase),color=C2,lw=1.9);axes[0].set_ylabel('$E_x/E_0$');axes[0].set_ylim(-1.35,1.35)
axes[1].plot(phase,np.cos(phase),color=C1,lw=1.9);axes[1].set_ylabel('$cB_y/E_0$');axes[1].set_ylim(-1.35,1.35)
for ax in axes:ax.axhline(0,c=GR,lw=.8);ax.grid(alpha=.15)
axes[1].set_xlabel('Position  $kz$  (at fixed time $t=0$)')
axes[1].set_xticks([0,np.pi,2*np.pi,3*np.pi,4*np.pi],['0','$\\pi$','$2\\pi$','$3\\pi$','$4\\pi$'])
fig.suptitle('Propagation along +z: E along x, B along y (same phase)',fontsize=11)
fig.tight_layout()
save(fig,'12-plane-wave.svg')
print('Generated:',*[p.name for p in out.glob('*.svg')],sep='\n- ')
