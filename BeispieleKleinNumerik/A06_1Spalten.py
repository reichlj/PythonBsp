import numpy as np

mytype = np.dtype([('ID', np.int32), ('Preis', np.float)])

a1 = np.array([(12, 12.1), (13, 13.1), (14, 14.1)], dtype=mytype)
print(a1)
print(a1['ID'])
print(a1['Preis'])
print(a1[1])
print(a1[1]['ID'])
print(a1['ID'][1])

print(a1.shape)
