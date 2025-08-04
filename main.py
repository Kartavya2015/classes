import random

import sys
def play_game():
    print(" Welcome to the Dice Game!")

    user_score = 0
    computer_score = 0
    round_number = 1

    while user_score < 5 and computer_score < 5:
        print(f"\n--- Round {round_number} ---")
        try:
            user_input = int(input("Enter a number between 1 and 6: "))
        except ValueError:
            print(" Invalid input. Please enter a number.")
            continue

        if user_input < 1 or user_input > 6:
            print(" Number out of range. Try again.")
            continue

        computer_number = random.randint(1, 6)
        print(f"Computer rolled: {computer_number}")

        if user_input > computer_number:
            print(" You win this round!")
            user_score += 1
        elif user_input < computer_number:
            print(" You lose this round.")
            computer_score += 1
        else:
            print(" It's a tie! No points.")

        print(f"Score  You: {user_score} | Computer: {computer_score}")
        round_number += 1

    # want to quit option
    quit_input = input("Do you want to quit the game? (yes/no): ")4
    
    if quit_input == 'yes':
        print(" You chose to quit the game.")
        
    else:
        print(f" Ok, you have {5 - user_score} left to win")

    # Final Result
    print("\n Game Over!")
    if user_score == 10:
        print(" Congratulations! You won the game!")
    else:
        print(" Computer wins the game. Better luck next time!")

        

# Start the game
play_game()