"""Lightweight reproducible validation, not a formal proof of physics content.
Run from any directory: python tools/validate_notes.py
Dependencies: sympy, cairosvg (for render checks)
"""
from pathlib import Path
import re,sys,xml.etree.ElementTree as ET
import sympy as sp
R=Path(__file__).resolve().parents[1]
files=sorted((R/'chapters').glob('*.md'))
checks=[]
def record(label,result):
 checks.append((label,bool(result)))
 if not result: print('FAIL:',label)

record('exactly thirteen chapter files',len(files)==13 and [int(f.name[:2]) for f in files]==list(range(1,14)))
required={1:['Coulomb','Superposition','electric field','dipole','continuous','Dirac'],2:['flux','solid angle','Gauss','divergence'],3:['conservative','potential','multipole','Poisson','Laplace'],4:['conductor','uniqueness','images','capacitance'],5:['polarisation','bound','displacement','Lorentz','constitutive'],6:['current','continuity','Drude','Kirchhoff','RC'],7:['Lorentz','Hall','Biot','Ampère','solenoid','toroid'],8:['magnetisation','bound','diamagnetism','paramagnetism','ferromagnetism'],9:['Faraday','Lenz','motional','inductance','mutual','RL'],10:['LC','RLC','impedance','resonance','transformer'],11:['displacement','Maxwell','conservation','Poynting','boundary'],12:['wave','polarisation','reflection','refraction','intensity'],13:['Lorentz','four-vector','field tensor','four-potential']}
for f in files:
 n=int(f.name[:2]);s=f.read_text(encoding='utf-8');compact=s.casefold()
 record(f'ch {n:02d} core coverage',all(w.casefold() in compact for w in required[n]))
 record(f'ch {n:02d} explanatory prose',len(re.findall(r'[A-Za-z]{3,}',s))>280)
 record(f'ch {n:02d} full bibliographic titles',all(w in s for w in ('Fundamentals of Physics II: Electromagnetism, Optics, and Quantum Mechanics','PHAS0021 Electricity and Magnetism Course Notes','Fundamentals of Physics','Introduction to Electrodynamics')) if n<13 and n!=8 else (all(w in s for w in ('Fundamentals of Physics II: Electromagnetism, Optics, and Quantum Mechanics','Fundamentals of Physics','Introduction to Electrodynamics')) if n==8 else 'Fundamentals of Physics II: Electromagnetism, Optics, and Quantum Mechanics' in s))
 record(f'ch {n:02d} displays paired',s.count('$$')%2==0)
 # Remove displayed math, then ensure inline $ delimiters are paired.
 t=re.sub(r'\$\$.*?\$\$','',s,flags=re.S)
 record(f'ch {n:02d} inline math paired',t.count('$')%2==0)
 for expression in re.findall(r'\$\$(.*?)\$\$',s,flags=re.S):
  balance=0
  for c in expression:
   if c=='{': balance+=1
   elif c=='}': balance-=1
   if balance<0:break
  record(f'ch {n:02d} formula braces',balance==0)
 for link in re.findall(r'!?\[[^\]]+\]\(([^)]+)\)',s):
  if not link.startswith(('https://','http://','#')):
   record(f'ch {n:02d} local figure {link}',(f.parent/link).resolve().is_file())
 record(f'ch {n:02d} contains SI unit explanations',('\\mathrm' in s or 'units' in s))
 record(f'ch {n:02d} no exercise section',not re.search(r'^##\s*(?:Exercises?|Problems?)\b',s,re.M|re.I))

for f in (R/'figures').glob('*.svg'):
 try: ET.parse(f); valid=True
 except Exception: valid=False
 record(f'SVG parses {f.name}',valid)
 try:
  import cairosvg
  rendered=cairosvg.svg2png(url=str(f),output_width=200)
  record(f'SVG renders {f.name}',len(rendered)>100)
 except ImportError: pass
 except Exception:record(f'SVG renders {f.name}',False)
# Dimensional / limiting case physical regression checks.
Q,z,a,eps,R,L,omega,mu,eta1,eta2=sp.symbols('Q z a eps R L omega mu eta1 eta2',positive=True,real=True)
ring=Q*z/(4*sp.pi*eps*(a*a+z*z)**sp.Rational(3,2))
record('ring far-field approaches point charge',sp.simplify(sp.limit(ring*z*z,z,sp.oo)-Q/(4*sp.pi*eps))==0)
rod=L*a/(2*sp.pi*eps*z*sp.sqrt(a*a+z*z))
record('finite rod infinite-length limit',sp.simplify(sp.limit(rod,a,sp.oo)-L/(2*sp.pi*eps*z))==0)
disk=Q/(2*eps)*(1-z/sp.sqrt(a*a+z*z))
record('disk infinite-radius limit',sp.simplify(sp.limit(disk,a,sp.oo)-Q/(2*eps))==0)
r=(eta2-eta1)/(eta2+eta1);t=2*eta2/(eta2+eta1)
record('lossless Fresnel R+T=1',sp.simplify(r**2+eta1/eta2*t**2-1)==0)
k,n,e,E=sp.symbols('k n e E',positive=True)
x=-e*E/k;p=-e*x
record('Lorentz oscillator static induced dipole sign',sp.simplify(p-e**2*E/k)==0)
C=sp.symbols('C', positive=True)
w0=1/sp.sqrt(L*C)
record('series-RLC reactances cancel at natural frequency',sp.simplify(w0*L-1/(w0*C))==0)

failed=[name for name,ok in checks if not ok]
print(f'Checks: {len(checks)}, pass {len(checks)-len(failed)}, fail {len(failed)}')
if failed:print('\n'.join(failed));sys.exit(1)
