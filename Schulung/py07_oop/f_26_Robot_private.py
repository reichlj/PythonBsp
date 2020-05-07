class Robot:
    def __init__(self,name=None, year=2000):
        self.__name = name
        self.__build_year = year

    def say_hi(self):
        if self.__name:
            print('Hi, I am ' + self.__name)
        else:
            print('Hi, I am a robot without a name')
            
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
        
    def set_build_year(self, build_year):
        self.__build_year = build_year

    def get_build_year(self):
        return self.__build_year


x = Robot('Henry',2008)

y = Robot()
y.set_name(x.get_name())
print(x.get_name(),x.get_build_year())

