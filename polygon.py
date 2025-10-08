import turtle

turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(300, 400)
turtle.title("Drawing a polygon in turtle library")
polygon = turtle.Turtle()

num_of_sides = 2
side_length = 80
angle = 360 / num_of_sides

for i in range(num_of_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()