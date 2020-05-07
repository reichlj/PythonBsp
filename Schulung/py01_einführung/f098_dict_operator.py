numbers = {}
numbers['one'] = 'eins'
numbers['two'] = 'zwei'
numbers['three'] = 'drei'
print(numbers)
print(len(numbers))
del numbers['two']

print('one' in numbers)
print('two' in numbers)

print('one' not in numbers)
print('two' not in numbers)
