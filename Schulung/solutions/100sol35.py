def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element
        
numbers = cycle("abcde")
for _ in range(12):
    print(next(numbers), end=", ")
