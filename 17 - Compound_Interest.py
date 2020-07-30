''' Take money borrowed, interest and duration as input.
    Then, compute the compound interest rate.'''

''' Hint: Compund interest formula is:
            A = P(1 + r / 100)^t,
    P is the money borrowed
    r is the interest rate in %
    t is the time'''


def compound_interest(p, t, r):
    pay = 0

    pay = p * (1 + r / 100) ** t

    return pay

money = int(input("Enter the amount of money borrowed: \n\n"))
time = float(input("Enter the duration: \n\n"))
interest = float(input("Enter the interest rate: \n\n"))

print("You've to pay: ", compound_interest(money, time, interest))
