''' Create a simple Rock Paper Scissor game '''

print("Welcome to the Rock, Paper, Scissor Game! \n\n")

def game(p1, p2):
    if p1 == p2:
      return "It's a tie! \n"
    elif (p1 == "rock" and p2 == "scissor") or (p1 == "scissor" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
      return "The Player 1 Wins! \n"
    elif (p2 == "rock" and p1 == "scissor") or (p2 == "scissor" and p1 == "paper") or (p2 == "paper" and p1 == "rock"):
      return "The Player 2 Wins! \n"
    else:
      return "Invalid input!\n"


p1 = input("Player 1: Enter your choice: ").lower()
p2 = input("Player 2: Enter your choice: ").lower()

print(game(p1, p2))
