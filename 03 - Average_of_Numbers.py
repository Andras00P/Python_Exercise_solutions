''' Take numbers from a user and show the average of the numbers the user entered '''

nums = int(input("How many numbers to you want use?\n\n"))
num_list = []

for n in range(0, nums):
    num = float(input("What's the number?\n\n"))
    num_list.append(num)

average = (sum(num_list) / nums)

print("The average is: ", average)

# Other (For loop) way

total = 0

for i in range(0, nums):
    num2 = float(input("What's the number?\n\n"))
    total += elem

average2 = (total / nums)

print("The average is: ", average2)

# Using While loop

num_listw = []

while len(num_listw) < nums:
    numw = float(input("What's the number?\n\n"))
    num_listw.append(numw)

averagew = (sum(num_listw) / nums)

print("The average is: ", averagew)
