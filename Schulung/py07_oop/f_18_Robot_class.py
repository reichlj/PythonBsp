class Robot:
    def __init__(self,name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print('Hi, I am ' + self.name)
        else:
            print('Hi, I am a robot without a name')

        
x = Robot()
x.say_hi()
Robot.say_hi(x)

y = Robot('Marvin')
y.say_hi()

