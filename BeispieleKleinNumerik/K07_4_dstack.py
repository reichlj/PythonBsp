import numpy as np

# 2d-arrays
A = np.array([[3,4,5]])
B = np.array([[1,9,0]])
D = np.array([[10,90,20]])
E = np.array([[11,91,21]])
print(A)
print(B)
print(np.shape(A), np.shape(B))
C = np.dstack((A,B,D,E))
print(C)
print(C.shape)
print('*** R-G-B-Colors ***')
# 2d-arrays
R = np.array([[3,4,5],[13,14,15]])
G = np.array([[1,9,0],[11,19,10]])
B = np.array([[10,90,20],[110,190,120]])
print(R)
print(G)
print(B)
print(np.shape(R), np.shape(G), np.shape(B))
C = np.dstack((R,G,B))
print(C)
print(C.shape)
print(C[:,:,0])
print(C[:,:,1])
print('*** 1-d ***')


# 1d-arrays
A = np.array([3,4,5])
B = np.array([1,9,0])
D = np.array([10,90,20])
E = np.array([11,91,21])
print(A)
print(B)
print(np.shape(A), np.shape(B))
# note: A (3,) -> (1,3) -> (1,3,:)
C = np.dstack((A,B,D,E))
print(C)
print(C.shape)

