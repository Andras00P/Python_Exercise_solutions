''' Ask the user to enter a number. Then find all the prime factors for the number '''

''' HINT: A prime factor is a prime number that could divide a number'''

def prime_factors(num):
    primes = []
    divisor = 2

    while num > 2:
        if num % divisor == 0:
            primes.append(divisor)
            num = num / divisor
        else:
            divisor += 1

    return primes

usr_num = int(input("Enter number: \n"))
print("list of Prime Factors", prime_factors(usr_num))
