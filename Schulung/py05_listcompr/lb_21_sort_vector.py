lst = [ [2,6], [1,3], [5,4], [1,0] ]
lst.sort(key=lambda x: x[1])
print(lst)

lst = [ [2,6], [1,3], [5,4], [1,0] ]
lst.sort(key=lambda x: sum(x))
print(lst)

