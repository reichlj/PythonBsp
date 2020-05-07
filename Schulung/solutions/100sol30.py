import random

def random_ones_and_zeros():
    p = random.random()
    while True:
        x = random.random()
        message = yield 1 if x < p else 0
        if message != None:
            p = message
        
x = random_ones_and_zeros()
next(x)  # not interested in the return value
for p in [0.2, 0.8]:
    x.send(p)
    print("\nprobabiliy: " + str(p))    
    for i in range(15):
        print(next(x), end=" ")
