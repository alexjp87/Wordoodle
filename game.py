### SETUP

#
#
#

## Import Libraries

# Import 'colorama' library
from colorama import Fore, Style

# Import 'random' library
import random

#-------------------------------------------------------------#


## Variables

# gameTitle
gameTitle='Wordoodle'

# welcomeMessage
welcomeMessage=f'Welcome to {gameTitle}!'

# blurb
blurb='A terminal-based word guessing game built in python'

# instructionsMessage
# ...

# maxTurns
maxTurns=6
# turnsTaken
turnsTaken=0
# turnsRemaining
turnsRemaining=(maxTurns-turnsTaken)
# turnsRemaning message
turnsRemainingMessage=f'Turns remaining: {str(turnsRemaining)}'

# takeTurn message
takeTurnMessage='Please take your turn:'

#-------------------------------------------------------------#


## Lists

# Initialise wordoodleDictionary as empty list
wordoodleDictionary=[]
# populate with contents of words.txt - strip white space at end of lines and make lower case
with open('words.txt') as wordsFile:
    for line in wordsFile:
        wordoodleDictionary.append(line.rstrip("\n").upper())

# Initialise incorrectGuesses empty list
incorrectGuesses=[]

#-------------------------------------------------------------#


## Functions

# Create validateGuess to process guess (deals with repeated letter issue) and populate guessString:
def validateGuess(guess, answer, guessString):
# Define length of answer to check against
    length = 5
# Loop through guess to check for letters contained in answer and in correct position:
    for index in range(length):
# if indexes match
        if guess[index] == answer[index]:
# insert letter into output in same position in lower case (flag)
            guessString[index] = guess[index].lower()
# replace letter in answer with '!' so it doesn't show up on next loop
            answer = answer.replace(answer[index], '!', 1)
# Loop through guess to check for letters contained in answer but in incorrect position:
    for index in range(length):
# if letter is in answer and has not already been replaced in output, i.e. the index in output is a '*'
        if guess[index] in answer and guessString[index] == '*':
# insert letter into output in same position
            guessString[index] = guess[index]
# replace letter in answer with '!' so it doesn't show up on next loop
            answer.replace(answer[index], '!', 1)
# Return guessString list   
    return guessString


# Create printColouredLetters to print coloured guessString:
def printColouredLetters(guessString):
## Loop through guessString
    for letter in guessString:
# if * then print yellow
        if letter == '*':
            print(f'{Fore.YELLOW + letter}')
# else if letter was flagged as in correct position (is lowercase) print in green
        elif letter.lower() == letter:
            print(f'{Fore.GREEN + letter.upper()}')
# else letter must have incorrect position so print in red
        else:
            print(f'{Fore.RED + letter}')
# Reset text colour to standard
        print(Style.RESET_ALL)


# Create findIncorrectGuesses:
def findIncorrectGuesses(guess, answer, incorrectGuesses):
# Loop through guess
    for letter in guess:
# if letter not in answer
        if letter not in answer:
 # append to incorrectGuesses list
            incorrectGuesses.append(letter)
# Return incorrectGuesses
    return(incorrectGuesses)

# Create removeDuplicates to neaten incorrectGuesses list
def removeDuplicates(x):
    return list(dict.fromkeys(x))

#-------------------------------------------------------------#



### GAME

#
#
#

# Select random word from dictionary to become game answer
# answer=random.choice(wordoodleDictionary)
answer='LOAVE'

## START SCREEN

## Print welcome message and blurb
print(f'\n{welcomeMessage}\n\n{blurb}\n')

# Prommpt player to enter name
print('\nPlease enter username:')

# Capture username in variable
username = input()

# Print personalised welcome message using capitalised username
print(f'\n\nHello {username.title()}!')

# Print initial game status: (number of turns remaining)
print(f'\n{turnsRemainingMessage}\n')



### LOOP


# Define loop condition as: run game while number of turns taken is less than 5
while turnsTaken < maxTurns:

# Return guessString to initial state
    guessString = ['*', '*', '*', '*', '*']

# Prompt player to take turn
    print(f'\n{takeTurnMessage}')

## Capture input in variable
    guess = input()
# re-declare input variable in upper case for case insensitivity
    guess = guess.upper()


## Error checking:
# If input was not the expected length (5):
    if len(guess) != 5:
# inform player of error and prompt to try again
        print(f'{guess} is an invalid turn. Please enter a 5 letter word!')
# display unchanged number of turns remaining
        print(f'\nTurns remaining: {str((turnsRemaining))}')
# Else:
    else:
## process guess and print coloured guessString
        printColouredLetters(validateGuess(guess, answer, guessString))

## Check guessString to see if player has won - if so print winning message and end game
        if  guess == answer:
            print(f'Congratulations {username}! You win!\n\nWooooooooooooooooo-rdoodle!')
            break

## Else if player hasn't won and game continues:
        else:    
# increment turns taken by 1
            turnsTaken += 1
# if turns taken = 5, print game over message (and end loop)
            if turnsTaken == maxTurns:
                print(f'\nGame over! (The word was \'{answer}\'!)')
            else:
# remove duplicates from incorrect guesses list and print
                print(f'Incorrect guesses: {','.join(removeDuplicates(findIncorrectGuesses(guess, answer, incorrectGuesses)))}')
# re-declare turnsRemaining variable
                turnsRemaining = maxTurns - turnsTaken
# print how many turns remaining        
                print(f'\nTurns remaining: {turnsRemaining}')

# ...and return to start of game loop (approx. line 90 - clear guessString list and prompt input)












"""
NOTES:

- add instructions message

- create win message variable and replace current string
    - save player name to variable to personalise win message?

- print game over message only when player runs out of turns, not when wins
    - where to place?

- add more error checking, e.g. check if input consisted only of letters

- README

- change layout, make pretty!
    - centre title
    - change gameplay strings to uppercase?
    - | to separate incorrectGuesses?

"""