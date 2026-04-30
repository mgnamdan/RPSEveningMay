import random

compChoice = random.randint(1, 3)
# FOR COMPUTER:
#     1 = ROCK
#     2 = PAPER
#     3 = SCISSORS

humChoice = input("Make a choice (rock, paper, scissors): ")

if compChoice == 1 and humChoice == "rock":
    print("You both chose rock and tied!")
elif compChoice == 1 and humChoice == "paper":
    print("You won! Paper beats rock!")
elif compChoice == 1 and humChoice == "scissors":
    print("Sorry, you lost! Rock beats scissors!")
elif compChoice == 2 and humChoice == "rock":
    print("Sorry, you lost! Paper beats rock!")
elif compChoice == 2 and humChoice == "paper":
    print("You both chose paper and tied!")
elif compChoice == 2 and humChoice == "scissors":
    print("You won! Scissors beats paper!")
elif compChoice == 3 and humChoice == "rock":
    print("You win! Rock beats scissors!")
elif compChoice == 3 and humChoice == "paper":
    print("You lost! Scissors beats paper!")
elif compChoice == 3 and humChoice == "scissors":
    print("You both chose scissors and tied!")
elif humChoice == "dynamite":
    print("Dynamite beats everything! You win!")
else:
    print("That's not an option!")