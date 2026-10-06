#!/usr/bin/env python3
"""Schematic regime map from proved exponents; no simulated data."""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/landscape-mpl')
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(11,4.4),layout='constrained')
p=np.linspace(.02,4,400)
axs[0].axvspan(0,1,color='#d8eee8');axs[0].axvspan(1,3,color='#f7e5b7');axs[0].axvspan(3,4,color='#efd5d7')
axs[0].plot(p,np.minimum(0,(1-p)/(1+p)),color='#23645a',label='Summit')
axs[0].plot(p,np.minimum(0,(3-p)/(1+p)),color='#a43f49',label='Integrated elevation, d=2')
axs[0].axvline(1,color='#555',ls=':',lw=1);axs[0].axvline(3,color='#555',ls=':',lw=1)
axs[0].set(xlabel='Exponent ratio p = m/n',ylabel='Power of D in leading size',title='Finiteness thresholds (d = 2)',xlim=(0,4),ylim=(-.65,.12))
axs[0].text(1,.055,'log',ha='center');axs[0].text(3,.055,'log',ha='center');axs[0].legend(loc='lower left',frameon=False)
b=np.linspace(.01,3,400);p0=.75
axs[1].plot(b,np.minimum((b+1-p0)/(p0+1),1),color='#245680',lw=2)
axs[1].axvline(2*p0,color='#555',ls=':',lw=1)
axs[1].text(.7,.83,'Summit contribution\n'+r'$D^{(\beta+1-p)/(p+1)}$',ha='center')
axs[1].text(2.3,.74,'Outer contribution\nD',ha='center')
axs[1].annotate('D log(1/D)',xy=(1.5,1),xytext=(1.8,1.17),arrowprops={'arrowstyle':'->'})
axs[1].set(xlabel='Moment weight β (p = 0.75)',ylabel='Generic correction exponent',title='Correction threshold β = 2p',xlim=(0,3),ylim=(0,1.3))
fig.suptitle('A finite observable can retain a singular summit correction',fontsize=14)
fig.text(.02,-.045,'Schematic asymptotic regimes. Zero exponent on the left denotes a finite limit except at marked logarithmic thresholds.\nCorrection coefficients may vanish; the right panel does not assert a nonzero leading term in every case.',fontsize=9)
out=ROOT/'figures';out.mkdir(exist_ok=True)
for ext in ['pdf','png']:fig.savefig(out/f'thresholds.{ext}',dpi=180,bbox_inches='tight')
