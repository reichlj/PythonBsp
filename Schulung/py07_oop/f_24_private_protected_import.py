from f_24_private_protected import *

x = A()
print(x.pub)
x.pub = x.pub + ' and my value can be changed' 
print(x.pub)
   
print(x._prot)
x._prot = x._prot + ' and my value can be changed' 
print(x._prot)
    
print(x._A__priv)
#print(x.__priv)
print(dir())
print(dir(x))

