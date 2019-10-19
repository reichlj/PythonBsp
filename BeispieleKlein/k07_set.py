a = {'123', 57, (6,7)}
print(a)
b = [1, 2 ,3]
try:
    a = {'123', 57, (6,7), b}
except TypeError as te :
    print(te)

