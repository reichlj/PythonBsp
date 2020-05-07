fobj = open('yellow_snow.txt')
for line in fobj:
    print(line.rstrip())
fobj.close()

fileHandle = open('yellow_snow.txt')
char = fileHandle.read(1)
while char:
    print(char,end='')
    char = fileHandle.read(1)
fileHandle.close()

        
