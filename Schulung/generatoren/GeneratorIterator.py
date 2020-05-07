s = 'abc'
it = iter(s)
print(type(it))


def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

print(type(reverse))
obj = reverse('abcd')
print(type(obj))

obj = (i*i for i in range(10))
print(type(obj))