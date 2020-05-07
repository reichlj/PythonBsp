from f_24_private_protected_class_attr import A

if __name__ == '__main__':
    print(A.pub)
    A.pub = A.pub + ' and my value can be changed' 
    print(A.pub)
    
    print(A._prot)
    A._prot = A._prot + ' and my value can be changed' 
    print(A._prot)
    
    print(A.__priv)

