class person( object ):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(f"name: {self.name}, id: {self.id}")
class employee(person):
    def __init__ (self, name, id, salary, post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, id)

a = employee("Smita", 101, 50000, "Developer")
a.display()