class A:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y
    def set_y(self, y):
        self.__y = y
        
a1 = A(3,4)
a2 = A(17,4)
a1.set_x(a2.get_y())