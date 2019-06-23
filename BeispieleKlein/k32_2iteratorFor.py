cities = ["Hamburg", "Berlin", "München", "Zürich"];
for city in cities:
    print("Stadt ", city)

print('Mit Iterator:')
cityIterator = iter(cities);
print(type(cityIterator))
while True:
    try:
        city = next(cityIterator)
        print('Stadt ', city)
    except StopIteration:
        break


