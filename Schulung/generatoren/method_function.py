class MyClass:
    
    def func(self):
        print('Function func')

print(type(MyClass.func))
x = MyClass()
print(type(x.func))
print(type(MyClass))
print(type(x))


s = 'abc'
it = iter(s)
print(type(it))


def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

print(type(reverse))
obj = reverse('abcd')
print(type(obj))