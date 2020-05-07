class Robot(object):
    pass

x = Robot()
Robot.brand = 'Kuka'
print('01 type(x)    :', type(x))
print('02 type(Robot):', type(Robot))
print('03 x.brand    :', x.brand)
print('04 Robot.brand:', Robot.brand)

x.brand = 'Thales'
print('05 x.brand    :', x.brand)
print('06 Robot.brand:', Robot.brand)

y = Robot()
print('07 y.brand    :', y.brand)

Robot.brand = 'Thales'
print('08 x.brand    :', x.brand)
print('09 y.brand    :', y.brand)

print('10 x.__dict__ :', x.__dict__)
print('11 y.__dict__ :', y.__dict__)
print('12 Robot_dict :', Robot.__dict__)

