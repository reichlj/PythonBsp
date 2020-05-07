list1 = ['ab','ba']
list2 = list1
print(id(list1))
print(id(list2))

list2[1]='d'
print(list1)
print(list2)

list1 = ['a','b', ['ab','ba']]
list2 = list1[:]
print(id(list1))
print(id(list2))
print(id(list1[2]))
print(id(list2[2]))

list2[0] = 'c'
print(list1[0])
print(list2[0])

list2[2][1]='d'
print(list1[2][1])
print(list2[2][1])
