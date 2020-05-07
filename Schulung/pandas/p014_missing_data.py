import pandas as pd

cities = {'London': 8615246,
          'Berlin': 3562166,
          'Madrid': 3165235,
          'Rome':   2874038,
          'Paris':  2273305}
my_cities = ['London', 'Paris', 'Zürich', 'Berlin', 
             'Stuttgart', 'Hamburg' ]          
city_series = pd.Series(cities,index=my_cities)
print(city_series)
