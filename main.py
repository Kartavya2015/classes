import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("Hey,you might be new here, please play the game first!")
    else:
        print("yor score is {} attempt/s!".format(min(attempts_list)))
        def start_game():
            random_number =int(random.randint(1, 10))
            print("hey there.whats yor name?")
            player_name = input("Enter right HERE:")
            wanna_play = input("Hey {}, do you want to play a game? (yes/no): ".format(player_name))
            ## Where the show_score function USED to be 
            attempts = 0
            while wanna_play.lower() == "yes":
                try:
                    guess = input("Enter a number between 1 and 10: ")
                    if int(guess)< 1 or int(guess) > 10:
                        raise ValueError("Number out of range. Please try again in 1-10.")
                    if int(guess) == random_number:
                        print("congrats,you geussed it right!")
                        attempts +=1
                        attempts_list.append(attempts)
                        print("You guessed it in {} attempts.".format(attempts))
                        play_again = input("do you want to play again? (yes/no): ")
                        attempts = 0
                        show_score()
                        random_number = int(random.randint(1-10))
                        if play_again.lower() == "no":
                            print("that's col,have a nice day")
                            break
                        elif int(guess) > random_number:
                            print("Your guess is too high, try again!")
                        elif int(guess) < random_number:
                            print("Your guess is too low, try again!")
                except ValueError as err:
                    print("Invalid input")
                    print("({})".format(err))
            else:
                print("Thanks for playing, !")
                if __name__ == '__main__' :
                 start_game()