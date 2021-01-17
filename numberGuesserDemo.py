# Number Guessing Program

from random import randrange

numberRange = int(input('What do you want the number range to be? Give us a good one: '))
#secretNum = 0
guessNum = -1
secretNum = randrange(numberRange)
guessCount = 0

# Guessing loop

while guessNum != secretNum:
    # do this code forever

    guessNum = input('Guess a number between 0 and ' + str(numberRange) + ': ')
    guessCount += 1

    if int(guessNum) == secretNum:
        print('Zone! ' + guessNum + ' was correct. You won in ' + str(guessCount) + ' guesses!')
        break

    elif int(guessNum) < secretNum:
        print('Zone! ' + guessNum + ' was too small big-bruv!')

    elif int(guessNum) > secretNum:
        print('Zone! ' + guessNum + ' was too big bruvna!')
