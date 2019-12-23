import pandas as pd

S = pd.Series([20, 33, 52, 10])
print(S.apply(lambda x: x if x > 50 else x+10))

S = pd.Series([20, 33, 52, 10])
print(S.apply(lambda x: x if x > 50 else x+args[0]),5)