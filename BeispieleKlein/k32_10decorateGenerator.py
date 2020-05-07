from functools import wraps

def get_ready(gen):
    """
    gets a generator gen ready by advancing it to first yield statement
    """
    #@wraps
    def generator(*args, **kwargs):
        g = gen(*args, **kwargs)
        next(g)
        return g
    return generator

@get_ready
def infinite_looper(objects):
    count = -1
    message = yield None
    while True:
        count +=1
        if message != None:
            count = 0 if message < 0 else message
        if count >= len(objects):
            count = 0
        message = yield objects[count]

x = infinite_looper('abcdef')
print(x.send(3))
print('nach send')
print(next(x))
print(next(x))
print(next(x))
