import numpy as np
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[10,20,30],[40,50,60]])
print(A)
print(B)
print(np.shape(A), np.shape(B))
C = np.dstack((A,B))
print(C)
print(C.shape)
print('Get A')
print(C[:,:,0])
print('Get B')
print(C[:,:,1])

