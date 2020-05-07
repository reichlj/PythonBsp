import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,2*np.pi,25,endpoint=True)
F1 = np.sin(X)
F2 = 5*np.sin(X)
F3 = 0.3*np.sin(X)
fig, ax = plt.subplots()
print(type(fig),type(ax))
ax.plot(X,F1,'ro')
ax.plot(X,F2,'bx')

plt.show()
