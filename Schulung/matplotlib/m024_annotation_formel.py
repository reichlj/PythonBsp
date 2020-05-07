import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-2*np.pi, 2*np.pi, 100)
F1 = np.sin(X)
F2 = 3*np.sin(X)
fig, ax = plt.subplots()

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi/2))

ax.set_xticklabels( [r'$-2\pi$', r'$-\frac{3\pi}{2}$',
          r'$-pi$', r'$-\frac{\pi}{2}$', 0,
          r'$\frac{\pi}{2}$', r'$pi$',
          r'$\frac{3\pi}{2}$', r'$+2\pi$',] )

ax.plot(X,F1,label='$sin(x)$')
ax.plot(X,F2,label='$3 sin(x)$')
ax.legend(loc='lower left')
x = 3*np.pi/4
#plot vertical line
ax.plot([x,x],[-3,3*np.sin(x)], color='blue', linewidth=2.5,
        linestyle='--')
#print a blue dot
ax.scatter([x,],[3*np.sin(x),], 50, color='blue')
text_x, text_y = (3.5, 2.2)
ax.annotate(r'$3\sin(\frac{3\pi}{2}=\frac{3}{sqrt{2}}$',
            xy=(x,3*np.sin(x)),
            xytext=(text_x,text_y),
            arrowprops=dict(facecolor='orange',shrink=0.05),
            fontsize=12)
plt.show()
