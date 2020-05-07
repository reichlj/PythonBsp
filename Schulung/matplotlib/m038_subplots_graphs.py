import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + x*np.cos(x)

def fp(x):
    return x* np.sin(x)

plt.figure(figsize=(6, 4))
X = np.arange(-5, 5, 0.05)
fig, ax =plt.subplots(2,sharex='col',sharey='row')

ax[0].plot(X,f(X),'bo',X,f(X),'k')
ax[0].set(title='The function f')

ax[1].plot(X,fp(X),'o',X,fp(X),'k')
ax[1].set(xlabel='X Values', ylabel='Y Values',
          title='Derivative Function of f')

plt.show()