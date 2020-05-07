import pandas as pd

city_index= [ ['Vienna']*3 + ['Hamburg']*3 + ['Berlin']*3,
              ['country','area','population']*3 ]

data =[ 'Austria', 414.60,1805681,
        'Germany', 755.00, 1760433,
        'Germany', 891.85, 3562166]

data = pd.Series(data,index=city_index)

print(data)
print('unstack level=0')
print(data.unstack(level=0))
print('unstack level=1')
print(data.unstack(level=1))
print('unstack level=-1')
print(data.unstack(level=-1))