''' Calculate the greatest common divisor (GCD) of two numbers '''


import math

# Using loop
def gcd(x, y):
    smaller = min(x, y)
    gcd = 1

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

# Using the python built-in method
def gcd_math(c, d):
    gcd_m = math.gcd(c, d)

    return gcd_m

num = int(input("Enter the first number: \n"))
num2 = int(input("Enter the second number: \n"))
print("GCD of ", num, " and ", num2, " is ", gcd(num, num2))
print("GCD of ", num, " and ", num2, " is ", gcd_math(num, num2))
