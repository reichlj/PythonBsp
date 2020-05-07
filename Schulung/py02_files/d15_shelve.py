import shelve

d = shelve.open('test.shelve')
print(type(d),d)
d['a'] = [23, 1.2, 'Strings possible', [34,18]]
d['b'] = {'1':'eins', '2':'zwei'}
for el in d:
    print(el, d[el])
d.close() # auf d kann man nicht mehr zugreifen

d = shelve.open('test.shelve')
for el in d:
    print(el, d[el])
