import numpy as np

A = np.array([10, 20, 30])
B = np.array([1, 2, 3])
A=A.reshape((3, 1))
print(A)
print(A*B)
B=B.reshape((1, 3))
print(A@B)

print('*********')
A1 = np.array([12, 22, 32])
print(A1)
B1 = np.array([1, 2, 3])
#A1=np.reshape(A1, (3, 1))
#A1=np.reshape(A1, (3, 1))
print(A1)
#print(A1*B1)
B1=np.reshape(B1,(1, 3))
print(A1@B1)

A2 = np.array([12, 22, 32])
B2 = np.reshape(A2,(3,1))
print(A2)
print(B2)
print(np.may_share_memory(A2,B2))
print('A2 :',id(A2))
print('B2 :',id(B2))
