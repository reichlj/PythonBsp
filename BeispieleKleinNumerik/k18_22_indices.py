import pandas as pd

fruits = ['apples', 'oranges', 'cherries', 'pears']
S = pd.Series([20, 33, 52, 10], index=fruits)
print(S['apples'])
print(S[['apples','oranges','cherries']])
print(S[S>30])
