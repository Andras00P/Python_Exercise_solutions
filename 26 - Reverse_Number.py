''' Reverse a number '''

def reverse_number(n):
    reverse = 0

    while n > 0:
        last = n % 10
        reverse = reverse * 10 + last
        n = n // 10

    return reverse

num = int(input("Enter the number you would like to reverse: \n"))
print("Reversed number: ", reverse_number(num))
