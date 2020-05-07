import pandas as pd

df = pd.read_csv('temperatures.csv',
                 sep=';',
                 decimal=',')
print(df.head())
print('----------mean-------------------')
print(df.mean())
