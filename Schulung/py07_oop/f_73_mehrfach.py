class A(object):
    def m(self):
        print('m in A')
    
class B(A):
    pass

class C(A):
    def m(self):
        print('m in C')

class D(B,C):
    pass

a = A()
a.m()
b = B()
b.m()
c = C()
c.m()
d = D()
d.m()
print(D.mro())