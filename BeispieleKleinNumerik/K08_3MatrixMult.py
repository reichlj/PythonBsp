import numpy as np

A = np.array([[10, 20, 30],[100,200,300],[1000,2000,3000]])
B = np.array([1, 2, 3])
C = np.dot(A,B)
print('C', C.shape,C)
C = np.multiply(A,B)
print('C', C.shape,C)
