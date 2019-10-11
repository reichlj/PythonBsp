import numpy as np

mytype = np.dtype([('ID', np.int32), ('Preis', np.float)])

a1 = np.array([(12, 12.1), (13, 13.1), (14, 14.1)], dtype=mytype)
anzahl = np.array([100,200,300])
einzelpreise = a1['Preis']*anzahl
print(einzelpreise)
print(einzelpreise.sum())
