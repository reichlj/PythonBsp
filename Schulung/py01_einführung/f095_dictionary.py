tel = {'moe':'0000', 'ned':'8904', 'homer':'3223'}
print(tel)
print(tel['moe'])

numbers = {}
numbers['one'] = 'eins'
numbers['two'] = 'zwei'
numbers['three'] = 'drei'
print(numbers)

prices = {'milk': 1.29, 'butter': 1.79, 'egg': 1.99}
print(prices)
print(prices['milk'])
prices['bananas'] = 2.99
print(prices)
print(prices.get('apples'))
print(prices.get('apples',3.49))
print(prices.get('bananas',3.49))
