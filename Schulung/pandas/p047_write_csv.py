import pandas as pd

pd.set_option('display.width',1000)
column_names = ['Country'] + list(range(2002,2013))
male_pop =pd.read_csv('countries_male_population.csv', 
                      header=None,
                      index_col=0, 
                      names=column_names)
female_pop =pd.read_csv('countries_female_population.csv', 
                        header=None,
                        index_col=0, 
                        names=column_names)
population = male_pop + female_pop
print(population)
population.to_csv('countries_total_population.csv')
