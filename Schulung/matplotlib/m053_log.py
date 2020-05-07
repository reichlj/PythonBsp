import matplotlib.pyplot as plt
from numpy import arange

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x = arange(0, 5, 0.25)
ax.plot(x,x**2,x,x**3)
ax.set_yscale('log')

plt.show()
