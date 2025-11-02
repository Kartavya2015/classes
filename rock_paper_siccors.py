import random
while True:
    useraction = input("Enter rock, paper or scissors: ")
    possibleactions = ["rock", "paper", "scissors"]
    computeraction = random.choice(possibleactions)
    print(f"You chose {useraction}, computer chose {computeraction}.")

    if useraction == computeraction:
        print(f"Both players selected {useraction}. It's a tie!")
    elif useraction == "rock":
        if computeraction == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif useraction == "paper":
        if computeraction == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cut paper! You lose.")
    elif useraction == "scissors":
        if computeraction == "paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    playagain = input("Do you want to play again?(y/n): ")
    if playagain == "n":
        break
    else:
        pass