class A:
    def __str__(self):
        return '__str__ 42'
a = A()
print(str(a))
print(repr(a))


class B:
    def __repr__(self):
        return '__repr__43'
b = B()
print(str(b))
print(repr(b))

a
class C:
    def __repr__(self):
        return 'C()'
    def __str__(self):
        return 'C__str__ 42'
c  = C()
print(c)
print(str(c))
print(repr(c))
d= eval(repr(c))
print(type(d))
