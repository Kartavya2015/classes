import turtle

length = int(input("Enter the length of the sides: "))

turtle.Screen().bgcolor("black")
turtle.Screen().setup(500, 500)
me = turtle.Turtle()
me.color("white")

for i in range(4):
    me.forward(length)
    me.right(90)
    me.forward(length)
    me.right(90) 
    me.forward(length)
    me.right(90)
    me.forward(length)
    me.right(90)
turtle.done()