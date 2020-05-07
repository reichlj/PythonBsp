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
    pass

d = D()
d.m()
