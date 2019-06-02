pairs = [(x,y) for x in range(1,7) for y in range(1,7)]
print('pairs : Anzahl={}'.format(len(pairs)))

sieben = [p for p in pairs if p[0]+p[1] == 7]
print('sieben : Anzahl={}'.format(len(sieben)))
print(len(sieben)/len(pairs))

sieben = [p for p in pairs if sum(p) == 7]
print('sieben : Anzahl={}'.format(len(sieben)))
print(len(sieben)/len(pairs))
