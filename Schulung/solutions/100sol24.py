def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__

    return helper

@call_counter
def succ(x):
    return x + 1

print(succ.calls)

s = 0
for i in range(10):
    s += succ(i)
    
print(succ.calls)
