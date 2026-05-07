# ~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~

import random

def rps():
    playAgain = True
    while playAgain:
        compChoice = random.choice(["rock", "paper", "scissors"])

        validChoice = False
        while not validChoice:
            print("")
            print("Make a choice (rock, paper, scissors)")
            print("")
            humChoice = input(" --> ").lower()
            if humChoice in ["rock", "paper", "scissors", "dynamite", "r", "p", "s", "d"]:
                validChoice = True
            else:
                print("")
                print("That's not an option - try again!")
                print("")

            determineWinner(humChoice, compChoice)

        print("")
        print("Would you like to play another game or rock, paper, scissors? (yes/no)")
        print("")
        moreGame = input(" --> ").lower()
        if moreGame in ["no", "n", "exit", "quit"]:
            print("")
            print("")
            playAgain = False



def determineWinner(hChoice, cChoice):
    if cChoice == "rock" and hChoice == "rock":
        print("You both chose rock and tied!")
    elif cChoice == "rock" and hChoice == "paper":
        print("You won! Paper beats rock!")
    elif cChoice == "rock" and hChoice == "scissors":
        print("Sorry, you lost! Rock beats scissors!")
    elif cChoice == "paper" and hChoice == "rock":
        print("Sorry, you lost! Paper beats rock!")
    elif cChoice == "paper" and hChoice == "paper":
        print("You both chose paper and tied!")
    elif cChoice == "paper" and hChoice == "scissors":
        print("You won! Scissors beats paper!")
    elif cChoice == "scissors" and hChoice == "rock":
        print("You win! Rock beats scissors!")
    elif cChoice == "scissors" and hChoice == "paper":
        print("You lost! Scissors beats paper!")
    elif cChoice == "scissors" and hChoice == "scissors":
        print("You both chose scissors and tied!")
    elif hChoice == "dynamite":
        print("Dynamite beats everything! You win!")



# ~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~

def main():
    appOn = True
    while appOn:
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("              MAIN MENU")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("1. Rock, Paper, Scissors")
        print("2. Quit")
        print("")
        print("")
        userChoice = input(" --> ").lower()
        if userChoice in ["1", "1.", "rock, paper, scissors", "rps", "r,p,s", "1. rock, paper, scissors"]:
            rps()
        elif userChoice in ["quit", "2", "2.", "2. quit"]:
            appOn = False
        else:
            print("")
            print("Invalid option - try again!")
            print("")
        


# ~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    main()




























# ~~~~~~~~~~~~~~~~~~~~
# OLD RPS CODE
# ~~~~~~~~~~~~~~~~~~~~



# compChoice = random.randint(1, 3)
# # FOR COMPUTER:
# #     1 = ROCK
# #     2 = PAPER
# #     3 = SCISSORS

# humChoice = input("Make a choice (rock, paper, scissors): ").lower()

# if compChoice == 1 and humChoice == "rock":
#     print("You both chose rock and tied!")
# elif compChoice == 1 and humChoice == "paper":
#     print("You won! Paper beats rock!")
# elif compChoice == 1 and humChoice == "scissors":
#     print("Sorry, you lost! Rock beats scissors!")
# elif compChoice == 2 and humChoice == "rock":
#     print("Sorry, you lost! Paper beats rock!")
# elif compChoice == 2 and humChoice == "paper":
#     print("You both chose paper and tied!")
# elif compChoice == 2 and humChoice == "scissors":
#     print("You won! Scissors beats paper!")
# elif compChoice == 3 and humChoice == "rock":
#     print("You win! Rock beats scissors!")
# elif compChoice == 3 and humChoice == "paper":
#     print("You lost! Scissors beats paper!")
# elif compChoice == 3 and humChoice == "scissors":
#     print("You both chose scissors and tied!")
# elif humChoice == "dynamite":
#     print("Dynamite beats everything! You win!")
# else:
#     print("That's not an option!")
    