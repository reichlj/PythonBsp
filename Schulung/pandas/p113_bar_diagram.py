import pandas as pd

data =[100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data,index=range(len(data)))
s.plot(kind='bar', rot=90)