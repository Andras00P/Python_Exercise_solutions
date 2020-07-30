""" Take a number as input. Then get the sum of the number. If the number is n.
Then get 0^2 + 1^2 + 2^2 + 3^2 + 4^2 + ....... + n^2 """


def sum_of_square(num):

   result = 0

   for i in range(num + 1):
       result += i ** 2

   return result

num = int(input("Insert number: "))
print("Sum of square numbers is ", sum_of_square(num))


# Mathmatical Way
def sum_of_square2(n):
   result2 = n * (n + 1) * (2 * n + 1)/6

   return result2

 num2 = int(input("Insert number: "))
 print("Sum of square numbers is ", sum_of_square2(num2))
