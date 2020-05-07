colors = ['red']
for k in colors:
    if k == 'red':
        colors += ['black']
    if k == 'black':
        colors += ['white']
print(colors)

colors = ['red']
for k in colors[:]:
    if k == 'red':
        colors += ['black']
    if k == 'black':
        colors += 'white'
print(colors)

colors = ['red']
print(id(colors))
print(id(colors[:]))

colors = ['red']
count = 0
for k in colors:
    count += 1
    print('count=', count, k)
    if k == 'red':
        colors.insert(0,'black')
print(colors)
