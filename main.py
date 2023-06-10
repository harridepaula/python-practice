import random
max_number = 100
secret_number = random.randint(1, max_number)
guess_count = 0
while True:
    guess = int(input(f'Guess a number between 1 and {max_number}: '))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    elif guess < 0 and guess > 100:
        print("Enter a number between 1 and 100")
    else:
        print(f'You won with {guess_count} guesses!')
        break
    guess_count += 1
