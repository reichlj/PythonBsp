lst = [3, 8, 9, 2, 123, 234]
def int2str(i):
    return str(i)
lst.sort(key=int2str)
print(lst)

lst = [3, 8, 9, 2, 123, 234]
lst.sort(key=lambda x: str(x))
print(lst)

lst = [3, 8, 9, 2, 123, 234]
lst.sort(key=str)
print(lst)