import pandas as pd

fruits = ['apples','oranges','cherries','pears']
quantities = [20,33,52,10]
s = pd.Series(quantities,index=fruits)
s.plot()
