class A:
    def __init__(self):
        self.x = 'public'
        self._x = 'protected'
        self.__x = 'private'
        print('__init__ A called')

class B(A):
    def show_attributes(self):
        print(self.x)
        print(self._x)
        #print(self.__x)
        print(self._A__x)

class C(A):
    def __init__(self):
        pass
    def show_attributes(self):
        print(self.x)
        print(self._x)
        #print(self.__x)
        print(self._A__x)

if __name__ == '__main__':
    b = B()
    b.show_attributes()
    b._A__x += '1'
    b.show_attributes()
    c = C()
    c.show_attributes()
