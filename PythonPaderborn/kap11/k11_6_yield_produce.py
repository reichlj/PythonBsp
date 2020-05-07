def odd_production(start,incr):
    while True:
        yield start
        start += incr

for i, k in zip(range(5),odd_production(11,2)):
    print(i,k)

gen = odd_production(13,3)
for i, k in zip(range(5),gen):
    print(i,k)

