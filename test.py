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

word='leave'

for letter in word:
    print(word.count(letter))