import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0, 2*np.pi, 150, endpoint=True)
F1 = np.sin(X)
F2 = 3.5*np.sin(X/2)
F3 = 0.8*np.cos(X)

fig, ax = plt.subplots()
ax.plot(X,F1,color='blue',linewidth=2.5,linestyle='-')
ax.plot(X,F2,color='red',linewidth=1.5,linestyle='--')
ax.plot(X,F3,color='green',linewidth=2,linestyle=':')

plt.show()
