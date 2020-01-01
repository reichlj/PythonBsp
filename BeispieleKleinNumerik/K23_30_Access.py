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
#print(city_series)
print(city_series["Vienna"])
print(city_series["Vienna"]["area"])
print(city_series["Vienna", "area"])
city_series = city_series.sort_index()
print("city_series with sorted index")
print(city_series)
print("Slicing the city_series")
print(city_series["Berlin":"Vienna"])
print(city_series[:, 'area'])
for i in range(len(city_series.index.levels)):
    if i == 0:
        print('Oberste Hierarchiestufe')
    elif i == 1:
        print('Untere Hierarchiestufe')
    print(city_series.index.levels[i])

