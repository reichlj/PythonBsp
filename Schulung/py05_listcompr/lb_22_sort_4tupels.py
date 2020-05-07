p = [('Peter',114,42,5526),
     ('Eve',129,37,4302),
     ('Bill',105,42,6000),
     ('Stella',125,36,4320),
     ('Eve',117,37,4744),
     ('Peter',114,41,5395,),
     ('Helen',138,39,4239)]
for item in p:
    print(item)
print('*** Alphabetically')
p.sort()
for item in p:
    print(item)
print('*** Sort : x[2] x[1]')
p.sort(key=lambda x: (x[2], x[1]))
for item in p:
    print(item)
print('*** 1/x[1]*15000*x[2]  x[2]/x[1]')
p.sort(key=lambda x: x[2]/x[1])
for item in p:
    print(item)
