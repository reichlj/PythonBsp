import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(10),
             index=[['a','a','a','c','c','c','b','b','b','d'],
                    [1, 2, 3, 1, 2, 3, 1, 2, 2, 3] ])
print(data)
print("***** data['a']")
print(data['a'])
print('***** data[:,3]')
print(data[:,3])
print("***** data['a':'c']")

data1 = data.sort_index()
print(data1['a':'c'])

data.sort_index(inplace=True)
print(data['a':'c'])
