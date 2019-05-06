import numpy as np
Pixel = np.dtype(np.uint8)
print(Pixel)
lst = [ [115, 230.9, 229.2, 234],
        [117, 229, 232.1, 235],
        [116, 140, 141, 142] ]
A = np.array(lst, dtype=Pixel)
print(A)

dt = np.dtype([('country', 'S20'),
               ('density', 'i4'),
               ('area', 'i4'),
               ('population', 'i4')])
population_table = np.array([('Netherlands', 393, 41526, 16928800),
('Belgium', 337, 30510, 11007020),
('United Kingdom', 256, 243610, 62262000),
('Germany', 233, 357021, 81799600),
('Liechtenstein', 205, 160, 32842),
('Italy', 192, 301230, 59715625),
('Switzerland', 177, 41290, 7301994),
('Luxembourg', 173, 2586, 512000),
('France', 111, 547030, 63601002),
('Austria', 97, 83858, 8169929),
('Greece', 81, 131940, 11606813),
('Ireland', 65, 70280, 4581269),
('Sweden', 20, 449964, 9515744),
('Finland', 16, 338424, 5410233),
('Norway', 13, 385252, 5033675)],
             dtype=dt)
print(population_table[:4])

print(population_table['density'])
print(population_table['country'])
print(population_table['area'][2:5])

s = population_table['country'][0]
print(s, type(s))
s = str(s)
print(s, type(s))
