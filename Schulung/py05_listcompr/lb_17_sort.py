lst = [123, 17, 4, 69, 9, 259]
lst.sort()
print(lst)          

def f(x):
    return x[0]+x[1]


st = [(1,3),(4,1),(1,1)]

lst.sort(key=f, reverse=True )
print(lst)