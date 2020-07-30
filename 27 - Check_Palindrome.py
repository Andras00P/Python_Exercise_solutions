''' Check whether the string is a palindrome '''

''' A palindrome is a word, phrase or sequence, that reads the same backward
    as forward. For example: madam'''

def reverse_stack(text):
    stack = list(text)
    reverse = ""

    while len(stack) > 0:
        reverse += stack.pop()

    return reverse

usr_str = input("Word to check: \n")

if usr_str == reverse_stack(usr_str):
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

# Shortcut
usr_str = input("Word to check: \n")

rev_str = usr_str[::-1]

if usr_str == rev_str:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
