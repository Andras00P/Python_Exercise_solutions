""" Reverse a string.
    If the input is: Hello World.
    The output should be: .dlroW olleH """


def reverse_string(text):
    result = ""

    for char in text:
        result = char + result

    return result


# Shortcut
def reverse_string2(text):
    return text[::-1]


usr_text = input("Write the text, you want to reverse: \n")
print("Reversed: \n", reverse_string(usr_text) + "\n", reverse_string2(usr_text))
