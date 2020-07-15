import turtle

painter = turtle.Turtle()
turtle.bgcolor('black')
painter.pencolor('blue')

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time

painter.pencolor('green')
for i in range(50):
    painter.forward(100)
    painter.left(123)

turtle.done()