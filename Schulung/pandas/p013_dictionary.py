import pandas as pd

cities = {'London': 8615246,
          'Berlin': 3562166,
          'Madrid': 3165235,
          'Rome':   2874038,
          'Paris':  2273305}
          
city_series = pd.Series(cities)
print(city_series)

print('Berlin' in cities)
print('Berlin' in city_series)
