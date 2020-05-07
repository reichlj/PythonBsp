import matplotlib.pyplot as plt
from numpy import arange

fig = plt.figure()
fig, axes = plt.subplots(1,3,figsize=(12,4))

x = arange(0, 5, 0.25)

axes[0].plot(x,x**2,x,x**3)
axes[0].set_title('default axes ranges')

axes[1].plot(x,x**2,x,x**3)
axes[1].axis('tight')
axes[1].set_title('tight axes')

axes[2].plot(x,x**2,x,x**3)
axes[2].set_xlim([2,5])
axes[2].set_ylim([0,60])
axes[2].set_title('custom axes ranges')

plt.show()
