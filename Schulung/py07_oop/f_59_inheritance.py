class A:
    def __init__(self):
        self.x = 'public'
        self._x = 'protected'
        self.__x = 'private'
        print('__init__ A called')

class B(A):
    def __init__(self):
        A.__init__(self)
    def show_attributes(self):
        print(self.x)
        print(self._x)
        #print(self.__x)
        print(self._A__x)
        print(dir(self))

if __name__ == '__main__':
    b = B()
    b.show_attributes()
