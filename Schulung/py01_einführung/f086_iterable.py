fib = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for el in fib:
    print(el)
    
for i in range(len(fib)):
    print(i, fib[i])
    
x = [34, 65, 89, 78]
nlist=list(enumerate(x))
print(nlist)

for index, value in enumerate(x):
    print(index, value)