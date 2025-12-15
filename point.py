class Point:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "point({0},{1})".format(self.x, self.y)

p1 = Point(2,3)
p2 = Point(67,99)
p3 = Point(50,-88)
p4 = Point(6,7)
print(p1, p2, p3, p4)