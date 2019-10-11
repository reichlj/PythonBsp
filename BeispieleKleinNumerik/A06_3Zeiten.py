import numpy as np

zeit_type = np.dtype([('h', np.int32), ('min', np.int32), ('sec', np.int32)])

zeiten = np.array([(2,12,22), (3,13,23), (4,42,42)], dtype=zeit_type)
print(zeiten)
