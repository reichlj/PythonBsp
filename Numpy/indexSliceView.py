import numpy as np
print('No slicing')
a = np.array([[1,2,3],[4,5,6]])
print(a)
b= a[0,1]
print(b)
b=17
print(a)
print(b)

print('Slicing')
a = np.array([[1,2,3],[4,5,6]])
print(a)
b= a[0:1, 1]
print(b,b.shape)
b[0] = 17
print(a)
print(b)