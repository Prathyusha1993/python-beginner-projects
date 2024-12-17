# it si a fun number guessing challenge that tests your loagical thinking
# need to guess random 4 generated number
#  after each guess feedback in form of cows and bulls
# bull means you guessed thr right digit in right spot
# while cow means the digit is correct but in wrong spot.

import random


def generate_secret():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join([str(digit) for digit in digits[:4]])


def calculate_cows_bulls(secret, guess):
    bulls = sum([1 for i in range(4) if guess[i] == secret[i]])
    cows = sum([1 for i in range(4) if guess[i] in secret]) - bulls

    return cows, bulls


def main():
    secret = generate_secret()
    print('I have generated a 4-digit number with unique digits. Try to guess it!')

    while True:
        guess = input('Guess: ')
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            cows, bulls = calculate_cows_bulls(secret, guess)
            print(f'{cows} cows, {bulls} bulls')

            if bulls == 4:
                print('Congratulations! you guessed the correct number')
                break
            else:
                print('Invalid guess.please enter a 4-digit number with unique digits.')


main()