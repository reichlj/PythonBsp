class OrientationError:
    pass

class Robot:
    def __init__(self, name, pos, orientation):
        self.name = name
        self.pos = pos
        self.orientation = orientation

    def __str__(self):
        return self.name + ' , x=' + str(self.pos[0]) + ' y=' + str(self.pos[1]) + ', ' + self.orientation

    def __repr__(self):
        return self.__class__.__name__ + '("' + self.name + '",[' + str(self.pos[0]) + ',' + str(self.pos[1]) + '],"'\
               + self.orientation + '")'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[0:10]
        else:
            self.__name = name

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        if orientation in ("east", "west", "north", "south"):
            self.__orientation = orientation
        else:
            raise OrientationError("Wrong orientation: " + orientation)

    def move(self, distance):
        if self.orientation == "east":
            self.pos[1] += distance
        elif self.orientation == "west":
            self.pos[1] -= distance
        elif self.orientation == "north":
            self.pos[0] += distance
        elif self.orientation == "south":
            self.pos[0] -= distance



r = Robot("Otto", [3,7], "east")
print(r)
print(repr(r))
t =eval(repr(r))

r.move(10)
print(r)
r.name = 'Gustav'
print(r)
r.name = 'GustavGustav'
print(r)
r.orientation='west'
print(r)
r.move(11)
print(r)
print(r.__dict__)
print(r.__dir__())

