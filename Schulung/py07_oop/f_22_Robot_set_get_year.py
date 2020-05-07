class Robot:
    def __init__(self,name=None, year=None):
        self.name = name
        self.build_year = year

    def say_hi(self):
        if self.name:
            print('Hi, I am ' + self.name)
        else:
            print('Hi, I am a robot without a name')
            
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
        
    def set_build_year(self, build_year):
        self.build_year = build_year

    def get_build_year(self):
        return self.build_year


x = Robot('Henry',2008)

y = Robot()
y.set_name(x.get_name())
print(x.get_name(),x.get_build_year())

