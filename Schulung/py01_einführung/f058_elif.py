temperature = int(input('Temperatur: '))
if temperature < -20:
    print('Stay at home')
else:
    if temperature < -10:
        print('need warm clothes')
    else:
        if temperature < 0:
            print('Still very cold')
        else:
            if temperature < 10:
                print('not freezing')
            else:
                print('okay')
                
temperature = int(input('Temperatur: '))
if temperature < -20:
    print('Stay at home')
elif temperature < -10:
    print('need warm clothes')
elif temperature < 0:
    print('Still very cold')
elif temperature < 10:
    print('not freezing')
else:
    print('okay')