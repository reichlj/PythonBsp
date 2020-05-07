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
city_df = pd.DataFrame([], index=index[0])
print(city_df)
for key in index[1][:3]:
    city_df = pd.concat([city_df, city_series[:, key]], axis=1, sort=True)
city_df.set_axis(['country', 'population', 'area'], axis='columns', inplace=True)
print(city_df)

city_df = pd.DataFrame([], index=index[0])
print(city_df)
for key in index[1][:3]:
    city_df = pd.concat([city_df, city_series[:, key]], axis=1, sort=False)
city_df.set_axis(['country', 'population', 'area'], axis='columns', inplace=True)
print(city_df)


city_df = city_series.unstack()
print(city_df)
city_df = city_series.unstack(level=0)
print(city_df)