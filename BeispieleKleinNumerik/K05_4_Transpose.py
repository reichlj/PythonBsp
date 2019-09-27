import numpy as np
A = [[2, 3, 4], [12, 13, 14]]
X = np.array(A)
T = X.transpose()
print(np.may_share_memory(X,T))
