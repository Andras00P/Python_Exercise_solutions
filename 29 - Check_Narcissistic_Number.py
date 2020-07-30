''' Check whether a number is an Narcissistic Number '''

''' A number is narcissistic number if it is equal to the sum of it's own digits
    raised to the power of the number of digits'''


def narcissistic_number(n):
    n_str = str(n)
    n_length = len(str(n))
    result = 0

    for i in n_str:
        result += int(i) ** n_length

    if n == result:
        return "It's a narcissistic number"

    return "It's not a narcissistic number"

num = int(input("Enter number: \n"))
print(narcissistic_number(num))
