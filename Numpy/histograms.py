import numpy as np
mu, sigma = 2, 0.5
v = np.random.normal(mu , sigma , 1000)
v
(n, bins) = np.histogram(v, bins=50, density = True)
print(n)
print(n.size)
print(bins)
print(bins.size)
print(bins[1:])
print(bins[:-1])
