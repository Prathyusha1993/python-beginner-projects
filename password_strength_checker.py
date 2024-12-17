# strength of password like length, uppercase, number, special characters.
# categorize as very weak, weak, medium strong or very strong

import re


def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search('[a-z]', password):
        strength += 1
    if re.search('[A-Z]', password):
        strength += 1
    if re.search('[0-9]',password):
        strength += 1
    if re.search('[@#$%+=!]', password):
        strength += 1

    return strength


def main():
    password = input('Enter a Password: ')
    strength = check_password_strength(password)

    if strength == 5:
        print('Password strength: very strong')
    elif strength == 4:
        print('Password strength: strong')
    elif strength == 3:
        print('Password strength: medium')
    elif strength == 2:
        print('Password strength: weak')
    else:
        print('Password strength: very weak')


main()