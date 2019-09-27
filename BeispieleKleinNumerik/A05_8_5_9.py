import numpy as np

m=np.array([[1,2,3],[4,5,6]])
print(m)
um = m[:,::-1]
print(um)
zum = m[::-1,:]
print(zum)
zsum = m[::-1,::-1]
print(zsum)
t=m.transpose()
print(t)
