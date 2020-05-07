import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-4.1, 3.1, 150, endpoint=True)
F = X**5 + 3*X**4 - 11*X**3 - 27*X**2 + 10*X + 24
fig, ax = plt.subplots()
ax.plot(X, F)

minimum1 = -1.5264814, -7.051996717492152
minimum2 = 2.3123415793720303, -81.36889464201387

ax.annotate('minima',
            xy=minimum1,
            xytext=(-1.5,-50),
            arrowprops=dict(arrowstyle='->',
                connectionstyle='angle3,angleA=0,angleB=-90'))
ax.annotate(' ',
            xy=minimum2,
            xytext=(-0.7,-50),
            arrowprops=dict(arrowstyle='->',
                connectionstyle='angle3,angleA=0,angleB=-90'))

maximum1 = -3.354758, 56.963107876630595
maximum2 = .168898282, 24.868343482875

ax.annotate('maxima',
            xy=maximum1,
            xytext=(-1.5,30),
            arrowprops=dict(arrowstyle='->',
                connectionstyle='angle3,angleA=0,angleB=-90'))
ax.annotate(' ',
            xy=maximum2,
            xytext=(-0.6,30),
            arrowprops=dict(arrowstyle='->',
                connectionstyle='angle3,angleA=0,angleB=-90'))

zeroes = -4, -2, -1, 1, 3
for zero in zeroes:
    zero = zero, 0
    ax.annotate('Zeroes',
            xy=zero,
            color='orange',
            bbox=dict(boxstyle='round', fc='none', ec='green'),
            xytext=(1,40),
            arrowprops=dict(arrowstyle='->',
                connectionstyle='angle3,angleA=0,angleB=-90'))
    
plt.show()
