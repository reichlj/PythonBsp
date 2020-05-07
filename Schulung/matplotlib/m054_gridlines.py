import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

def g(t):
    return np.sin(t)*np.cos(1/(t+0.1))

fig, ax = plt.subplots()

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

ax.plot(t1,g(t1),'ro',t2,f(t2),'k')
ax.grid(color='b',alpha=0.5,linestyle='dashed',linewidth=0.5)

plt.show()
