import turtle

turtle.Screen().bgcolor("lightgreen")
turtle.Screen().setup(300, 400)
turtle.title("Maze in turtle library")
my_pen = turtle.Turtle()

size = 0
num = int(input("Enter the number of squares you want in the maze: "))
while num > 0:
    for i in range(4):
        my_pen.forward(size+1)
        my_pen.left(90)
        size = size - 5
        size = size + 1
        num = num -1
        if num == -1:
            break
turtle.done()