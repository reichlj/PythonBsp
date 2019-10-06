import numpy as np
X = np.array(
    [[[3, 1, 2],
      [4, 2, 2]],
     [[-1, 0, 1],
      [1, -1, -2]],
     [[3, 2, 2],
      [4, 4, 3]],
     [[2, 2, 1],
      [3, 1, 3]]])
print(X.shape)

print("Dimension 0 with size ", X.shape[0])
for i in range(X.shape[0]):
    print(f"\nAusgabe von X[{i:1},:,:]:")
    print(X[i,:,:])

print('axis=0',X.sum(axis=0))
print('axis=1',X.sum(axis=1))
print('axis=2',X.sum(axis=2))

print("\nDimension 1 with size ", X.shape[1])
for i in range(X.shape[1]):
    print(f"\nAusgabe von X[:,{i:1},:]:")
    print(X[:,i,:])

print("\nDimension 2 with size ", X.shape[2])
for i in range(X.shape[2]):
    print(f"\nAusgabe von X[:,:,{i:1}]:")
    print(X[:,:,i])

print('may_share_memory : ', np.may_share_memory(X, X[:,:,2]))
