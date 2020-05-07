temp = (36.5, 37, 37.5, 39, 29.8, 27.3, 25.9)
print([1.8*t+32 for t in temp])
print(list( map(lambda t : 1.8*t+32, temp) ))

print([t for t in temp if t >=30])
print(list( filter(lambda t : t>30,temp) ))

print([1.8*t+32 for t in temp if t >= 30])
print(list(map(lambda t: 1.8*t+32, filter(lambda t: t>30, temp))))
    