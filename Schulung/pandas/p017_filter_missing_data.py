import pandas as pd

cities = {'London': 8615246.0,
          'Paris':  2273305.0,
          'Berlin': 3562166.0,
          'Hamburg': 1760433.0
          }
my_cities = ['London', 'Paris', 'Zürich', 'Berlin', 
             'Stuttgart', 'Hamburg' ]          
my_city_series = pd.Series(cities, index=my_cities)
drop_series = my_city_series.dropna()
print(drop_series)

missing_cities = {'Stuttgart': 597939, 'Zürich': 378884}

new_series = my_city_series.fillna(missing_cities)
print(new_series)
