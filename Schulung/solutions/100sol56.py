import pandas as pd
fruits = ['peaches', 'oranges', 'cherries', 'pears']
S = pd.Series([25, 33, 52, 29], index=fruits)
S.apply(lambda x: int(x/10)*10)
