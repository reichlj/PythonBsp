import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-4.0,4.0,30)
ylist = np.linspace(-4.0,4.0,50)

# Regel 1: Array, das weniger Dimensionen besitzt wird
#          mit 1 von links aufgefüllt
# Regel 2: Arrays mit Shape 1 werden angepasst

#           (50,1)              (30,) -> (1,30)  Regel 1
#           (50,30)                      (50,30) Regel 2
X = np.ones((ylist.shape[0],1))*xlist

#           (50,1)              (30,) -> (1,30)  Regel 1
#           (50,30)                      (50,30) Regel 2
Y = ylist.reshape((-1,1))*np.ones(xlist.shape[0])

#           (50,1)              (1,30)   Dimensionen gleich
#           (50,30)             (50,30)          Regel 2
Y = ylist.reshape((-1,1))*np.ones((1,xlist.shape[0]))

Z = np.sqrt(X**2+Y**2)
plt.contour(X, Y, Z)
plt.title('Kontourplot')
plt.show()