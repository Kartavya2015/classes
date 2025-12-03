class Parrot:
    species = "bird"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a {}.".format(blu.species))
print("Woo is also a {}.".format(woo.species))

print("{} is {} years old.".format(blu.name, blu.age))
print("{} is {} years old.".format(woo.name, woo.age))
