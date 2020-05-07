def chain(*iterables):
    """ This generator is equivalent 
        to the chain
        method of iterables  """
    for iterable in iterables:
        for element in iterable:
            yield element

names1 = ["Pete", "Tom"]
names2 = ["Tom", "Oscar"]        
c = chain(names1, names2)
for el in c:
    print(el)
