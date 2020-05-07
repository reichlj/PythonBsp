import pandas as pd

pop = pd.read_csv("countries_population.csv",
                  header=None,
                  names=['Country','Population'],
                  index_col=0,
                  quotechar="'",
                  sep=" ",
                  thousands=",")
print(pop)
