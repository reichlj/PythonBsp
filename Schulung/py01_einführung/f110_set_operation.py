A = {3, 78, 43, 2, 9}
B = {2, 89,  7, 9, 78}
print(78 in A)
print(A.discard(43))
A = {3, 78, 43, 2, 9}
print(A.remove(43))
print(A.discard(43)) # no exception
A = {3, 78, 43, 2, 9}
B = {2, 89,  7, 9, 78}
print(A.intersection(B))
print(A.union(B))
print(A.difference(B))
print(A.symmetric_difference(B))
print(A.pop())
print(A)
