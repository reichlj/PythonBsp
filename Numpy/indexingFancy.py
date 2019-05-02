import numpy as np

print('Example 1')
a = np.arange(12)**2
i = np.array([1, 1, 3, 8, 5])
print(a[i])
j = np.array([[3, 4], [9, 7]])
print(a[j])
print('Example 2')
a = np.arange(12).reshape(3, 4)
print(a)
i = np.array([[0, 1], [1, 2]])
j = np.array([[2, 1], [3, 3]])
print(a[i, j])
print(a[i, 2])
print(a[:, j])
print('Example 3')
l = [i, j]
print(l)
s = np.array([i, j])
print(s)
print(s[0][0][1])
