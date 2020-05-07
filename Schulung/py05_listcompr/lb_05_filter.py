fib = [0,1,1,2,3,5,8,13,21,34]

def is_even(x):
    return x%2 == 0

result = filter(is_even,fib)
print(list(result))

result = filter(lambda x : x%2 == 0,fib)
print(list(result))


    