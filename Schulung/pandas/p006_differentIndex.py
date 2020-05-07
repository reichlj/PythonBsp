import pandas as pd

fruits1 = ['peaches','oranges','cherries','pears']
fruits2 = ['raspberries','oranges','cherries','pears']
S1 = pd.Series([20, 33, 52, 10], index=fruits1)
S2 = pd.Series([17, 13, 31, 32], index=fruits2)
print(S1+S2)
