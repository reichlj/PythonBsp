def city_generator():
    cities = ["Hamburg", "München", "Stuttgart", "Zürich"]
    for city in cities:
        yield city

gen = city_generator()
for city in gen:
    print("Stadt " + city)



