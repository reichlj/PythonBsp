fibo = [0,1,1,2,3,5,8,13,21,34,55,89]
iter = filter(lambda x: x%2 == 0,fibo)
print(type(iter))
print(list(iter))
