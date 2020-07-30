''' Reverse a string (stack) '''

def reverse_stack(text):
    stack = []
    reverse = ""

    for char in text:
        stack.append(char)

    while len(stack) > 0:
        reverse += stack.pop()

    return reverse

text = input("Write the text, you want to reverse: \n")
print("Reversed: \n", reverse_stack(text))

# Shorter way
def reverse_stack2(text):
    stack = list(text)
    reverse = ""

    while len(stack) > 0:
        reverse += stack.pop()

    return reverse

print("Reversed: \n", reverse_stack2(text))
