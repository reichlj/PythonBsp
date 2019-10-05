class Robot:
    __forbidden_names = {"Henry", "Oscar"}

    def __init__(self, name="Marvin"):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name in Robot.__forbidden_names:
            self.__name = "Marvin"
        else:
            self.__name = name

if __name__ == '__main__':
    r = Robot('my_robot')
    print(r.name)
    r.name='my_robot1'
    print(r.name)
