best =[ [34587,'Learning',4,40.95],
        [98762,'Programm',5,56.80],
        [77226,'Head',3,32.95]]
print(best)
mylambda = lambda ele: (ele[0], ele[2]*ele[3])
ergebnis = list(map(mylambda,best))
print(ergebnis)

addlambda = lambda x : x if x[1] > 100 else (x[0], x[1]+10)
ergebnis2 = list(map(addlambda, map(mylambda, best)))
print(ergebnis2)
