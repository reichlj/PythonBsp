import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,2*np.pi,50,endpoint=True)
F1 = np.sin(X)
F2 = 5*np.sin(X)
F3 = 0.3*np.sin(X)
fig, ax = plt.subplots()
ax.plot(X,F1)
ax.plot(X,F2)
ax.plot(X,F3)
#ax.plot(X,F1,X,F2,X,F3)
plt.show()
