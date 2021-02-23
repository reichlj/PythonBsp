import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-3.0,3.0,100)
ylist = np.linspace(-3.0,3.0,100)
X,Y = np.meshgrid(xlist,ylist)
Z = np.sqrt(X**2+Y**2)
#plt.figure() nicht notwendig
n = 4
if n==1:
    cp = plt.contour(X, Y, Z)
elif n==2:
    cp = plt.contour(X,Y,Z,colors='r',linestyles='dashed')
    plt.clabel(cp,inline=True,fontsize=10)
elif n==3:
    cp = plt.contourf(X,Y,Z)
    plt.colorbar(cp)
elif n==4:
    cp = plt.contour(X,Y,Z,levels=[0.0,0.2,0.5,0.9,1.5,2.5,3.5])
    plt.clabel(cp,inline=True,fontsize=10)

plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.title('Kontourplot')
plt.show()