def city_generator():
    cities = ["Hamburg", "München", "Stuttgart", "Zürich"]
    while True:
        city = cities.pop(0)
        yield city
        cities.append(city)

def gen_n(gen, n):
    my_city_gen = gen()
    for k in range(0, n):
        yield next(my_city_gen)

if __name__ == "__main__":
    g = gen_n(city_generator, 8)
    for city in g:
        print("Stadt: " + city)
