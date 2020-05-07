print([(i,j) for i in range(1,7) for j in range(1,7)])

dir = {'DE':'Deutschland', 'FR':'Frankreich'}
print(dict([(item[1],item[0]) for item in dir.items() ]))
print(dict((dir[k],k) for k in dir))