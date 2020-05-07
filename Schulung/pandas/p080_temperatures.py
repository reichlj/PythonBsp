import pandas as pd

df = pd.read_csv('temperatures.csv',
                 sep=';',
                 decimal=',')
print(df[:3])
