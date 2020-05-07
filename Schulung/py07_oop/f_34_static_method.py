class Robot:

    @staticmethod
    def hi():
        print('Hi')

    def hi1(self):
        print('Hi1')

    def hi2():
        print('Hi2')


x = Robot()

Robot.hi()
x.hi()
Robot.hi2()
x.hi1()
