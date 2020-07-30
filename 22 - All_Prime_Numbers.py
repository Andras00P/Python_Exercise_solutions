''' Ask the user to enter a number. Then find all the primes up to that number '''


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True

def all_primes(num):
    primes = []

    for n in range(2, num + 1):
        if is_prime(n) is True:
            primes.append(n)

    return primes

usr_num = int(input("Enter number: \n"))
print("list of Primes", all_primes(usr_num))
