cities = ["Hamburg", "München", "Stuttgart", "Zürich"]
iterator = iter(cities)
while True:
    try:
        city = next(iterator)
    except StopIteration:
        break
    print("Stadt " + city)
