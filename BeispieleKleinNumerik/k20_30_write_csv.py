import pandas as pd

column_names = ['Country'] + list(range(2002,2013))
male_pop =pd.read_csv('countries_male_population.csv', header=None,index_col=0, names=column_names)
female_pop =pd.read_csv('countries_female_population.csv', header=None,index_col=0, names=column_names)
population = male_pop + female_pop
print(population)

pop_complete = pd.concat([population,male_pop,female_pop],keys=['total','male','female'])
print(pop_complete.iloc[[0,1,2,29,30,31,32,59,60,61,62]])

df = pop_complete.swaplevel()
df.sort_index(inplace=True)
print(df.head(12))

df.to_csv('countries_total_population.csv')
