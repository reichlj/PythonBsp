ba = 40000000
bb = 70000000
wa = 0.033
wb = 0.019

k= 0
while ba < bb:
    ba = ba*(1.0+wa)
    bb = bb*(1.0+wb)
    k +=1
    
print('Anzahl der Jahre: ' + str(k))
print('Bevölkerung A: ' + str(ba))
print('Bevölkerung B: ' + str(bb))

