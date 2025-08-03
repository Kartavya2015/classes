import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import random

BATTERY_LEVEL = 100
CHARGING = False

PASSCODE = "#1234"

# Game Functions
def play_guess_number():
    num = random.randint(1, 10)
    guess = simpledialog.askinteger("Guess", "Guess a number (1-10):")
    if guess == num:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", f"Wrong! It was {num}.")

# Move snake_game and questions to top-level scope
def snake_game():
    input("help the snake reach the end by answering correctly:")
    questions = [
        {
            "question": "What is the largest planet in our solar system?",
            "options": [
                "A. Earth",
                "B. Mars",
                "C. Jupiter",
                "D. Saturn",
            ],
            "answer": "C",
        },
        {
            "question": "What is the capital of France?",
            "options": [
                "A. Berlin",
                "B. Madrid",
                "C. Paris",
                "D. Rome",
            ],
            "answer": "C",
        },
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "How many days are there in a leap year?",
            "options": ["A. 365", "B. 366", "C. 364", "D. 367"],
            "answer": "B"
        },
        {
            "question": "Who is known as the Father of the Nation in India?",
            "options": ["A. Nehru", "B. Subhash Chandra Bose", "C. Mahatma Gandhi", "D. Sardar Patel"],
            "answer": "C"
        },
        {
            "question": "Which animal is called the 'Ship of the Desert'?",
            "options": ["A. Horse", "B. Camel", "C. Donkey", "D. Elephant"],
            "answer": "B"
        },
        {
            "question": "Which gas do plants absorb from the air?",
            "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Hydrogen", "D. Nitrogen"],
            "answer": "B"
        },
        {
            "question": "Which festival is known as the Festival of Lights?",
            "options": ["A. Holi", "B. Eid", "C. Diwali", "D. Christmas"],
            "answer": "C"
        },
        {
            "question": "How many players are there in a cricket team?",
            "options": ["A. 10", "B. 11", "C. 12", "D. 9"],
            "answer": "B"
        },
        {
            "question": "Which part of the plant conducts photosynthesis?",
            "options": ["A. Stem", "B. Root", "C. Leaf", "D. Flower"],
            "answer": "C"
        },
        {
            "question": "Which is the smallest continent in the world?",
            "options": ["A. Asia", "B. Europe", "C. Australia", "D. Antarctica"],
            "answer": "C"
        },
        {
            "question": "Which is the national bird of India?",
            "options": ["A. Peacock", "B. Eagle", "C. Sparrow", "D. Parrot"],
            "answer": "A"
        },
        {
            "question": "Which is the longest river in the world?",
            "options": ["A. Ganga", "B. Amazon", "C. Nile", "D. Yangtze"],
            "answer": "C"
        },
        {
            "question": "How many colors are there in the rainbow?",
            "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
            "answer": "B"
        },
        {
            "question": "Which organ pumps blood in the human body?",
            "options": ["A. Brain", "B. Kidney", "C. Heart", "D. Liver"],
            "answer": "C"
        },
        {
            "question": "What is the main source of energy for Earth?",
            "options": ["A. Moon", "B. Fire", "C. Sun", "D. Water"],
            "answer": "C"
        },
        {
            "question": "How many legs does a spider have?",
            "options": ["A. 6", "B. 8", "C. 4", "D. 10"],
            "answer": "B"
        },
        {
            "question": "What is H2O commonly known as?",
            "options": ["A. Salt", "B. Sugar", "C. Water", "D. Acid"],
            "answer": "C"
        },
        {
            "question": "Which Indian city is known as the Pink City?",
            "options": ["A. Delhi", "B. Jaipur", "C. Jodhpur", "D. Udaipur"],
            "answer": "B"
        },
        {
            "question": "Which month has the least number of days?",
            "options": ["A. January", "B. February", "C. April", "D. June"],
            "answer": "B"
        },
        {
            "question": "What is the name of our galaxy?",
            "options": ["A. Milky Way", "B. Andromeda", "C. Mars", "D. Sunlight"],
            "answer": "A"
        },
        {
            "question": "Which fruit has its seeds on the outside?",
            "options": ["A. Banana", "B. Apple", "C. Strawberry", "D. Mango"],
            "answer": "C"
        },
        {
            "question": "Which is the fastest land animal?",
            "options": ["A. Tiger", "B. Horse", "C. Cheetah", "D. Leopard"],
            "answer": "C"
        },
        {
            "question": "What is the boiling point of water in Celsius?",
            "options": ["A. 90°C", "B. 100°C", "C. 120°C", "D. 80°C"],
            "answer": "B"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["A. India", "B. Japan", "C. China", "D. Thailand"],
            "answer": "B"
        },
        {
            "question": "How many hours are there in a day?",
            "options": ["A. 24", "B. 12", "C. 48", "D. 36"],
            "answer": "A"
        },
        {
            "question": "Which festival is known as the Festival of Colors?",
            "options": ["A. Diwali", "B. Holi", "C. Eid", "D. Baisakhi"],
            "answer": "B"
        },
        {
            "question": "Which is the largest animal on land?",
            "options": ["A. Rhino", "B. Elephant", "C. Giraffe", "D. Lion"],
            "answer": "B"
        },
        {
            "question": "What is the currency of India?",
            "options": ["A. Dollar", "B. Rupee", "C. Yen", "D. Peso"],
            "answer": "B"
        },
        {
            "question": "Which sense organ helps us to see?",
            "options": ["A. Ears", "B. Skin", "C. Eyes", "D. Nose"],
            "answer": "C"
        },
        {
            "question": "Which shape has 4 equal sides?",
            "options": ["A. Rectangle", "B. Triangle", "C. Circle", "D. Square"],
            "answer": "D"
        },
        {
            "question": "Which animal is known for its black and white stripes?",
            "options": ["A. Zebra", "B. Tiger", "C. Leopard", "D. Panda"],
            "answer": "A"
        },
        {
            "question": "Who was the first Prime Minister of India?",
            "options": ["A. Sardar Patel", "B. Rajendra Prasad", "C. Jawaharlal Nehru", "D. Lal Bahadur Shastri"],
            "answer": "C"
        },
        {
            "question": "What do bees make?",
            "options": ["A. Wax", "B. Butter", "C. Milk", "D. Honey"],
            "answer": "D"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["A. Venus", "B. Earth", "C. Mercury", "D. Mars"],
            "answer": "C"
        },
        {
            "question": "Which is the tallest animal?",
            "options": ["A. Kangaroo", "B. Camel", "C. Giraffe", "D. Elephant"],
            "answer": "C"
        },
        {
            "question": "What does a thermometer measure?",
            "options": ["A. Pressure", "B. Speed", "C. Temperature", "D. Weight"],
            "answer": "C"
        },
        {
            "question": "Which Indian river is considered holy?",
            "options": ["A. Yamuna", "B. Krishna", "C. Ganga", "D. Narmada"],
            "answer": "C"
        },
        {
            "question": "Which bird can mimic human speech?",
            "options": ["A. Crow", "B. Pigeon", "C. Parrot", "D. Eagle"],
            "answer": "C"
        },
        {
            "question": "Which color is made by mixing red and white?",
            "options": ["A. Orange", "B. Purple", "C. Pink", "D. Brown"],
            "answer": "C"
        },
        {
            "question": "How many letters are there in the English alphabet?",
            "options": ["A. 24", "B. 25", "C. 26", "D. 27"],
            "answer": "C"
        },
        {
            "question": "Which organ helps us breathe?",
            "options": ["A. Kidney", "B. Lungs", "C. Liver", "D. Heart"],
            "answer": "B"
        },
        {
            "question": "Which is the biggest ocean in the world?",
            "options": ["A. Indian", "B. Atlantic", "C. Arctic", "D. Pacific"],
            "answer": "D"
        },
        {
            "question": "How many wheels does an auto rickshaw have?",
            "options": ["A. 2", "B. 3", "C. 4", "D. 6"],
            "answer": "B"
        },
        {
            "question": "Which Indian state is famous for tea gardens?",
            "options": ["A. Gujarat", "B. Kerala", "C. Assam", "D. Punjab"],
            "answer": "C"
        },
        {
            "question": "Which device is used to type letters on a computer?",
            "options": ["A. Monitor", "B. Mouse", "C. Keyboard", "D. Printer"],
            "answer": "C"
        },
        {
            "question": "Which festival marks the end of Ramadan?",
            "options": ["A. Bakrid", "B. Holi", "C. Eid-ul-Fitr", "D. Diwali"],
            "answer": "C"
        },
        {
            "question": "What is the color of an emerald?",
            "options": ["A. Blue", "B. Red", "C. Green", "D. Yellow"],
            "answer": "C"
        },
        {
            "question": "Which vegetable is known as the king of vegetables in India?",
            "options": ["A. Potato", "B. Brinjal", "C. Tomato", "D. Onion"],
            "answer": "B"
        },
        {
            "question": "Who invented the light bulb?",
            "options": ["A. Newton", "B. Einstein", "C. Thomas Edison", "D. Galileo"],
            "answer": "C"
        },
        {
            "question": "Which Indian state is famous for backwaters?",
            "options": ["A. Goa", "B. Kerala", "C. Tamil Nadu", "D. Maharashtra"],
            "answer": "B"
        }
    ]
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['question']}")
        for opt in q['options']:
            print(opt)
        user_ans = input("Your answer (A/B/C/D): ").strip().upper()

        if user_ans == q["answer"]:
            print(" Correct answer!Keep up the good work!")
            score += 1
        else:
            print(f" Wrong! Correct answer is {q['answer']}. No worries, you can try again next time!")

    print(f"\n Your final score is: {score}/{len(questions)}")
    if score in range(6, len(questions)):
        print("You did great!You can improve even more!")
    else:
        print("You have a amazing score!Keep it up!")

