print("test")
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

'''
#angles, degrees
tina.left(270)
tina.right(90)
tina.setheading(0)

#draw circle, semi circle, arc
tina.circle(100)
tina.circle(100, 90)



#color
tina.fillcolor ("yellow")
tina.begin_fill()
tina.circle(50)
tina.end_fill()

#stamp
tina.stamp()
tina.forward(100)
tina.stamp()
tina.forward(100)

'''

#body
tina.setheading(270)
tina.begin_fill()
tina.circle(50, 180)
tina.forward(80)
tina.circle(50, 180)
tina.forward(80)
tina.end_fill()

#belly
tina.goto (10,0)
tina.fillcolor("white")
tina.begin_fill()
tina.circle(40)
tina.end_fill()

#eyes
tina.goto(30, 80)
tina.setheading(0)
tina.fillcolor("white")
tina.begin_fill()
tina.circle(20)
tina.end_fill()
tina.goto(70, 80)
tina.fillcolor("white")
tina.begin_fill()
tina.circle(20)
tina.end_fill()

tina.shape("circle")
tina.fillcolor("black")
tina.penup()
tina.goto(30,100)
tina.stamp()
tina.goto (70,100)
tina.stamp()

#beak
tina.shape("triangle")
tina.fillcolor("orange")
tina.goto(50, 70)
tina.setheading(270)
tina.stamp()

#flippers
tina.fillcolor("black")
tina.pencolor("white")
tina.goto(0,50)
tina.setheading(0)
tina.stamp()
tina.fillcolor("black")
tina.pencolor("white")
tina.goto(100,50)
tina.setheading(180)
tina.stamp()

#feet
tina.shape("square")
tina.fillcolor("orange")
tina.goto(30,-50)
tina.stamp()
tina.shape("square")
tina.fillcolor("orange")
tina.goto(70,-50)
tina.stamp()
