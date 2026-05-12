# ~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~

import random

def rps():

    MOVES = {"rock": 0, "paper": 1, "scissors": 2, "dynamite": 3,
             "r": 0, "p": 1, "s": 2, "d": 3}

    playAgain = True
    while playAgain:
        compChoice = random.randint(0, 2)

        validChoice = False
        for _ in range(50):
            print("")
            
        while not validChoice:
            print("")
            print("Make a choice (rock, paper, scissors)")
            print("")
            humChoice = input(" --> ").lower()
            if humChoice in MOVES.keys():
                validChoice = True
            else:
                print("")
                print("That's not an option - try again!")
                print("")

        humChoice = MOVES[humChoice]

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
    MOVES_R = {0: "rock", 1: "paper", 2: "scissors", 3: "dynamite"}
    if hChoice == 3:
        outcome = 1
    else:
        outcome = ((hChoice - cChoice + 1) % 3) - 1
        # x % y --> x - (y * floor(x/y))

    if outcome > 0:
        print("")
        print(f"{MOVES_R[hChoice]} beats {MOVES_R[cChoice]}! You beat the computer!")
        print("")
    elif outcome == 0:
        print("")
        print(f"You tied the computer! You both chose {MOVES_R[hChoice]}!")
        print("")
    else:
        print("")
        print(f"{MOVES_R[cChoice]} beats {MOVES_R[hChoice]}! The computer beat you!")
        print("")




# ~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~

def main():
    appOn = True
    while appOn:
        for _ in range(50):
            print("")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("              MAIN MENU")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("1. Rock, Paper, Scissors")
        print("2. Quit")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
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
    