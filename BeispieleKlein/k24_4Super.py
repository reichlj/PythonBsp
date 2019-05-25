class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
        super().m()
        print("m of B1 called")

class C(A):
    def m(self):
        print("m of C called")
        super().m()
        print("m of C1 called")

class D(B,C):
    def m(self):
        print("m of D called")
        super().m()

x = D()
x.m()
