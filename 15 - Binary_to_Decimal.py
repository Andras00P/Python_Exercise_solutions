''' Convert a binary number to decimal number
                    N = b * q^i,
    N is a real positive number
    b is the digit
    q is the base value
    i is an integer can be positive, negative or zero'''

def binary_to_decimal(num):
    decimal = 0
    btd = 0

    if int(num) == 0 or int(num) == 1:
        decimal = num

    else:
        i = len(num)
        num = num[::-1]
        while i > 0:
            btd = int(num[i - 1]) * 2 ** (i - 1)
            i -= 1
            decimal += btd

    return decimal

# Shortcut
def binary_to_decimal2(num):
    return int(num,2) # int() function already is able to convert binary to decimal

usr_num = input("Enter a binary number: \n")
print("Decimal number: ", binary_to_decimal(usr_num))
print("Decimal number: ", binary_to_decimal2(usr_num))
