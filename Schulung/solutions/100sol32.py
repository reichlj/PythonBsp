from random import randint, seed

def random_ascending_lists(length, value_range=(1,100), secret_key = 0):
    seed(secret_key)
    counter = 0
    while True:
        seq = [randint(*value_range) for _ in range(length)]
        counter += 1
        if seq == sorted(seq):   
            new_secret_key = (yield (counter, secret_key, seq))
            if new_secret_key:
                secret_key = new_secret_key
                seed(secret_key)

numbers = 7
range_of_values = (1, 100)
alists = random_ascending_lists(numbers, range_of_values, 42) 
for i in range(10):
    print(next(alists))
