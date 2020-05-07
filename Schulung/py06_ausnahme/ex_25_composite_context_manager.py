from contextlib import contextmanager

@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)
    
with tag('body') as b:
    with tag('p') as p:
        print('Just some text!')
