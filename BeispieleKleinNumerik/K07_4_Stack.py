import numpy as np
A_1 = [[3,4,5]]
B_1 = [[1,9,0]]
D_1 = [[10,90,20]]

print('A_1: ', A_1)
A = np.array(A_1)
B = np.array(B_1)
D = np.array(D_1)
print(A)
print(B)
print(np.shape(A), np.shape(B))
C = np.dstack((A,B,D))
print(C)
print(C.shape)

