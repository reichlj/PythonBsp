def rev(lst):
    rlist = []
#    while lst:
#        rlist.append(lst.pop())
    for k in range(len(lst)):
        rlist.append(lst.pop())
    return rlist

lst = ['a', 'b', 'c', 'd']
print(lst)
print(rev(lst))
print(lst)
lst = ['a', 'b', 'c', 'd']
lst.reverse()
print(lst)