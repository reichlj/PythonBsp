import random
n = 20
to_be_guessed = random.randint(1,n)

guess =int(input('Your guess: '))
while to_be_guessed != guess:
    if guess > to_be_guessed:
        print('Number is too large')
    elif guess < to_be_guessed:
        print('Number is too small')
    guess = int(input('Your new guess: '))
    
print('You got it!')