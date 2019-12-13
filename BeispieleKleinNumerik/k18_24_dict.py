import pandas as pd

cities = {'Munich': 1493900,
          'London': 8615246,
          'Vienna': 1805681 }
          
city_series = pd.Series(cities)
print(city_series)