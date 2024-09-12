# import getpass

# x = getpass.getpass("Input something: ")
# print(x)

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

prGreen('Hello Green!')
prYellow('Hello Yellow!')

print('t',5,end="")
print(" next bit")