import numpy as np
x = np.array([2,5,18,14,4])
y = x[:,np.newaxis]
z = x[np.newaxis,:]
print(y,y.shape)
print(z,z.shape)