''' You borrowed $5000 for 2 years with 2% interest per year.
Calculate the simple interest to know how much you have to pay '''

def simple_interest(m, t, i):
    pay = 0
    i = i / 100

    pay = (m * t * i) + m

    return pay

money = int(input("Enter the amount of money borrowed: \n\n"))
time = float(input("Enter the duration: \n\n"))
interest = float(input("Enter the interest rate: \n\n"))

print("You've to pay: ", simple_interest(money, time, interest))
