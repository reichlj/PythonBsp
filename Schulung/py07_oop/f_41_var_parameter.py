class NN:
    def abc(self, *args):
        if len(args) == 1:
            if type(args[0]) == int:
                print('args=1 - int')
            elif type(args[0]) == float: 
                print('args=1 - float')
        elif len(args) == 2:
            print('args=2')
        else:
            print('args=3')
            
        
x = NN()
x.abc()
x.abc(1)
x.abc(1.2)
x.abc(1,2)
x.abc(1,2,3)