''' Find the largest of the three numbers '''

num = float(input("First Number?\n\n"))
num2 = float(input("Second Number?\n\n"))
num3 = float(input("Third number?\n\n"))

# Beginner version
if (num2 >= num) and (num2 >= num3):
  largest = num2
elif(num3 >= num1) and (num3 >= num):
  largest = num3
else:
  largest = num

print("This is the largest number: ", largest)

# Simple way
print("This is the largest number: ", max(num, num2, num3))
