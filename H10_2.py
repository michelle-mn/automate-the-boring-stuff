#!/usr/bin/env python3
import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

guess = ''

def get_input():
    return input().lower()

logging.info('Start of the program')
while guess not in ('heads', 'tails'):
    print('Guess the coin tos! Enter heads or tails:')
    guess = get_input()
    if guess not in ('heads', 'tails'):
        assert Exception ('You have to type : heads or tails')

coinflip = random.choice(['heads', 'tails']) # 0 is tails, 1 is heads


logging.debug('toss is: ' + coinflip +' and guess is: ' + guess)


if coinflip == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = get_input()

    if coinflip == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game')

logging.debug('End of program')
