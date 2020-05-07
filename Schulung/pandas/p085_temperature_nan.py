import pandas as pd

temps_with_NaN = pd.read_csv('temperatures_with_NaN.csv',
                            index_col=0)

print(temps_with_NaN[:5])