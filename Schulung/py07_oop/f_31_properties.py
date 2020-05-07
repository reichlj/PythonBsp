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
            
    x = property(__getX,__setX)


class Q:
    def __init__(self, x):
        self.x = x
        
    @property    
    def x(self):
        return self.__x
        
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

p = P(12)
p.x = 42
print(p.x)

q = Q(13)
q.x = 43
print(q.x)