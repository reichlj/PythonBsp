import sys
print(len(sys.argv))
for i, arg in enumerate(sys.argv):
    print(i, arg)
if len(sys.argv)==1:
    print('Argument erwartet')
elif sys.argv[1]=='-h':
    print('Option -h erkannt')
else:
    print('Unbekannte Option')
