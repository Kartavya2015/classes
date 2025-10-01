string = str(input("Enter your word: "))
char = str(input("Enter Your Character: "))

i = 0
count = 0

while (i < len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1
print("The character", char, "occurs", count, "times in the word", string)