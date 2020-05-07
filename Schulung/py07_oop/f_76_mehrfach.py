class A(object):
    def m(self):
        print('m in A')
    
class B(A):
    def m(self):
        A.m(self)
        print('m in B')

class C(A):
    def m(self):
        A.m(self)
        print('m in C')

class D(B,C):
    def m(self):
        B.m(self)
        C.m(self)
        print('m in D')

d = D()
d.m()
print(D.__mro__)
