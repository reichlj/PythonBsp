import pandas as pd

wechselkurse = { 'GBP': 0.9124, 'JPY': 120.33, 'USD': 1.1034, 
       'AUD': 1.6108, 'CNY': 7.6113, 'CHF': 1.0979, 'EUR': 1.00 }

s1 = pd.Series(wechselkurse)
s2 = s1.apply(lambda x: x/s1['CHF'] )
df = pd.concat([s1,s2],axis=1)
print(df)