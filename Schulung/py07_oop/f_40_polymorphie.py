class NN:

    def abc(self, x):
        print('ein Argument:', x)

    def abc(self, x, y):
        print('zwei Argument:', x, y)

nn = NN()
try:
    nn.abc(5)
except Exception as e:
    print("Aufruf von abc(x)",e)
nn.abc(5,15)
