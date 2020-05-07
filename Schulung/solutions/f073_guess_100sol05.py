import random
n = 20
to_be_guessed = int(n * random.random()) + 1
# or equivalently
# to_be_guessed = random.randint(1,n)
import random
n = 20
to_be_guessed = random.randint(1,n)

guess = int(input("Your guess: "))
while guess != to_be_guessed:
    if guess > to_be_guessed:
        print("Number is too large")
    elif guess < to_be_guessed:
        print("Number is too small")
    guess = int(input("Your new guess: "))
print("You got it!")
import random
n = 20
to_be_guessed = random.randint(1,n)

while True:
    guess = int(input("Your guess: "))
    if guess > to_be_guessed:
        print("Number is too large")
    elif guess < to_be_guessed:
        print("Number is too small")
    if guess == to_be_guessed:
        break
print("You got it!")
