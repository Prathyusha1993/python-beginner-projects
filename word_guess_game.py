# guess a secert word one letter at time.
# word is selected randomly from list
# six attempts to guess word

import random
import re
from mimetypes import guess_extension


def read_words():
    try:
        with open('words.txt','r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print('words.txt file not found')
        return []


def display_word(secret_word, guessed_letter):
    word_to_display = ''

    for letter in secret_word:
        if letter in guessed_letter:
            word_to_display += letter
        else:
            word_to_display += '_'

    print(word_to_display)


def get_guess(guessed_letter):
    while True:
        guess = input('Enter a letter: ').lower()
        if len(guess) != 1:
            print('Enter only one letter.')
        elif not re.search('[a-z]', guess):
            print('Enter only letters from a to z.')
        elif guess in guessed_letter:
            print('You already guessed the letter')
        else:
            return guess


def is_word_guessed(secret_word, guessed_letter):
    for letter in secret_word:
        if letter not in guessed_letter:
            return False
    return True


def main():
   words = read_words()
   if not words:
       print('No words loaded.')
       return
   secret_word = random.choice(words)
   # print(secret_word)

   attempts = 6
   guessed_letter = []
   while attempts > 0:
       display_word(secret_word, guessed_letter)

       guess = get_guess(guessed_letter)
       guessed_letter.append(guess)

       if guess in secret_word:
           print('Good Guess')
           if is_word_guessed(secret_word, guessed_letter):
               print('Congratulations! you guessed the word')
               break
       else:
           print('Wrong guess')
           attempts -= 1
           if attempts == 0:
               print(f'Game over!The word was {secret_word}')


main()