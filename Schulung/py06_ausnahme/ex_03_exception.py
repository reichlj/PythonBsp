while True:
    try:
        zahl = input('Zahl eingeben: ')
        zahl = int(zahl)
        break
    except ValueError as e:
        print('ValueError: ',e)
        print('Keine korrekte Integerzahl!')
        
print(zahl)

count = 0
weiter = True
while weiter:
    try:
        zahl = input('Zahl eingeben: ')
        zahl = int(zahl)
        weiter = False
    except ValueError as e:
        print('ValueError: ',e)
        print('Keine korrekte Integerzahl!')
    count += 1
    print(count, weiter)
        
print(zahl)