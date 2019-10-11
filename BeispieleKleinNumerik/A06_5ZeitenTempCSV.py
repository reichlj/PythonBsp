import numpy as np

zeit_type = np.dtype([('h', np.int32), ('min', np.int32), ('sec', np.int32)])

zeit_temp_type = np.dtype([('time', zeit_type), ('t',np.float)])

zeit_temp = np.array([((2,12,22),12.5), ((3,13,23),13.5), ((4,42,42),14.5)], dtype=zeit_temp_type)

with open("zeit_tmp.csv","w") as fh:
    for entry in zeit_temp:
        fh.write(f"{entry['time']['h']:2d}:{entry['time']['min']:2d}:{entry['time']['sec']:2d} {entry['t']:f}\n")
