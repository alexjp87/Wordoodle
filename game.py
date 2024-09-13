### SETUP

### Libraries

# Import 'colorama' library
from colorama import Fore, Style

# Import 'random' library
import random


### Variables

# Declare gameTitle variable
gameTitle='Wordoodle'

# Create welcomeMessage
welcomeMessage=f'Welcome to {gameTitle}!'

# Create blurb
blurb='A terminal-based word guessing game built in python'

# Create instructions message
# ...

# Declare maxTurns and turnsTaken variables
maxTurns=5
turnsTaken=0
# Declare turnsRemaining variable
turnsRemaining=(maxTurns-turnsTaken)
# Create turnsRemaning message
turnsRemainingMessage=f'Turns remaining: {str(turnsRemaining)}'

# Create takeTurn message
takeTurnMessage='Please take your turn:'


### Lists

# Initialise wordoodleDictionary as empty list
wordoodleDictionary=[]
# populate wordoodleDictionary with contents of words.txt (strip white space at end of lines and make lower case)
with open('words.txt') as wordsFile:
    for line in wordsFile:
        wordoodleDictionary.append(line.rstrip("\n").lower())

# Declare guessString and incorrectGuesses as empty lists
guessString=[]
incorrectGuesses=[]


### Functions

# Create removeDuplicates function
def removeDuplicates(x):
    return list(dict.fromkeys(x))




### GAME


# Select random word from dictionary to become game answer
answer=random.choice(wordoodleDictionary)


### START SCREEN

## Print welcome message and blurb
print(f'{welcomeMessage}\n\n{blurb}\n')

# Prommpt player to enter name and print personalised welcome message
print(f'\n\nHello {(input('Player Name: '))}!')


# Print initial game status: (number of turns remaining)
print(f'\n{turnsRemainingMessage}\n')



### LOOP


# Define loop condition as: run game while number of turns taken is less than 5
while turnsTaken < 5:

# Clear guessString list
    guessString.clear()

# Prompt player to take turn
    print(f'\n{takeTurnMessage}')

## Capture input in variable
    guess = input()
# re-declare input variable in lower case for case insensitivity
    guess = guess.lower()


## If input was not the expected length (5):
    if len(guess) != 5:
# inform player of error and prompt to try again
        print('Invalid turn. Please enter a 5 letter word!')
# display unchanged number of turns remaining
        print(f'Turns remaining: {str((turnsRemaining))}')


## Else if input passes error checks:      
    else:
# print input
        print(f'\t{' '.join(guess)}\n')
        print(f'\t{answer}\n')

## And build string to display progress (guessString):
# loop through input
        for letter in guess:
# if letter is contained in answer, print congratulations
            if letter in answer:
                print(f'Congratulations, {letter} is in the answer!\n')
# if indexes match then append to guessString unmutated
                if answer.index(letter) == guess.index(letter):
                    guessString.append(letter)
# else if letter is contained in answer but indexes don't match then append to guessString in uppercase (flag)
                else:
                    guessString.append(f'{letter.upper()}')
# else if letter is not contained in answer then append to incorrectGuesses list and append * to guessString in place of letter
            else:
                incorrectGuesses.append(letter)
                guessString.append('*')

## colourise guessString letters:
        # print(' '.join(guessString))
# loop through guessString
        for letter in guessString:
# if letter was flagged (is uppercase) and isn't a * then print in RED and change end of line to a space
            if letter.upper() == letter and letter != '*':
                print(Fore.RED + letter.lower(), end=' ')
# else if letter is a * then print in WHITE and change end of line to a space
            elif letter == '*':
                    print(Fore.YELLOW + letter, end=' ')
# else letter must be in correct position so print in GREEN and change end of line to a space
            else:
                print(Fore.GREEN + letter, end=' ')

# reset text colour to standard
        print(Style.RESET_ALL)


## Check guessString to see if player has won - if so print winning message and end game
        if '*' not in guessString:
            print('You win! Wooooooooooooooooo-rdoodle!')
            break

## Else if player hasn't won and game continues:
# remove duplicates and print incorrect guesses list
        incorrectGuesses = removeDuplicates(incorrectGuesses)
        print(f'\nIncorrect guesses: {' / '.join(incorrectGuesses)}')
# increment turns taken by 1 and re-declare turnsRemaining variable
        turnsTaken += 1
        turnsRemaining=(maxTurns-turnsTaken)
# print how many turns remaining        
        print(f'\nTurns remaining: {str((turnsRemaining))}')

# ...and return to start of game loop (approx. line 78 - clear guessString list and prompt input)


print(f'\nGame over! (The word was \'{answer}\'!)')











"""
NOTES:

- ***double letters bug***

- change win condition - don't check for no *'s as would fail if had all letters but in wrong order

- deal with duplicates in incorrect letters list

- add instructions message

- create win message variable and replace current string
    - save player name to variable to personalise win message?

- print game over message only when player runs out of turns, not when wins
    - where to place?

- add more error checking, e.g. check if input consisted only of letters

- change layout, make pretty!
    - centre title
    - change gameplay strings to uppercase?
    - | to separate incorrectGuesses?

"""