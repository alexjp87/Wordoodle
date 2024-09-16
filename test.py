from colorama import Fore, Style

# import getpass

# x = getpass.getpass("Input something: ")
# print(x)
"""
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

prGreen('Hello Green!')
prYellow('Hello Yellow!')

print('t',5,end="")
print(" next bit")
"""
# print(Fore.RED + "HELLO",end=" ")
# print(Fore.GREEN + "green text",end="")
# print(Style.RESET_ALL,end="")
# print("test")

# letters = ['a', '(b)', 'c']

# for letter in letters:
#     if letter == 'a':
#         print(letter, end=' ')
#     else:
#         print(Fore.RED + letter, end=' ')

# print(Style.RESET_ALL)
# print('Finished')

# word='leave'

# for letter in word:
#     print(word.count(letter))

# def validateGuess(guess, answer):
# # initialise default guessString (output) list
#     output = ['*', '*', '*', '*', '*']

# # define length of answer
#     length = len(answer)

# # loop through guess to check for letters contained in answer and in correct position:
#     for index in range(length):
# # if indexes match
#         if guess[index] == answer[index]:
# # insert letter into output in same position
#             output[index] = guess[index].upper()
# # replace letter in answer with '!' so it doesn't show up on next loop
#             answer.replace(answer[index], '!', 1)

# # loop through guess to check for letters contained in answer but in incorrect position:
#     for index in range(length):
# # if letter is in answer and has not already been replaced in output, i.e. the index in output is a '*'
#         if guess[index] in answer and output[index] == '*':
# # insert letter into output in same position
#             output[index] = guess[index]
# # replace letter in answer with '!' so it doesn't show up on next loop
#             answer.replace(answer[index], '!', 1)

#     # ' '.join(output)
    
#     return ' '.join(output)

# output = validateGuess(guess, answer)
# print(output)
# expected output:
# e l * * E


answer = 'leave'
guess = 'riiie'
guessString = ['*', '*', '*', '*', '*']
incorrectGuesses=[]

# def validateGuess(guess, answer, guessString):
# # Define length of answer to check against
#     length = 5
# # Loop through guess to check for letters contained in answer and in correct position:
#     for index in range(length):
# # if indexes match
#         if guess[index] == answer[index]:
# # insert letter into output in same position
#             guessString[index] = guess[index].upper()
# # replace letter in answer with '!' so it doesn't show up on next loop
#             answer.replace(answer[index], '!', 1)
# # Loop through guess to check for letters contained in answer but in incorrect position:
#     for index in range(length):
# # if letter is in answer and has not already been replaced in output, i.e. the index in output is a '*'
#         if guess[index] in answer and guessString[index] == '*':
# # insert letter into output in same position
#             guessString[index] = guess[index]
# # replace letter in answer with '!' so it doesn't show up on next loop
#             answer.replace(answer[index], '!', 1)
# # Return guessString    
#     return guessString

# def printColouredLetters(guessString):
# ## Loop through guessString
#     for letter in guessString:
# # if * then print yellow
#         if letter == '*':
#             print(Fore.YELLOW + letter)
# # else if letter was flagged as in correct position (is uppercase) print in green
#         elif letter.upper() == letter:
#             print(Fore.GREEN + letter)
# # else letter must have incorrect position so print in red
#         else:
#             print(Fore.RED + letter.upper())
# # Reset text colour to standard
#         print(Style.RESET_ALL)


# printColouredLetters(validateGuess(guess, answer, guessString))

def findIncorrectGuesses(guess, answer, incorrectGuesses):
    for letter in guess:
        if letter not in answer:
            incorrectGuesses.append(letter)

    return(incorrectGuesses)

def removeDuplicates(x):
    return list(dict.fromkeys(x))

print(','.join(removeDuplicates(findIncorrectGuesses(guess, answer, incorrectGuesses))))
 