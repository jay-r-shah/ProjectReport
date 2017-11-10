# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 16:36:36 2015

@author: Jay
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
hotT=[40.,45.,50.,60.,170.,200.];
hotH=[2800.,3150.,3562.125,6592.52,6592.525,6688.915];
coldT=[14.,14.,40.,150.];
coldH=[2000.,2263.85,2276.5432,2645.5683];
dTmin=10
def yhot(x):
    if x>max(hotH):
        return max(coldT)+100
    if x<min(hotH):
        return min(coldT)-100
    for n in range(len(hotT)):
        if hotH[n]<=x<=hotH[n+1]:
            return hotT[n]+((hotT[n+1]-hotT[n])/(hotH[n+1]-hotH[n]))*(x-hotH[n])
def ycold(x):
    if x>max(coldH):
        return max(coldT)
    if x<min(coldH):
        return min(coldT)
    for n in range(len(coldT)):
        if coldH[n]<=x<=coldH[n+1]:
            return coldT[n]+((coldT[n+1]-coldT[n])/(coldH[n+1]-coldH[n]))*(x-coldH[n])

xhot=np.arange(min(hotH),max(hotH),3)
xcold=np.arange(min(coldH),max(coldH),3)
fig=plt.figure()
ax1=fig.add_subplot(111)
fig.show()
ax1.plot(xcold,[ycold(x) for x in xcold],'b--')
hotstep=xhot[1]-xhot[0]

if max(coldH)-min(coldH)<max(hotH)-min(hotH):
    a=np.arange(min(coldH),max(coldH),hotstep)
    hoty=[yhot(x) for x in xhot]
    coldy=[ycold(x) for x in a]
else:
    a=np.arange(min(hotH),max(hotH),hotstep)
    hoty=[yhot(x) for x in a]
    coldy=[ycold(x) for x in xcold]

n=0
a=np.array(a)
b=a+min(hotH)-min(coldH)
hotdic=dict(zip(list(b),[yhot(x) for x in list(b)]))
colddic=dict(zip(list(b),coldy))
while True:
    count=0
    for xval in hotdic.keys():
        if colddic[xval]<yhot(xval)-dTmin:
            count+=1
    print count,len(b)
    if count==len(b):
        break
    else:
        b=b+hotstep
        hotdic=dict(zip(list(b),[yhot(x) for x in list(b)]))
        colddic=dict(zip(list(b),coldy))
ax1.plot(xhot,hoty,'r')
ax1.plot(b,[ycold(x) for x in a],'b')
fontP = FontProperties()
fontP.set_size('small')
diff=[hotdic[val]-colddic[val] for val in colddic.keys()]
q=abs(np.array(diff)-dTmin)
coldpinch= colddic.values()[q.argmin()]
hotpinch=hotdic.values()[q.argmin()]
print 'Hot pinch temperature = '+ str(hotpinch)
print 'Cold pinch temperature = ' + str(coldpinch)
ax1.plot(colddic.keys()[q.argmin()],coldpinch,'*k')
ax1.plot(hotdic.keys()[q.argmin()],hotpinch,'*k')
ax1.set_xlabel('Enthalpy (kW)')
ax1.set_ylabel('Temperature (Celsius)')
ax1.set_ylim(0,250)
