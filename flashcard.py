class flashcard:
    def __init__ (self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__ (self):
        return self.word + '(' + self.meaning + ')'
    
flash = []

while (True):
    word = input("Enter a word: ")
    meaning = input("Enter its meaning: ")
    flash.append(flashcard(word, meaning))

    option = input("Do you want to add more flashcards? (yes/no): ")

    if (option == 'no'):
        break
    else:
        continue
for i in flash:
    print(i)