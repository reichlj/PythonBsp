class Roboter():

    def __init__(self, name):
        print(name + ' wurde erschaffen!')
        self.name = name
    def __del__(self):
        print(self.name + ' sagt bye-bye')
        print('Es gibt '+ self.name + ' ihn nun nicht mehr!')

if __name__ == '__main__':
    x = Roboter('Tik-Tok')
    y = Roboter('Jenkins')
    z = x
    print('Deleting x')
    del x
    print('Deleting z')
    del z
    del y
