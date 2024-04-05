#task1-create a screen, change title, add background colour and set width & height
#of the screen
#task2- create a turtle player
#task3- set key binds for left,right
#task4- increase and decrease speed
#task5- create play space(ground)
#task6-make sure player cant go out of play space
#task 7- create a goal

import turtle
import math
import random

#create a screen
win = turtle.Screen()
win.title('A Simple Game')
win.bgcolor('black')
win.setup(1200,720)

#create a field
ground=turtle.Turtle()
ground.penup()
ground.setposition(-500,-300)
ground.pendown()
ground.pensize(3)

ground.color('lime')
ground.begin_fill()
for i in range(2):
    ground.forward(1000)
    ground.left(90)
    ground.forward(600)
    ground.left(90)
ground.end_fill()
ground.hideturtle()
#creating player

player = turtle.Turtle()
player.pensize(0)
player.shape('turtle')
player.shapesize(2,2)
player.penup()

#create goal
goal = turtle.Turtle()
goal.speed(0)
goal.shape('circle')
goal.pensize('2')
goal.color('orange')
goal.penup()
goal.setposition(random.randint(-500,+500), random.randint(-300,+300))

#functions
def turnLeft():
    player.left(30)

def turnRight():
    player.right(30)

def increaseSpeed():
    global speed
    speed=speed+2
    
    
def decreaseSpeed():
    global speed
    if speed > 2:
        speed = speed-2
    else:
        speed = 1

# setting key binds
turtle.listen()

turtle.onkey( turnLeft , 'Left')
turtle.onkey(turnRight, 'Right')
#turtle.onkey(increseSpeed, 'Up')
#turtle.onkey(decreaseSpeed, 'Down')

speed=2

while True:
    player.forward(speed)

#check for border collision
    if player.xcor() <-495 or player.xcor() >495 or player.ycor()<-295 or player.ycor()>295:
        player.setposition(0,0)
        decreaseSpeed()

#check for goal collision
    d = math.sqrt( ((goal.xcor()-player.xcor())**2) +((goal.ycor()-player.ycor())**2))
    if d < 20 :
        goal.setposition(random.randint(-500,+500), random.randint(-300,+300))      
        increaseSpeed()
