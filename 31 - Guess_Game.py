''' Build a simple guessing game where it will continuously ask the user to enter a number between 1 and 10.
    If the user's guesses matched, the user will score 10 points, and display the score.
    If the user's guess doesn't match, display the generated number.
    Also, if the user enters "q" stop the game. '''

import random

print("Welcome to the Guessing Game! \n\n")
print("Enter the letter q, to quit.\n")

score = 0

while True:
    npc = random.randint(0, 10)
    print("Guess a number between 0 and 10.")
    n = input("What's your guess? \n")

    if n == "q":
        print("\nGame Over!")
        break

    num = int(n)
    if num is npc:
        score += 10
        print("Your guess was correct!\n")
        print(f"You currently have {score} points\n")
    else:
        print(f"The number was {npc}\n")
