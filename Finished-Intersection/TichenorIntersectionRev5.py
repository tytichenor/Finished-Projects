import turtle as t 
from turtle import *
turt = t.Turtle()
t.Screen().bgcolor("gray")
turt.speed(100)
turt.hideturtle()

def yellowLines():
    turt.pensize(20)
    turt.pencolor("yellow")
    turt.goto(0,400)
    turt.pendown()
    turt.goto(0,-400)
    turt.penup()
    turt.goto(-400,0)
    turt.pendown()
    turt.goto(400,0)
    turt.pensize(8)
    turt.pencolor("gray")
    turt.goto(0,400)
    turt.pendown()
    turt.goto(0,-400)
    turt.penup()
    turt.goto(-400,0)
    turt.pendown()
    turt.goto(400,0)
    turt.penup()

def dashedWhiteLines():
    turt.pencolor("white")
    turt.pensize(5)
    ycord=-400
    for x in range(20):
        turt.goto(-60,ycord)
        turt.pendown()
        ycord+=40
        turt.goto(-60,ycord)
        turt.penup()
        ycord+=40
        turt.goto(-60,ycord)
    ycord=-400
    for x in range(20):
        turt.goto(60,ycord)
        turt.pendown()
        ycord+=40
        turt.goto(60,ycord)
        turt.penup()
        ycord+=40
        turt.goto(60,ycord)
    xcord=-400
    for x in range(20):
        turt.goto(xcord,-60)
        turt.pendown()
        xcord+=40
        turt.goto(xcord,-60)
        turt.penup()
        xcord+=40
        turt.goto(xcord,-60)
    xcord=-400
    for x in range(20):
        turt.goto(xcord,60)
        turt.pendown()
        xcord+=40
        turt.goto(xcord,60)
        turt.penup()
        xcord+=40
        turt.goto(xcord,60)
    turt.penup()

def solidBlackLines():
    turt.pencolor("black")
    turt.goto(-400,120)
    turt.pendown()
    turt.goto(-120,120)
    turt.goto(-120,400)
    turt.penup()
    turt.goto(400,120)
    turt.pendown()
    turt.goto(120,120)
    turt.goto(120,400)
    turt.penup()
    turt.goto(400,-120)
    turt.pendown()
    turt.goto(120,-120)
    turt.goto(120,-400)
    turt.penup()
    turt.goto(-400,-120)
    turt.pendown()
    turt.goto(-120,-120)
    turt.goto(-120,-400)
    turt.penup()

def greyBox():
    turt.pencolor("grey")
    turt.fillcolor("grey")
    turt.goto(-120,120)
    turt.pendown()
    turt.begin_fill()
    turt.goto(120,120)
    turt.goto(120,-120)
    turt.goto(-120,-120)
    turt.goto(-120,120)
    turt.end_fill()


yellowLines()
dashedWhiteLines()
solidBlackLines()
greyBox()

#############################################################################################################


# create two empty lists of turtles, adding to them later
horizontalTurts = []
verticalTurts = []

# make the red dot 
redDot=Turtle("circle")
redDot.hideturtle()
redDot.fillcolor("red")
redDot.penup()

# use interesting shapes and colors
turtleShapes = ["turtle", "turtle"]
horizColors = ["blue", "blue", "blue", "blue", "blue", "blue","blue","blue"]
vertColors = ["blue", "blue", "blue", "blue", "blue", "blue","blue","blue"]
spacing1=-90
spacing2=30
spacing3=-90
spacing4=30
for shape in turtleShapes:
    ht=Turtle(shape=shape)
    horizontalTurts.append(ht)
    ht.penup()
    ht.speed(1)
    ht.fillcolor(horizColors.pop())
    # x cord is less than 300 to force collision
    ht.goto(-250,spacing1)
    ht.setheading(0)
    vt=Turtle(shape=shape)
    verticalTurts.append(vt)
    vt.penup()
    vt.speed(0)
    vt.fillcolor(vertColors.pop())
    vt.goto(-spacing2,300)
    vt.setheading(270)
    ht1=Turtle(shape=shape)
    horizontalTurts.append(ht1)
    ht1.penup()
    ht1.speed(1)
    ht1.fillcolor(horizColors.pop())
    ht1.goto(300,-spacing1)
    ht1.setheading(-180)
    vt1=Turtle(shape=shape)
    verticalTurts.append(vt1)
    vt1.penup()
    vt1.speed(0)
    vt1.fillcolor(vertColors.pop())
    vt1.goto(spacing4,-300)
    vt1.setheading(-270)
    spacing1+=60
    spacing2+=60
    spacing3+=60
    spacing4+=60

    
distanceToMove=5
collisionDistance=60

for step in range(200):
    for h in horizontalTurts:
        for v in verticalTurts:
            h.fd(distanceToMove)
            v.fd(distanceToMove)
        # check for collision
        if (abs(h.xcor() - v.xcor()) < collisionDistance):
            if (abs(h.ycor()-v.ycor()) < collisionDistance):
                print("collided!")
                h.hideturtle()
                v.hideturtle()
                # show the red dot
                redDot.goto(h.xcor(),h.ycor())
                redDot.showturtle()

wn=t.Screen()
wn.mainloop()
