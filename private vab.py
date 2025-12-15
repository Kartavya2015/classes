class vab:
    __privateVar = 78
    def _pri (self):
        print("I am inside vab class")

    def hello(self):
        print("Private variable value is:", self.__privateVar)

foo = vab()
foo.hello()
foo._pri()  # Accessing the protected method from outside the class