L = [3, 4]
print(id(L),L)
L = L + [42]
print(id(L),L)

L = [3, 4]
print(id(L),L)
L += [42]
print(id(L),L)

L = [3, 4]
print(id(L),L)
L.append(42)
print(id(L),L)

