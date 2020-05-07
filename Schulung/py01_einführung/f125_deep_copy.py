from copy import deepcopy

list1 = ['a','b', ['ab','ba']]
list2 = deepcopy(list1)

print(id(list1))
print(id(list2))
print(id(list1[2]))
print(id(list2[2]))
print(id(list1[2][0]))
print(id(list2[2][0]))


print(id(lst1),id(lst2),id(lst1)==id(lst2))

print(id(lst1[0]),id(lst2[0]), id(lst1[0])==id(lst2[0]))
print(id(lst1[2]),id(lst2[2]), id(lst1[2])==id(lst2[2]))
print(id(lst1[2][0]),id(lst2[2][0]), id(lst1[2][0])==id(lst2[2][0]))

print('Tupel')
lst1 = ['a','b',('ab','cd')]
lst2 = deepcopy(lst1)

print(id(lst1),id(lst2),id(lst1)==id(lst2))

print(id(lst1[0]),id(lst2[0]),id(lst1[0])==id(lst2[0]))
print(id(lst1[2]),id(lst2[2]),id(lst1[2])==id(lst2[2]))