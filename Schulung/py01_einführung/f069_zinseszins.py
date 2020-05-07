kap0 = float(input('Startkapital: '))
zinssatz = float(input('Zinssatz: '))
jahre = int(input('Anzahl der Jahre: '))

k = 0
kap = kap0
while k < jahre:
    kap = kap*(1.0 + zinssatz/100)
    k += 1
    
print('Kapital nach ' + str(jahre) + ' Jahren: ' + str(kap))