import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import json
import os
import random

# ---------- Configuration and Theme ----------
CONFIG_FILE = "config.json"
CONTACT_FILE = "contacts.json"
NOTES_FILE = "notes.json"
MSG_FILE = "messages.json"
PASSCODE = "1234"

PAGES = []  # For page swiping
CURRENT_PAGE = 0

DOCK_APPS = ["📞 Phone", "💬 Messages", "🌍 Browser", "🎵 Music"]

FOLDERS = {
    "📁 Utilities": ["🧮 Calculator", "⚙️ Settings", "⏰ Clock", "🧭 Compass", "🔋 Battery", "📍 Location"],
    "🧠 Knowledge": ["🧠 Memory", "📋 Clipboard", "📡 News", "📅 Calendar", "🎙️ Siri"],
    "📚 Tools": ["📓 Reminders", "🎯 Focus", "🪞 Mirror", "📷 Camera"],
    "🎮 Games": ["🕹️ Guess Number", "🧠 Quiz Game", "🪙 Toss Coin", "🎲 Roll Dice",
                 "✂️ Rock Paper Scissors", "🐍 Snake Game", "🧩 Puzzle", "💡 Math Game",
                 "🚗 Reaction Game", "🔠 Word Scramble", "🧠 Simon Memory", "🎯 Target Tap",
                 "🧱 Brick Breaker", "🧠 Number Memory", "🔢 Quick Math", "🧩 Tile Slider",
                 "🎯 Dart Flick", "🎮 Reflex Tap", "🕹️ Mini Shooter", "🔍 Hidden Object",
                 "🎯 Bullseye", "🏁 Speed Tap", "👀 Find Pair", "🧮 Quick Count",
                 "🧠 Brain Trainer", "🎳 Bowling Flick", "🧩 Logic Match", "🧠 Memory Grid",
                 "🔐 Lock Pick", "🔤 Type Race"]
}

FOLDERS["📚 Tools"] += [
    "🗂️ File Manager", "🧾 Budget Tracker", "📋 To-Do List", "⏳ Pomodoro Timer", "📑 PDF Viewer",
    "🖼️ Image Gallery", "📁 Zip Manager", "🔍 File Search", "📊 Charts Viewer", "📅 Weekly Planner",
    "📋 Clipboard History", "📬 Email Client", "📦 Inventory Tracker", "📎 Notes Sync", "🔐 Password Vault",
    "📈 Finance Graphs", "📤 Upload Manager", "📝 Meeting Notes", "📅 Habit Tracker", "🗓️ Schedule Builder"
]

FOLDERS["🧠 Knowledge"] += [
    "✏️ Drawing Pad", "🧮 Math Solver", "🔬 Science Facts", "🗺️ World Map", "🧪 Periodic Table",
    "📚 Dictionary", "📖 Story Reader", "📐 Geometry Tools", "📊 Grade Calculator", "🧠 IQ Test",
    "📈 Data Analyzer", "🖥️ Coding Lab", "🌌 Astronomy Viewer", "📖 Language Learner", "🔢 Prime Finder",
    "🧬 DNA Explorer", "📊 Survey Tool", "🎓 Exam Prep", "📙 Encyclopedia", "🗣️ Speech Practice"
]

BATTERY_LEVEL = random.randint(30, 100)
WALLPAPER_COLOR = "#202020"
NOTIFICATIONS = []
APP_BADGES = {"💬 Messages": 1, "📡 News": 2}

APP_FUNCTIONS = {}

# ---------- Game Placeholders (New Games) ----------
def open_bullseye():
    messagebox.showinfo("Bullseye", "Hit the center! (placeholder)")

def open_speed_tap():
    messagebox.showinfo("Speed Tap", "Tap rapidly! (placeholder)")

def open_find_pair():
    messagebox.showinfo("Find Pair", "Match cards! (placeholder)")

def open_quick_count():
    messagebox.showinfo("Quick Count", "Count fast! (placeholder)")

def open_brain_trainer():
    messagebox.showinfo("Brain Trainer", "Train your brain! (placeholder)")

def open_bowling_flick():
    messagebox.showinfo("Bowling Flick", "Flick the ball to strike! (placeholder)")

def open_logic_match():
    messagebox.showinfo("Logic Match", "Match logic pairs! (placeholder)")

def open_memory_grid():
    messagebox.showinfo("Memory Grid", "Remember the tiles! (placeholder)")

def open_lock_pick():
    messagebox.showinfo("Lock Pick", "Pick the lock! (placeholder)")

def open_type_race():
    messagebox.showinfo("Type Race", "Type fast to win! (placeholder)")

# ---------- Utility App Examples ----------
def open_calculator():
    try:
        expr = simpledialog.askstring("Calculator", "Enter expression:")
        if expr:
            result = eval(expr)
            messagebox.showinfo("Result", f"Result: {result}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_notes():
    note = simpledialog.askstring("Notes", "Write a note:")
    if note:
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        messagebox.showinfo("Saved", "Note saved!")

APP_FUNCTIONS.update({
    "🎯 Bullseye": open_bullseye,
    "🏁 Speed Tap": open_speed_tap,
    "👀 Find Pair": open_find_pair,
    "🧮 Quick Count": open_quick_count,
    "🧠 Brain Trainer": open_brain_trainer,
    "🎳 Bowling Flick": open_bowling_flick,
    "🧩 Logic Match": open_logic_match,
    "🧠 Memory Grid": open_memory_grid,
    "🔐 Lock Pick": open_lock_pick,
    "🔤 Type Race": open_type_race,

    "🧮 Calculator": open_calculator,
    "📓 Reminders": open_notes,
    "📝 Meeting Notes": open_notes,
    "📎 Notes Sync": open_notes
})

# ---------- Start App ----------
def launch_lock_screen():


 if __name__ == "__main__":
    launch_lock_screen()
