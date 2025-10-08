import turtle 
turtle.Screen().bgcolor("aqua")
b = turtle.Turtle()
#first triangle
#base
b.forward(100)

b.left(120)
b.forward(100)
b.left(120)
b.forward(100)

#move to new position
b.penup()
b.right(150)
b.forward(50)
#sceond triangle
b.pendown()

b.right(90)
b.forward(100)
b.right(120)
b.forward(100)
b.right(120)
b.forward(100)


turtle.done()