import numpy as np

dt = np.dtype([('country', 'S20'),
               ('density', 'i4'),
               ('area', 'i4'),
               ('population', 'i4')])
population_table = np.array([('1-Netherlands', 393, 41526, 16928800),
('United Kingdom', 256, 243610, 62262000),
('Germany', 233, 357021, 81799600),
('Italy', 192, 301230, 59715625),
('France', 111, 547030, 63601002),
('Austria', 97, 83858, 8169929),
('Greece', 81, 131940, 11606813),
('Norway', 13, 385252, 5033675)],
             dtype=dt)
print(population_table)
dt = np.dtype([('country', np.unicode, 20),
               ('density', 'i4'),
               ('area', 'i4'),
               ('population', 'i4')])
population_table = np.array([('2-Netherlands', 393, 41526, 16928800),
('United Kingdom', 256, 243610, 62262000),
('Germany', 233, 357021, 81799600),
('Italy', 192, 301230, 59715625),
('France', 111, 547030, 63601002),
('Austria', 97, 83858, 8169929),
('Greece', 81, 131940, 11606813),
('Norway', 13, 385252, 5033675)],
             dtype=dt)
print(population_table)
np.savetxt("population_table.csv",
           population_table,
           fmt="%s;%d;%d;%d",
           delimiter=";")
x = np.genfromtxt("population_table.csv",
               dtype=dt,
               delimiter=";")
print(x)
