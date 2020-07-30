""" For a given number, find all the numbers smaller than the number.
Numbers should be divisible by 3 and also by 5 """

def divisibleby3and5(num):
    results = []

    for i in range(1, num):
        if i % 3 == 0 and i % 5 == 0:
            results.append(i)
    return results

num = int(input("What's the number?\n\n"))

print(divisibleby3and5(num))

# Using While loop
def divisibleby3and5w(num):
    results = []
    i = 1

    while i <= num:
        if i % 3 == 0 and i % 5 == 0:
            results.append(i)
        i += 1

    return results

numw = int(input("What's the number?\n\n"))

print(divisibleby3and5w(numw))
