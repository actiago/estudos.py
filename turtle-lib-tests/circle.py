import turtle

ninja = turtle.Turtle()

colors = [ 'red', 'purple', 'yellow', 'blue', 'green', 'orange' ]

ninja.speed(10)

turtle.bgcolor('black')

for i in range(180):
    ninja.pencolor(colors[i%6])
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()