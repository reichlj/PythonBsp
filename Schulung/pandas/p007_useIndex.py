import pandas as pd

fruits = ['peaches','oranges','cherries','pears']
S = pd.Series([20, 33, 52, 10], index=fruits)
for fruit in fruits:
    print(S[fruit])

print('----------------')
print(S[['peaches','pears','oranges']])