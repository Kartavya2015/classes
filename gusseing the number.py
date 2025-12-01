import random
import time

number = random.randint(1, 100)
def intro():
    print("Ehat is your name?")
    global name
    name = input()
    print("Hello, " + name + ", I am thinking of a number between 1 and 100.")
    print("You have to guess which number I am thinking of.")
    print("You have 6 attempts to guess the number.")

    if(number % 2 == 0):
        x = "even"
    else:
        x = "odd"
    print("Here is a hint! The number is an" + x + "number.")
    time.sleep(.5)

def pick():
    guessTaken = 0

    while guessTaken < 6:
        enter=input("Take a guess: ")
        try:
            guess = int(enter)
            if guess <=100 or guess >=1:
                guessTaken += 1
                if guess < number:
                    print("Your guess is too low.")
                if guess > number:
                    print("Your guess is too high.")
                if guess != number:
                    time.sleep(.5)
                    print("Try again.")

                if guess == number:
                    break

                if guess<100 or guess>1:
                    print("Silly Goose!It is too out of range.")
                    time.sleep(.25)
        except:
                print("I don't thonk that"+enter+"is a number.")
    if guess == number:
        guessTaken = str(guessTaken)
        print("Good job, " + name + "! You guessed my number in " + guessTaken + " guesses!")
    if guess != number:
        number = str(number)
        print("Nope. The number I was thinking of was " + number)

playingagain = "yes"
while playingagain == "yes" or playingagain == "y":
    intro()
    pick()
    print("Would you like to play again? (yes or no)")
    playingagain = input()