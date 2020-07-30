''' Convert a decimal number to binary number '''

''' Hint: To convert a decimal number to a binary number, you have to keep
dividing the number by 2.

While dividing, you will keep the remainder. These remainders will be usd to
build a binary number.

Then, reverse the order of the remainder, to get the binary number. '''


def decimal_to_binary(nums):
    bits = []

    while nums > 0:
        bits.append(nums % 2)
        nums = nums // 2

    bits.reverse()

    binary = ""

    for bit in bits:
        binary += str(bit)

    return binary

usr_num = int(input("Enter a decimal number: \n"))
print("Binary number: ", decimal_to_binary(usr_num))
