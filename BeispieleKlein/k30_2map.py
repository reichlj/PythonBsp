y = lambda x : x + 42

z = map(y, range(1, 10, 1))
print(z)
print(type(z))
for count, x in enumerate(z,1):
    print("index={0:} value={1:}".format(count,x))
