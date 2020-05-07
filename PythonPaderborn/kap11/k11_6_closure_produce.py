def odd_production(start,incr):
    value = start - 2
    def nextodd():
        nonlocal value
        value += incr
        return value
    return nextodd

odd11 = odd_production(11,2)
for i in range(5):
    print(i,odd11())
odd21 = odd_production(21,3)
for i in range(5):
    print(i,odd21())

