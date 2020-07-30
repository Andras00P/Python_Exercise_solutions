''' Find the largest of two numbers '''

num = float(input("First Number?\n\n"))
num2 = float(input("Second Number?\n\n"))

# Beginner version
if (num2 >= num):
  largest = num2
else:
  largest = num

print("This is the largest number: ", largest)

# Simple way
print("This is the largest number: ", max(num, num2))

# Alternative Solution
#
# if(num - num2 > 0):
#   print("This is the largest number: ", num)
# else:
#   print("This is the largest number: ", num2)
