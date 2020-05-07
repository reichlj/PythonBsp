class A:
    __priv = 'I am private class'
    _prot = 'I am protected class'
    pub = 'I am public class'

if __name__ == '__main__':
    print(A.pub)
    A.pub = A.pub + ' and my value can be changed' 
    print(A.pub)
    
    print(A._prot)
    A._prot = A._prot + ' and my value can be changed' 
    print(A._prot)
    
    print(A.__priv)

