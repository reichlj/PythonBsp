import numpy as np
A = np.genfromtxt("data/shop_sales_figures_extended.txt", usecols=(1,3,4), dtype=None)
A
A1 = A[1:,:].astype(np.float)
A1.sum(axis=0)
