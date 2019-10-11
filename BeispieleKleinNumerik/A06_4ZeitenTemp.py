import numpy as np

zeit_type = np.dtype([('h', np.int32), ('min', np.int32), ('sec', np.int32)])

zeit_temp_type = np.dtype([('time', zeit_type), ('t',np.float)])

zeit_temp = np.array([((2,12,22),12.5), ((3,13,23),13.5), ((4,42,42),14.5)], dtype=zeit_temp_type)

print(zeit_temp)
print(zeit_temp['time'])
print(zeit_temp['time']['h'])
print(zeit_temp['t'])

