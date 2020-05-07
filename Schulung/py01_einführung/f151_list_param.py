def s(liste):
    print('sa:',id(liste))
    liste += [47,11]
    print('sa:',liste)
    print('sb:',id(liste))
    
def s1(liste):
    print('s1a:',id(liste))
    liste = liste + [47,11]
    print('s1a:',liste)
    print('s1b:',id(liste))
    
print('**** in-place ****')    
fib=[0,1,1,2,3]
print('m :',fib)
print('m :',id(fib))
s(fib)
print('m :',id(fib))
print('m :',fib)

print('****  concatenate ****')    
fib=[0,1,1,2,3,5]
print('m :',fib)
print('m :',id(fib))
s1(fib)
print('m :',fib)
print('m :',id(fib))

print('**** copy ****')    
fib=[0,1,1,2,3,5,8]
print('m :',fib)
print('m :',id(fib))
s(fib[:])
print('m :',id(fib))
print('m :',fib)
