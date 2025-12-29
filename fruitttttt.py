import random
class fru:
    def __init__ (self):
        
        self.fruits = {'banana': 'yellow',
                       'apple': 'red',
                       'grape': 'purple',
                       'orange': 'orange',
                       'kiwi': 'brown',
                       'watermelon': 'green',
                       'blueberry': 'blue',
                       'peach': 'pink',
                       'mango': 'yellow',
                       'strawberry': 'red',
                       'lemon': 'yellow',
                       'cherry': 'red',
                       'pear': 'green',
                       'plum': 'purple',
                       'papaya': 'orange',
                       'coconut': 'brown',
                       'lime': 'green',
                       'raspberry': 'red',
                       'blackberry': 'black',
                       'pomegranate': 'red'}
        
    def quiz (self):
            while (True):
                fruit, color = random.choice(list(self.fruits.items()))
                print("What is the color of {}?".format(fruit))
                answer = input("Your answer: ")
                if (answer.lower() == color):
                    print("Correct!")
                else:
                    print("Incorrect! The correct answer is {}.".format(color))
                
                option = input("Do you want to try again? (yes/no): ")
                if (option.lower() == 'no'):
                    break
                else:
                    continue

print("Welcome to the Fruit Color Quiz!")
game = fru()
game.quiz()