a = [1,2,3,4]
b = [17,12,11,10] 
c = [-1,-4,5,9]
 
print(list(map(lambda x,y:x+y,a,b)))
print(list(map(lambda x,y,z:x+y+z,a,b,c)))
print(list(map(lambda x,y,z:x+y-z,a,b,c)))

    