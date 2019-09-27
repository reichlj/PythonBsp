import numpy as np
A = [[2, 3, 4], [12, 13, 14]]
X = np.array(A)
print(X.shape)
print('X=', X)
print('r0 using : for first row')
r0 = X[0, :]
print('r0=', r0)
print('X,r0 : ',np.may_share_memory(X,r0))
X[0,0]=32
print('X=', X)
print('r0=', r0)
print('a1 using :')
a1 = X[0, 0:1]
print('a1', a1)
print('X,a1 : ', np.may_share_memory(X, a1))
a1[0] = 52
print('X=', X)
print('a1', a1)
print('X,a1 : ', np.may_share_memory(X, a1))
print('a2 no slicing')
a2 = X[0, 0]
print('a2', a2)
print('X,a2 : ', np.may_share_memory(X, a2))

