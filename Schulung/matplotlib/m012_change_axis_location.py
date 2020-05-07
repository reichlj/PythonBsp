import matplotlib.pyplot as plt
import numpy as np

right_limit = 2*np.pi
X = np.linspace(-right_limit, right_limit,150,endpoint=True)
F = 5*np.sin(X)

fig, ax = plt.subplots()
print(type(fig),type(ax))
ax.plot(X,F,'ro')
min_x, max_x, min_y, max_y = -2, 4.8, -np.max(F), np.max(F)
ax.axis([min_x, max_x, min_y, max_y])

plt.show()
