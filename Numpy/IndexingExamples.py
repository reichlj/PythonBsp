import numpy as np

Y = np.arange(10,20)
print(Y)
index= np.array([2,3,6,7])
print(Y[index])
Z = Y[index]
print(Z>14)
print(Y[index][Z>14])
