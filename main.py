#write in file using with() function
with open('index.html', 'w') as file:
    file.write("Hi! I am penguin and i am 1 year old")
file.close()

with open('index.html', 'r') as file:
    data = file.readlines()
    print(" words are")
    for line in data:
        word = line.split
        print(word)
        file.close