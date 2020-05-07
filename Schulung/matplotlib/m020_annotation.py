import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-2*np.pi, 2*np.pi, 150, endpoint=True)
F = np.cos(X)

fig, ax = plt.subplots()
ax.plot(X, F)
maximum = (0,1)
minimum = (np.pi,-1)
ax.annotate('local maximum',maximum)
ax.annotate('local minimum',minimum)
plt.show()
