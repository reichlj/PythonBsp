import pandas as pd

fruits = ['apples','oranges','cherries','pears']
quantities = [20, 33, 52, 10]
S1 = pd.Series(quantities, fruits)
print('-----S1:-----')
print(S1)
S2 = pd.Series([17,13,31,32], fruits)
print('-----S2:-----')
print(S2)
print('-----S1 + S2:-----')
print(S1+S2)
