from contextlib import contextmanager

@contextmanager
def tag(name):
    print('<%s>' % name)
    yield  42
    print('</%s>' % name)
    
with tag('h1') as r:
    print('My string and the return value: ',r)
