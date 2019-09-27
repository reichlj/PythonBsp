import numpy as np
v = np.arange(0,11)
print(v)
ungerade = v[1::2]
print(ungerade)
umgekehrt=v[::-1]
print(umgekehrt)
print(np.may_share_memory(v,ungerade))
print(np.may_share_memory(v,umgekehrt))
a=np.array([1,2,3,4,5])
b=a[1:4]
b[0]=200
print(a[1])
