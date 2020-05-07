import pandas as pd

dr = pd.date_range('2017-06-30','2017-07-08',
                   freq='D')
T = [23.4,24.7,27.1,25.8,23.4,28.1,32.3,35.8,38.0]

temperatures = pd.Series(T,index=dr)
print(temperatures)
