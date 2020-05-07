  
temp = (36.5, 37, 37.5, 39)

ctemp = map(lambda x : 1.8*x + 32, temp)
print('Fahrenheit')
for k in ctemp:
   print(k)
   
ctemp = map(lambda x : 1.8*x + 32, temp)
print('Celsius')
for k in map(lambda x : 5.0/9.0*(x-32),ctemp):
   print(k)
    