#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:48:54 2019

@author: thierry
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

fac = np.sqrt(3./4.)

len_lattice_x = 6
len_lattice_y = 5
x = []
y = []
for j in range(len_lattice_y):
  for i in range(len_lattice_x):
    if np.mod(j,2)==0:
      x.append(i)
    else:
      x.append(i+0.5)
for j in range(len_lattice_y):
  for i in range(len_lattice_x):
    y.append(j*fac)
      
x = np.asarray(x)
y = np.asarray(y)

#x = np.asarray([0, 1, 2, 3, 0.5, 1.5, 2.5, 3.5])
#y = np.asarray([0, 0, 0, 0, fac, fac, fac, fac])

fig = plt.figure(figsize=(21,29))
ax = fig.add_subplot(111)
ax.set_aspect('equal')

'''this is for getting points to hand draw'''
if False:
  p = ax.plot(x,y,'*')
  for i in range(len(x)):
    ax.text(x[i],y[i], r' $P_{%i}$=(%i,%i)' %(i,x[i],y[i]), fontsize=12)

#add vessels
colorstring = 'b-'
colorstringCap = 'coral'
scaling = 5
minLineWidth = 2.5 * scaling
nextLineWidth = 3.15 *scaling
nextNextLineWidth = 3.61 *scaling
nextNextNextLineWidth = 3.97 * scaling
fontsize= 33
offsetX = -0.0
offsetY = 0.15
#po - p1
ax.plot([x[0],x[1]],[y[0],y[1]], color='coral', linewidth=minLineWidth )
ax.text(x[0]+offsetX,y[0]+offsetY, r'$r_{cap}$=2.5$\mu$m', fontsize= fontsize)
#p1 - p7
ax.plot([x[1],x[7]],[y[1],y[7]], colorstring, linewidth=minLineWidth)
circle1 = plt.Circle((x[7],y[7]), 0.4, color='k',linestyle=':', fill=False, linewidth=10)
ax.add_artist(circle1)
ax.text(x[7]+0.35,y[7]+0.35, r'$b_{1}$', fontsize= fontsize)
#p12 - p13
ax.plot([x[12],x[13]],[y[12],y[13]], color=colorstringCap, linewidth=minLineWidth)
ax.text(x[12]+offsetX,y[13]+offsetY, r'$r_{cap}$=2.5$\mu$m', fontsize= fontsize)
#p13 -p7
ax.plot([x[13],x[7]],[y[13],y[7]], colorstring, linewidth=minLineWidth)
#p7 -p 8
ax.plot([x[7],x[8]],[y[7],y[8]], colorstring, linewidth=nextLineWidth)
#ax.text(x[7]+offsetX,y[7]+offsetY, r'$r_1$=3.15 $\mu$m', fontsize=fontsize)
ax.text(x[7]+0.5,y[7]-0.25, r'$r_1$=3.15 $\mu$m', fontsize=fontsize)
#p8 - p15
ax.plot([x[8],x[15]],[y[8],y[15]], colorstring, linewidth=nextLineWidth)
#p18 - p19
ax.plot([x[18],x[19]],[y[18],y[19]], color=colorstringCap, linewidth=minLineWidth)
ax.text(x[18]+offsetX,y[18]+offsetY, r'$r_{cap}$=2.5$\mu$m', fontsize= fontsize)
#p19 - p20
ax.plot([x[19],x[20]],[y[19],y[20]], colorstring, linewidth=minLineWidth)

#p20 - p15
ax.plot([x[20],x[15]],[y[20],y[15]], colorstring, linewidth=minLineWidth)
circle2 = plt.Circle((x[15],y[15]), 0.4, color='k',linestyle=':', fill=False, linewidth=10)
ax.add_artist(circle2)
ax.text(x[15]+0.35,y[15]+0.35, r'$b_{2}$', fontsize= fontsize)
#p15 - p16
#ax.text(x[15]+offsetX,y[15]+offsetY, r'$r_2$=3.61 $\mu$m', fontsize=fontsize)
ax.text(x[15]+0.5,y[15]-0.25, r'$r_2$=3.61 $\mu$m', fontsize=fontsize)
ax.plot([x[15],x[16]],[y[15],y[16]], colorstring, linewidth=nextNextLineWidth)
#p16 - p22
ax.plot([x[16],x[22]],[y[16],y[22]], colorstring, linewidth=nextNextLineWidth)
circle3 = plt.Circle((x[22],y[22]), 0.4, color='k',linestyle=':', fill=False, linewidth=10)
ax.add_artist(circle3)
ax.text(x[22]+0.35,y[22]+0.35, r'$b_{3}$', fontsize= fontsize)
#p24 - p25
ax.plot([x[24],x[25]],[y[24],y[25]], color=colorstringCap, linewidth=minLineWidth )
ax.text(x[24]+offsetX,y[24]+offsetY, r'$r_{cap}$=2.5$\mu$m', fontsize= fontsize)
#p25 - p26
ax.plot([x[25],x[26]],[y[25],y[26]], colorstring, linewidth=minLineWidth )
#p26 - p27
ax.plot([x[26],x[27]],[y[26],y[27]], colorstring, linewidth=minLineWidth )
#p27 - p28
ax.plot([x[27],x[28]],[y[27],y[28]], colorstring, linewidth=minLineWidth )
#p28 - p22
ax.plot([x[28],x[22]],[y[28],y[22]], colorstring, linewidth=minLineWidth )
#p22 - p23
#ax.text(x[22]+offsetX,y[22]+offsetY, r'$r_3$=3.97 $\mu$m', fontsize= fontsize)
ax.text(x[22]+0.5,y[22]-0.25, r'$r_3$=3.97 $\mu$m', fontsize= fontsize)
ax.plot([x[22],x[23]],[y[22],y[23]], colorstring, linewidth=nextNextNextLineWidth)


ax.axis('off')
#ax.get_xaxis().set_visible(False)
#ax.get_yaxis().set_visible(False)

with PdfPages('discrete_daughter_differences_at_bifurcation.pdf') as pdf:
  pdf.savefig(fig)
plt.close()

#fig.tight_layout()
#plt.show()