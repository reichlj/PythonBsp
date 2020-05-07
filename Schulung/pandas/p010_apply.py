import pandas as pd
import numpy as np

index1 = ['Monday','Tuesday','Wednesday','Monday']
index2 = ['Monday','Tuesday','Thursday','Friday']
s1 = pd.Series([10, 12, 8, 7], index = index1)
s2 = pd.Series([9, 4, 1, 11], index = index2)
print('s1',s1)
print('s2',s2)
s = s1.add(s2, fill_value = 0)  # in index1 kommt Monday zweimal vor
print('s',s)
s = s.apply(int)
print(s)
# ohne fill_value
s1 = pd.Series([10, 12, 8, 7], index = index1)
s2 = pd.Series([9, 4, 1, 11], index = index2)
s = s1.add(s2)
print(s)

