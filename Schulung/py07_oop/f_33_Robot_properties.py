class Robot:
    def __init__(self,name=None, year=2000):
        self.name = name
        self.build_year = year

    def say_hi(self):
        if self.name:
            print('Hi, I am ' + self.name)
        else:
            print('Hi, I am a robot without a name')
    
    @property        
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = 'Marvin' if name == 'Henry' else name
        
    @property        
    def build_year(self):
        return self.__build_year
    
    @build_year.setter
    def build_year(self, build_year):
        self.__build_year = 2000 if build_year < 2000 else build_year



x = Robot('Henry',2008)

y = Robot()
y.name = x.name
print(x.name, x.build_year)

