class A:
    def __init__(self):
        print('__init__ has been executed')

x = A()
print(A.__dict__)
