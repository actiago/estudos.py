import turtle
import math

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color('red')
size=200
turtle.bgcolor('black')

myPen.setheading(90) #Point the top
for i in range(0,6):
  myPen.forward(size)
  myPen.penup()
  myPen.forward(-size)
  myPen.left(60)
  myPen.pendown()

myPen.setheading(90) #Point the top
myPen.forward(size)
myPen.setheading(215) #Point the left
newSize=size
newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(65))
for i in range(0,30):
   myPen.forward(newSize)
   myPen.left(60)
   newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(70))

turtle.done()
