def anwenden(f, liste):
    result = []
    for x in liste:
        result.append(f(x))
    return result


y = (lambda x: x+42)(3)
print(y)
for k in range(10):
    print((lambda x: x+42)(k))
f42 = lambda x: x+42
print(f42(100))
print(type(f42))
r = anwenden(f42,range(10,20,1))
print(r)
r = anwenden(lambda x: x+100,range(10,20,1))
print(r)
