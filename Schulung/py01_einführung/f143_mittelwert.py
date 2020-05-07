def mittelwert(*values):
    if len(values) == 0:
        return None
    else:
        summe = 0
        for value in values:
            summe +=value
        return summe/len(values)
    
print(mittelwert()) 
print(mittelwert(2))  
print(mittelwert(2,3))
print(mittelwert(2,3,4))  
