bikes = ['trek', 'redline', 'giant']

print('Iterator:')
for bike in bikes:
    print(bike)

print('Index:')
for k in range(0,len(bikes)):
    print(bikes[k])

print('Listcomprehension:')
squares = [x*x for x in range(1,11)]
for k in squares:
    print(k)
