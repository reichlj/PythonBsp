import pandas as pd

dr = pd.date_range('2017-06-30','2017-07-08',
                   freq='D')
T1 = [23.4,24.7,27.1,
      25.8,23.4,28.1,
      32.3,35.8,38.0]

T2 = [23.8,25.2,27.3,
      25.8,23.8,28.8,
      32.8,34.9,37.9]

ts1 = pd.Series(T1,index=dr)
ts2 = pd.Series(T2,index=dr)
t = round((ts1+ts2)/2,1)
print(t)
