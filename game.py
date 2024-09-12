### SETUP

### Libraries

# Import 'colorama' library
from colorama import Fore, Style

# Import 'random' library
import random


### Variables

# Declare title variable
gameTitle='Wordoodle'

# Create title message
welcomeMessage=f'Welcome to {gameTitle}!'

# Create blurb
blurb='A terminal-based word guessing game built in python'

# Create instructions message
# ...

# Declare maxTurns and turnsTaken variables
maxTurns=5
turnsTaken=0
# Create remainingTurns message
remainingTurnsMessage=f'Turns remaining: {str((maxTurns-turnsTaken))}'

# Create take turn message
takeTurnMessage='Please take your turn:'


### Lists

# Initialise dictionary as empty list
wordoodleDictionary=[]
# populate dictionary with contents of words.txt
with open('words.txt') as wordsFile:
    for line in wordsFile:
        wordoodleDictionary.append(line.rstrip("\n").lower())

# Select random word from dictionary to become game answer
answer=random.choice(wordoodleDictionary)

# Declare guess string and incorrect guesses as empty lists
guessString=[]
incorrectGuesses=[]
    


### START SCREEN

# Print welcome message and blurb
print(f'{welcomeMessage}\n\n{blurb}\n')

# Prommpt player to enter name and print personalised welcome message
print(f'\n\nHello {(input('Player Name: '))}!')

# Print number of turns remaining (5)
print(f'\n{remainingTurnsMessage}\n')




### GAME LOOP

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


## If user input was not the expected length (5):
    if len(guess) != 5:
# inform player of error and prompt to try again
        print('Invalid turn. Please enter a 5 letter word!')
# display unchanged number of turns remaining
        print(f'Turns remaining: {str((maxTurns-turnsTaken))}')


## Else if user input passes error checks:      
    else:
# print input
        print(f'\t{' '.join(guess)}\n')
        print(f'\t{answer}\n')


## Build string to display progress (guessString):
# loop through input
        for letter in guess:
            if letter in answer:
# if letter is contained in answer, congratulate player
                print(f'Congratulations, {letter} is in the answer!\n')
# if indexes match then append to guessString as is
                if answer.index(letter) == guess.index(letter):
                    guessString.append(letter)
# else if letter is contained in answer but indexes don't match then append to guessString in uppercase (flagged)
                else:
                    guessString.append(f'{letter.upper()}')
# else if letter is not contained in answer then append to incorrectGuesses list and append * to guessString
            else:
                incorrectGuesses.append(letter)
                guessString.append('*')


## Colourise guessString letters:
        # print(' '.join(guessString))
# Loop through guessString
        for letter in guessString:
# if letter was flagged (is uppercase) and isn't a * then print in RED
            if letter.upper() == letter and letter != '*':
                print(Fore.RED + letter.lower(), end=' ')
# else if letter is a * then print in WHITE
            elif letter == '*':
                    print(Fore.WHITE + letter, end=' ')
# else letter must be in correct position so print in GREEN
            else:
                print(Fore.GREEN + letter, end=' ')
# reset text colour to standard
        print(Style.RESET_ALL)


## Check if player has won - if so print winning message and end game
        if '*' not in guessString:
            print('You win! Wooooooooooooooooo-rdoodle!')
            break


## Else print incorrect guesses list
        print(f'\nIncorrect guesses: {','.join(incorrectGuesses)}')
# increment turns taken to reduce remaining turns by 1
        turnsTaken += 1
# print how many turns remaining        
        print(f'\nTurns remaining: {str((maxTurns-turnsTaken))}')

# ...and return to start of game loop (clearing guessString list)


print(f'\nGame over! (The word was \'{answer}\'!)')











"""
NOTES:

- ***double letters bug***

- deal with duplicates in incorrect letters list

- add instructions message

- create win message variable and replace current string
    - save player name to variable to personalise win message?

- when player wins, don't print game over message

- add more error checking, e.g. if input consisted only of letters

- change layout, make pretty!
    - centre title
    - change guesses to uppercase?

"""