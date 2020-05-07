class Robot(object):
    pass

x = Robot()
y = Robot()
y2 = y
print(x==y)
print(y==y2)
print(id(x))
print(id(y))
