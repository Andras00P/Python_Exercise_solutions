''' With a given integral number n, write a program to calculate the sum of cubes '''

# Cube Sum using Math formula
def cube_sum_math(n):
    result = (n * (n + 1) / 2) ** 2

    return int(result)

# Using a for loop
def cube_sum(n):
    result = 0

    for i in range(0, num + 1):
        result += i ** 3

    return int(result)

num = int(input("Enter number: \n"))
print(cube_sum_math(num))
print(cube_sum(num))
