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
labels = [r'$-2\pi$', r'$-\frac{3\pi}{2}$',
          r'$-pi$', r'$-\frac{\pi}{2}$', 0,
          r'$\frac{\pi}{2}$', r'$pi$',
          r'$\frac{3\pi}{2}$', r'$+2\pi$',]
plt.xticks(np.arange(-2*np.pi,2.5*np.pi,np.pi/2),labels)
ax.plot(X,F1,label="$sin(x)$")
ax.plot(X,F2,label="$3 sin(x)$")
ax.legend(loc="upper right")
plt.show()