def play_math_game():
    choice = str(simpledialog.askstring("Math Game", "Choose: addition, subtraction, multiplication, division")).lower()
    if choice == "addition":
        a, b = random.randint(1, 999), random.randint(1, 999)
        answer = simpledialog.askinteger("Math Game", f"What's {a} + {b}?")
        if answer == a + b:
            messagebox.showinfo("Correct!", "Well done.")
        else:
            messagebox.showinfo("Oops!", f"Correct answer: {a + b}")
    elif choice == "subtraction":
        a, b = random.randint(1, 999), random.randint(1, 999)
        answer = simpledialog.askinteger("Math Game", f"What's {a} - {b}?")
        if answer == a - b:
            messagebox.showinfo("Correct!", "Well done.")
        else:
            messagebox.showinfo("Oops!", f"Correct answer: {a - b}")
    elif choice == "multiplication":
        a, b = random.randint(1, 99), random.randint(1, 99)
        answer = simpledialog.askinteger("Math Game", f"What's {a} × {b}?")
        if answer == a * b:
            messagebox.showinfo("Correct!", "Well done.")
        else:
            messagebox.showinfo("Oops!", f"Correct answer: {a * b}")
    elif choice == "division":
        a, b = random.randint(1, 99), random.randint(1, 99)
        answer = simpledialog.askinteger("Math Game", f"What's {a * b} ÷ {b}?")
        if answer == a * b // b:
            messagebox.showinfo("Correct!", "Well done.")
        else:
            messagebox.showinfo("Oops!", f"Correct answer: {a * b // b}")
    else:
        messagebox.showinfo("Math Game", "Invalid choice.")

