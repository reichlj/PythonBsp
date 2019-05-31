best =[ [3456, (34587, 'Learning', 4, 40.95), (98762, 'Programm', 5, 56.80), (77226, 'Head', 3, 32.95)],
        [3457, (34587, 'Learning', 4, 40.95), (98762, 'Programm', 4, 56.80), (77226, 'Head', 3, 32.95)],
        [3458, (34587, 'Learning', 2, 1.), (98762, 'Programm', 2, 2), (77226, 'Head', 1, 3)]
      ]

print(best)
mylambda = lambda ele: ele[2]*ele[3]
p = sum(list(map(mylambda, best[2][1:])))
print(p)
liste = [sum(list(map(mylambda, best[2][1:])))]
print(liste)
preis = map(lambda x: x if x>100 else x+10, [sum(list(map(mylambda, best[2][1:])))])
print((best[2][0], list(preis)[0]))

preise = lambda entry : (entry[0], list(map(lambda preis: preis if preis > 100 else preis + 10, [sum(list(map(mylambda, entry[1:])))]))[0])
print(list(map(preise,best)))
