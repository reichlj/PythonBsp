def makedict(**dictargs):
    return dictargs


colors = {'red':1, 'green':2, 'blue':3}
print(colors)
print(makedict(red=1, green=2, blue=3))

colors = dict(red=1, green=2, blue=3)
print(colors)
