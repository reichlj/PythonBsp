import pandas as pd

fruits = ['peaches','oranges','cherries','pears']
S = pd.Series([25, 33, 52, 29], index=fruits)

Sneu=S>30
print(Sneu)
Sneu=S[S>30]
print(Sneu)