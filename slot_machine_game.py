# player starts with balance, places bets, and spins the reels
# if all three symbols on the reels match, player wins 10times theor bet
#  if two symbols match, player wins 2 times their bet
# if none symbols match, player loses their bet

import random


def get_starting_balance():
    while True:
        try:
            balance = int(input('Enter your starting amount: $'))
            if balance <= 0:
                print('Balance must be a positive number.')
            else:
                return balance
        except ValueError:
            print('Please enter a valid number.')


def get_bet_amount(balance):
    while True:
        try:
            bet = int(input('Enter your bet amount: $'))
            if bet > balance or bet <= 0:
                print(f'Invalid bet amount.you can bet between $1 and ${balance}.')
            else:
                return bet
        except ValueError:
            print('plezse enter a valid number for the bet amount')


def spin_reels():
    symbols = ['🍒', '🥭', '🔔', '⭐️', '🍉']
    return [random.choice(symbols) for _ in range(3)]


def display_reels(reels):
    print(f'{reels[0]} | {reels[1]} | {reels[2]}')


def calculate_payout(reels, bet):
    if reels[0] == reels[1] == reels[2]:
        return bet * 10
    if reels[0] == reels[1] or reels[0] == reels[1] or reels[1] == reels[2]:
        return bet * 2
    return 0


def main():
    balance = get_starting_balance()

    print('Welcome to slot machine game!')
    print(f'you start with the balance of {balance}')

    while balance > 0:
        print(f'current balance is {balance}')

        bet = get_bet_amount(balance)
        reels = spin_reels()
        display_reels(reels)
        payout = calculate_payout(reels, bet)

        if payout > 0:
            print(f'You won {payout}')
        else:
            print('You lost')

        balance += payout - bet
        if balance <= 0:
            print('You are out of money! game over')
            break

        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            print(f'You walk away with ${balance}')
            break


main()