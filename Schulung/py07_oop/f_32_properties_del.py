class P:
    def __init__(self, x):
        self.__setX(x)
        
    def __getX(self):
        return self.__x

    def __setX(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    def __delx(self):
        del self.__x
        print('x deleted')
            
    x = property(__getX, __setX, __delx, "Docstring 'x'")


class Q:
    def __init__(self, x):
        self.x = x
        
    @property    
    def x(self):
        """Docstring 'x'"""
        return self.__x
        
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    @x.deleter    
    def x(self):
        del self.__x
        print('x deleted')


p = P(12)
p.x = 42
print(p.x)
del p.x

q = Q(13)
q.x = 43
print(q.x)
del(q.x)