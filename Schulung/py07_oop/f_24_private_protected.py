class A:
    def __init__(self):
        self.__priv = 'I am private'
        self._prot = 'I am protected'
        self.pub = 'I am public'

if __name__ == '__main__':
    x = A()
    print(x.pub)
    x.pub = x.pub + ' and my value can be changed' 
    print(x.pub)
    
    print(x._prot)
    x._prot = x._prot + ' and my value can be changed' 
    print(x._prot)
    
    print(x.__priv)

