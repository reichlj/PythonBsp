class Robot:
    __forbidden_names = {"Henry", "Oscar"}

    def __init__(self, name="Marvin"):
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self,name):
        if name in Robot.__forbidden_names:
            self.__name = "Marvin"
        else:
            self.__name = name

if __name__ == '__main__':
    r = Robot('my_robot')
    print(r.get_name())
    r.set_name('my_robot1')
    print(r.get_name())

    import A03_3_6_6Properties as m
    print(m.__dict__['Robot'])
    for num, item in enumerate(m.__dict__.items()):
        print("{0:2d} : {1}".format(num, item))
