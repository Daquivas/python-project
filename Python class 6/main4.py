import turtle
turtle.Screen().bgcolor("Orange")
# Create a turtle object
pen = turtle.Turtle()

# Draw a triangle
for i in range(3):
    pen.forward(100)
    pen.left(120)

# Move the turtle to a new position for the square
pen.penup()
pen.goto(-150, -100)
pen.pendown()

# Draw a square
for i in range(4):
    pen.forward(100)
    pen.left(90)

# Move the turtle to a new position for the rectangle
pen.penup()
pen.goto(150, 0)
pen.pendown()

# Draw a rectangle
for i in range(2):
    pen.forward(150)
    pen.left(90)
    pen.forward(50)
    pen.left(90)

