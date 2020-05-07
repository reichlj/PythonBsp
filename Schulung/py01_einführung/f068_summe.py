n = 100
s = 0
i = 1
while i <= n:
    s +=i
    i += 1
    
print('Summe von 1 bis '+ str(n) + ': ' + str(s))

s = sum(range(101))
print('Summe von 1 bis '+ str(n) + ': ' + str(s))
