def hi(obj):
    print('Hi, I am ' + obj.name)
    
class Robot:
    pass

x = Robot()
x.name = 'Marvin'
hi(x)


class RRobot:
    say_hi = hi
    
    
x = RRobot()
x.name = 'MMarvin'
RRobot.say_hi(x)
x.say_hi()