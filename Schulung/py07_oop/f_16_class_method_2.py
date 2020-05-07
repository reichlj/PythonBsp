class Robot:
    def say_hi(self):
        print('Hi, I am ' + self.name)

x = Robot()
x.name = 'Marvin'
x.say_hi()
Robot.say_hi(x)
y = Robot()
y.name = 'Caliban'
y.say_hi()

Robot.say_hi(x)
Robot.say_hi(y)

