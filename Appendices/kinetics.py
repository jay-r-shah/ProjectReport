import scipy
import scipy.integrate
import matplotlib.pyplot as plt 

arrC0 = [3.0,5.0,1.0,0.5]
k1 = 0.3
k2 = 0.1
tc = 1.0/(k1*arrC0[1])
t = scipy.linspace(0.0,7,100)
def deriv(arrC,t,arrk):
    [Ca,Cb,Cc,Cd] = arrC
    [k1,k2] = arrk
    dCa = -k1*Ca*Cb
    dCb = -k1*Ca*Cb-k2*Cb*Cc
    dCc = k1*Cb*Ca-k2*Cb*Cc
    dCd = k2*Cb*Cc
    arrdC=[dCa,dCb,dCc,dCd]
    return arrdC
C = scipy.integrate.odeint(deriv,arrC0,t,args=([k1,k2],))
fig = plt.figure();#ax=fig.add_subplot(111)
ax = fig.add_axes([0.1, 0.1, .8, .8])
print C
ax.plot(t,C[:,0],'r')
ax.plot(t,C[:,1],'b')
ax.plot(t,C[:,2],'m')
ax.plot(t,C[:,3],'g')
fig.show()
#fig.canvas.draw()
