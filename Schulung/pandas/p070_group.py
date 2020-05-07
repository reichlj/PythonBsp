import pandas as pd

s = pd.Series([4,6,6,7,1,3,5],
      index=['Bill','Eve','Bill',
             'Bob','Eve','Bill','Bob'])
s2 = s.groupby(s.index).sum()
print(s2)