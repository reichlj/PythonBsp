from operator import itemgetter
p = [('Peter',114,3467.87),
     ('Eve',117,3100.03),
     ('Bill',105,7239.34),
     ('Stella',125,3983.45)]
print('itemgetter: 2 0 1')
sorted_list = sorted(p,key=itemgetter(2,0,1))
for item in sorted_list:
    print(item)
print('itemgetter: 2 1 0')
sorted_list = sorted(p,key=itemgetter(2,1,0))
for item in sorted_list:
    print(item)
print('itemgetter: 1 2 0')
sorted_list = sorted(p,key=itemgetter(1,2,0))
for item in sorted_list:
    print(item)
