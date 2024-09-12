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
todaysWord=random.choice(wordoodleDictionary)

# Declare incorrectLetters and misplacedLetters variables
incorrectLetters=[]
misplacedLetters=[]

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
print(f'\nHello {(input('Player Name: '))}!')

# Welcome user by name and print initial game status
# print(f'{wordLengthMessage}\n')
print(f'\n{remainingTurnsMessage}\n')

# Game loop

# define loop condition
while turnsTaken < 5:

    print(f'{takeTurnMessage}')

    turn = input()


    if len(turn) != 5:
        print('Please enter a 5 letter word!')
        print(f'Turns remaining: {str((maxTurns-turnsTaken))}')
    else:
        print(' '.join(turn))
        print(todaysWord)
        turnsTaken += 1
        print(f'Turns remaining: {str((maxTurns-turnsTaken))}')