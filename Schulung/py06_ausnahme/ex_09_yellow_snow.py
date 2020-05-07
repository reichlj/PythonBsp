arg = 'yellow_snow.txt'
try:
    f = open(arg,'r')
except IOError:
    print('cannot open',arg)
else:
    print(arg, 'has',len(f.readlines()), 'lines')
    f.close()