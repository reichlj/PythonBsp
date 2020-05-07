my_list = [('a',232), ('b',343), ('c',543), ('d',23)]
print(list(zip(*my_list)))

lst = []
for item in zip(*my_list):
    lst.append(item)
print(lst)