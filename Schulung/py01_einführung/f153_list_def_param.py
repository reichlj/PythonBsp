def spammer(bag=[]):
    bag.append('spam')
    return bag

def spammer1(bag=None):
    if bag==None:
        bag=[]
    bag.append('spam')
    return bag
    
print(spammer())
print(spammer())
print(spammer())

mybag=['a']
print(spammer(mybag))
print(spammer(mybag))

print(spammer1())
print(spammer1())
print(spammer1())

mybag=['a']
print(spammer1(mybag))
print(spammer1(mybag))
