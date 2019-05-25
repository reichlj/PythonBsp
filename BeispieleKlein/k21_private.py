class MyClass:

    def __init__(self):
        self.__private_name = 'my private name'

x = MyClass()
print('type(x)    :',type(x))
print('x.__dict__ :', x.__dict__)
x._MyClass__private_name = 'Hallo'
x.__private_name = 'Hallo'
print(x.__dict__)
print(x.__private_name)
