''' For a given number, check whether the number is a prime number or not '''


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True

usr_num = int(input("Enter number: \n"))

if is_prime(usr_num):
    print("The number is a Prime")
else:
    print("The number is not a Prime")
