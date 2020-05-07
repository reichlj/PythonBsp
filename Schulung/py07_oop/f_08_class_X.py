class X(object):
    pass

x = X()
print(type(x))
print(x.__class__)

class Y(object):
    pass

y = Y()
print(type(y))
print(y.__class__)

import f_07_robot
z = f_07_robot.Robot()
print(type(z))
print(z.__class__)

print(dir(y))
