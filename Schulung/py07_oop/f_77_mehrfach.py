class A(object):
    def m(self):
        print('do A')
    
class B(A):
    def _m(self):
        print('do B')
    def m(self):
        self._m()
        A.m(self)

class C(A):
    def _m(self):
        print('do C')
    def m(self):
        self._m()
        A.m(self)

class D(B,C):
    def m(self):
        A.m(self)
        B._m(self)
        C._m(self)
        print('do D')

d = D()
d.m()

print(D.__mro__)
