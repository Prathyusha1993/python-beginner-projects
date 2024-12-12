import random

number_to_guess = random.randint(1, 100)
secret_number = 8
while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))

        if guess > number_to_guess:
            print('Too high!')
        elif guess < number_to_guess:
            print('Too Low')
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print('Please enter a valid number')