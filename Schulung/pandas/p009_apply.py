import pandas as pd
import numpy as np

fruits = ['peaches','oranges','cherries','pears']
S = pd.Series([20, 33, 52, 10], index=fruits)
print(S.apply(np.sin))
print(S.apply(lambda x: x if x>50 else x+10))