import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-2*np.pi, 2*np.pi, 100)
F1 = np.sin(X)
F2 = 3*np.sin(X)

fig, ax = plt.subplots()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi/2))
ax.plot(X,F1,X,F2)
plt.show()
