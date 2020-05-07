fobj = open('yellow_snow.txt')

line = 'no line'
while line:
    line = fobj.readline() 
    print(line.rstrip())
    
fobj.close()

        
