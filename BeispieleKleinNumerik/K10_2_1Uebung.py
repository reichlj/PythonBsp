import numpy as np

A = np.array([3,4,6,10,24,89,45,43,46,99,100])
print(A)
B = A[A%3!=0]
print(B, type(B))
cond = A%3!=0
print(cond,type(cond),type(cond[0]))

B = A[A%5==0]
print(B)

B = A[(A%5==0) & (A%3==0)]
print(B)

print("Bool'sche Operatoren")
print('5 and 3 :',5 and 3)
print('5 or 3  :',5 or 3)
print('0 and 3 :',0 and 3)
print('0 or 3  :',0 or 3)

#https://stackoverflow.com/questions/22646463/and-boolean-vs-bitwise-why-difference-in-behavior-with-lists-vs-nump
v1 = [1,2]
v2 = [10,11]
print('v1=',v1,'v2=',v2)
print('v1 or v2  :',v1 or v2)
print('v1 and v2 :',v1 and v2)
print('not v1    :',not v1)
v1 = []
print('v1=',v1,'v2=',v2)
print('v1 or v2  :',v1 or v2)
print('v1 and v2 :',v1 and v2)
print('not v1    :',not v1)

