import numpy as np
A = np.array([3,4,6,10,24,89,45,43,46,99,100])
A[A%3!=0]
A
A[A%5==0]
A[(A%3==0) & (A%5==0)]
A[A%3==0] = 42
A
