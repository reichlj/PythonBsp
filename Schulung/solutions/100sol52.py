import numpy as np
xdata = np.arange(-5, 5, 0.5)
ydata = np.array([20.773, 15.04, 12.9, 9.5, 7.5, 4.3, 2.4, 1, 0.2, 0, 0, 0.6, 2.1, 3.9, 6, 8, 12, 14, 19, 23])
coefficients = np.polyfit(xdata, ydata, 2)
print(coefficients)
f = np.poly1d(np.polyfit(xdata, ydata, 2))
print(f(6.201765102680708))
