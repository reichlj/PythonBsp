import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-4.0,4.0,30)
ylist = np.linspace(-4.0,4.0,50)

X = np.tile(xlist,(ylist.shape[0],1))
Y = np.tile(ylist.reshape(-1,1),(1,xlist.shape[0]))

X1,Y1 = np.meshgrid(xlist,ylist)
print('X==X1 ?',np.array_equal(X,X1))
print('Y==Y1 ?',np.array_equal(Y,Y1))

Z = np.sqrt(X**2+Y**2)
plt.contour(X, Y, Z)
plt.title('Kontourplot')
plt.show()