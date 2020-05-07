def fahrenheit(T):
    return float(9)/5*T +32
def celsius(T):
    return float(5)/9*(T - 32)
    
temp = (36.5, 37, 37.5, 39)
print('Fahrenheit')
print(list(map(fahrenheit,temp)))

print('Celsius')
ctemp = map(fahrenheit,temp)
print(list(map(celsius,ctemp)))
   