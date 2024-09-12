### SETUP

# Import 'random' library for use in step 5
import random

# Declare gameTitle variable
gameTitle='Wordoodle'

# Initialise dictionary as an empty list
wordoodleDictionary=[]

# Populate dictionary with contents of words.txt
with open('words.txt') as wordsFile:
    for line in wordsFile:
        wordoodleDictionary.append(line.rstrip("\n").lower())

# Pick random word for today's game
answer=random.choice(wordoodleDictionary)

# Declare incorrectLetters and misplacedLetters variables
guessGrid=[]
incorrectLetters=[]

# Declare maxTurns and turnsTaken variables
maxTurns=5
turnsTaken=0
    
# Create game title message
welcomeMessage=f'Welcome to {gameTitle}!'

# Create blurb
blurb='A terminal-based word guessing game built in python'

# Create enter player name message
# enterPlayerNameMessage='Please enter a player name below'

# Create instructions message

# Create length of word message
# wordLengthMessage='There are ' + {str(maxTurns)} + ' letters left to guess'

# Create remainingTurns message
remainingTurnsMessage=f'Turns remaining: {str((maxTurns-turnsTaken))}'

# Create take turn message
takeTurnMessage='Please take your turn:'

# Print welcome message and blurb
print(f'{welcomeMessage}\n\n{blurb}\n')

# Print enter name message
# print(f'{enterPlayerNameMessage}\n')

# Print welcome user message
print(f'\n\nHello {(input('Player Name: '))}!')

# Welcome user by name and print initial game status
# print(f'{wordLengthMessage}\n')
print(f'\n{remainingTurnsMessage}\n')



### GAME LOOP

# define loop condition
while turnsTaken < 5:

# clear guessGrid list
    guessGrid.clear()

# prompt to take turn
    print(f'\n{takeTurnMessage}')

# capture input in variable 'turn'
    guess = input()
    guess = guess.lower()
# check if turn had the expected length of 5 characters
    if len(guess) != 5:
# if not, show error and prompt to try again
        print('Invalid turn. Please enter a 5 letter word!')
# and show that still have same number of turn remaining
        print(f'Turns remaining: {str((maxTurns-turnsTaken))}')
# if so        
    else:
# ...
    
        print(f'\t{' '.join(guess)}\n')
        # print(f'\t{answer}\n')

        for letter in guess:
            if letter in answer:
                print(f'Congratulations, {letter} is in the answer!\n')
                if answer.index(letter) == guess.index(letter):
                    guessGrid.append(letter)
                else:
                    guessGrid.append(f'({letter})')
            else:
                incorrectLetters.append(letter)
                guessGrid.append('*')

        print(' '.join(guessGrid))
        print(f'\nIncorrect letters: {incorrectLetters}')
# increment turns takento reduce remaining turns by 1
        turnsTaken += 1
# print how many turns remaining        
        print(f'\nTurns remaining: {str((maxTurns-turnsTaken))}')













"""
NOTES:

- end game when correct guess made

- end game when run out of lives
"""