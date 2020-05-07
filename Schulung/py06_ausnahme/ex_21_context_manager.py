from contextlib import contextmanager

@contextmanager
def func():
    print('With statement has startet')
    yield
    print('With statement ends now')
    
with func():
    print('Whatever has to be done will be done!')
