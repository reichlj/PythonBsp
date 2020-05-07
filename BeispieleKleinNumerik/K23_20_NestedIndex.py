import pandas as pd

cities = ['Vienna', 'Vienna', 'Vienna',
          'Hamburg', 'Hamburg', 'Hamburg',
          'Berlin', 'Berlin', 'Berlin',
          'Zürich', 'Zürich', 'Zürich']
index = [cities, ['country', 'area', 'population',
                  'country', 'area', 'population',
                  'country', 'area', 'population',
                  'country', 'area', 'population']]
data = ['Austria',     414.6,  1805681,
        'Germany',     755,    1760433,
        'Germany',     891.85, 3562166,
        'Switzerland', 87.88,   378884]

city_series = pd.Series(data, index=index)
print(city_series)