def play_rock_paper_scissors():
    result = random.choice(['Rock', 'Paper', 'Scissors'])
    messagebox.showinfo("Rock Paper Scissors", f"You got: {result}")

def roll_dice():
    roll = random.randint(1, 6)
    messagebox.showinfo("Roll Dice", f"You rolled a {roll}!")

def show_compass():
    direction = random.choice(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
    messagebox.showinfo("Compass", f"Direction: {direction}")

def play_target_tap():
    messagebox.showinfo("Target Tap", "Target Tap game coming soon!")

def show_battery():
    global BATTERY_LEVEL
    messagebox.showinfo("Battery Status", f"Battery: {BATTERY_LEVEL}%")


def puzzle_game():
    messagebox.showinfo("Puzzle Game", "Puzzle solving coming soon!")

APPS = {
    "🕹️ Guess Number": play_guess_number,
    "🎲 Roll Dice": roll_dice,
    "✂️ Rock Paper Scissors": play_rock_paper_scissors,
    "🔋 Battery": show_battery,
    "🧭 Compass": show_compass,
    "🎯 Target Tap": play_target_tap,
    "🐍 Snake Game": snake_game,
    "💡 Math Game": play_math_game,
    "🧩 Puzzle": puzzle_game
}

def launch_lock_screen():
    def check_pass():
        if pass_entry.get() == PASSCODE:
            lock.destroy()
            launch_home_screen()
        else:
            messagebox.showerror("Wrong", "Incorrect Passcode!")

    lock = tk.Tk()
    lock.title("iPhone Lock Screen")
    lock.geometry("400x700")
    lock.configure(bg="black")

    tk.Label(lock, text="🔒 Enter Passcode", font=("Helvetica", 20), bg="black", fg="white").pack(pady=50)
    pass_entry = tk.Entry(lock, font=("Helvetica", 18), show="*", justify="center")
    pass_entry.pack(pady=10)
    tk.Button(lock, text="Unlock", font=("Helvetica", 16), command=check_pass).pack(pady=20)

    lock.mainloop()

def update_battery(icon, root):
    global BATTERY_LEVEL, CHARGING
    if CHARGING:
        if BATTERY_LEVEL < 100:
            BATTERY_LEVEL += 1
    else:
        if BATTERY_LEVEL > 0:
            BATTERY_LEVEL -= 1
        elif BATTERY_LEVEL == 0:
            icon.config(text="🔋 0% - Please charge!", fg="red")
            icon.after(3000, lambda: update_battery(icon, root))
            return

    display = f"🔋 {BATTERY_LEVEL}%"
    if CHARGING:
        display += " ⚡"
    icon.config(text=display, fg="white")
    icon.after(3000, lambda: update_battery(icon, root))

def launch_home_screen():
    root = tk.Tk()
    root.title("iPhone Home")
    root.geometry("400x700")
    root.configure(bg="#1C1C1E")

    tk.Label(root, text="🏠 Home Screen", font=("Helvetica", 20), bg="#1C1C1E", fg="white").pack(pady=10)

    battery_icon = tk.Label(root, text=f"🔋 {BATTERY_LEVEL}%", font=("Helvetica", 12), fg="white", bg="#1C1C1E")
    battery_icon.place(x=290, y=10)
    update_battery(battery_icon, root)

    def toggle_charge():
        global CHARGING
        CHARGING = not CHARGING
        messagebox.showinfo("Charging", "Charging Started ⚡" if CHARGING else "Charging Stopped")

    tk.Button(root, text="⚡ Plug In", command=toggle_charge, bg="gray", fg="white").place(x=290, y=40)

    row, col = 0, 0
    for name, func in APPS.items():
        btn = tk.Button(root, text=name, width=14, height=3, command=func, bg="white", fg="black")
        btn.place(x=20 + (col * 170), y=100 + (row * 100))
        col += 1
        if col >= 2:
            col = 0
            row += 1

    root.mainloop()

if __name__ == "__main__":
    launch_lock_screen()
