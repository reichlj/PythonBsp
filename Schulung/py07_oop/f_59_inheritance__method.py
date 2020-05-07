class A:
    def __init__(self):
        self.x = 'public'
        self._x = 'protected'
        self.__x = 'private'
        print('__init__ A called')
        
    def _m(self):
        print('This is _m!')
    def __m(self):
        print('This is __m!')

class B(A):
    def __init__(self):
        A.__init__(self)
    def show_attributes(self):
        self._m()
        self._A__m()
        #self.__m()
        print(dir(self))

if __name__ == '__main__':
    b = B()
    b.show_attributes()
