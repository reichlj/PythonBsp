import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots()

x = np.arange(1,7,0.1)

ax1.plot(x, 2*np.pi*x, lw=2, color='blue')
ax1.set_ylabel(r'Circumference $(cm)$')
for label in ax1.get_yticklabels():
    label.set_color('blue')

ax2 = ax1.twinx()
ax2.plot(x, np.pi*x**2, lw=2, color='darkgreen')
ax2.set_ylabel(r'area $(cm^2)$')
for label in ax2.get_yticklabels():
    label.set_color('darkgreen')

plt.show()
