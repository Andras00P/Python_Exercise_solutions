''' For a given number, find the sum of every digit '''

def sum_of_digits(nums):
    total = []

    for n in nums:
        total.append(int(n))

    total = sum(total)
    return total

num = input("give us a number?\n\n")

print("The Sum of the digits is: ", sum_of_digits(num))

# Other For Loop

def sum_of_digits(nums):
    total = 0

    for n in nums:
        total += int(n)

    return total

num2 = input("give us a number?\n\n")

print("The Sum of the digits is: ", sum_of_digits(num2))

# Using While Loop
def sum_of_digitsw(num):
   total = 0

   while(num > 0):
       last_digit = num % 10
       total += last_digit
       num = num // 10

   return total

numw = int(input("Enter a number:"))

print("The total sum of digits is: ", sum_of_digits(numw))
