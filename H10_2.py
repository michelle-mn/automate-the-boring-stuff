#! usr/bin/env python3
# nicely done babe!!
# I love you <3
# I love you too ! xxx
import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

guess = ''

while guess not in ('heads', 'tails'):
    logging.info('Start of the program')
    print('Guess the coin tos! Enter heads or tails:')
    guess = input()
    if guess not in ('heads', 'tails'):
        assert Exception ('You have to type : heads or tails')

toss = random.randint(0,1) # 0 is tails, 1 is heads

logging.debug('toss is: ' + str(toss) +' and guess is: ' + str(guess))


if guess == 'tails':
    guess = 0
if toss == guess:
    print('You got it!') 
else:
    print('Nope! Guess again!')
    guess = input()

    if guess == 'heads':
        guess = 1
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game')
        
logging.debug('End of program')
        

