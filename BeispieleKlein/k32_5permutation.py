def permutations(items):
    n = len(items)
    if n == 0:
        print('n=0')
        yield []
        print('nach n=0')
    else:
        for i, ele in enumerate(items):
            print('i={0} ele={1}'.format(i,ele))
            for cc in permutations(items[:i]+items[i+1:]):
                print('ele={0} cc={1}'.format(ele,cc))
                yield [ele] + cc
                print('nach [ele] + cc')

for item in permutations(['1']):
    print(''.join(item))
#for item in permutations(['1', '2']):
#    print(''.join(item))
#for item in permutations(['1','2','3']):
#    print(''.join(item))
