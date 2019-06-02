n = 10
z = {(x, y) for x in range(1, n) for y in range(1, n) if x % y == 0 and x != y}
print(z)

elements = {(x, y) for x in range(1, n) for y in range(1, n)}
elements = filter(lambda x: x[0] != x[1], elements)
elements = filter(lambda x: x[0] % x[1] == 0, elements)
print(set(elements))

elements = {(x, y) for x in range(1, n) for y in range(1, n)}
elements = filter(lambda x: x[0] != x[1] and x[0] % x[1] == 0, elements)
print(set(elements))
