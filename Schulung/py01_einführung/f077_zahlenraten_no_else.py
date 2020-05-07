import random
n = 20
to_be_guessed = random.randint(1,n)

resigned = False

guess =int(input('Your guess: '))
while guess != to_be_guessed:
    if guess > 0:
        if guess > to_be_guessed:
            print('Number is too large')
        elif guess < to_be_guessed:
            print('Number is too small')
        guess = int(input('Your new guess: '))
    else:
        print('I am sorry that you gave up!')
        resigned = True
        
if not resigned:
    print('You got it!')

print('Ende')