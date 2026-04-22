import turtle

pen = turtle.Turtle()
pen.speed(0)

# Grass
screen = turtle.Screen()
screen.bgcolor("green")

# Sky
pen.penup()
pen.goto(-500, 0)
pen.pendown()
pen.color("deepSkyBlue")
pen.begin_fill()
for i in range(2):
    pen.forward(1000)
    pen.left(90)
    pen.forward(500)
    pen.left(90)
pen.end_fill()

# Sun
pen.penup()
pen.goto(-300, 300)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(35)
pen.end_fill()

 # Cloud
pen.penup()
pen.goto(200, 200)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

pen.penup()
pen.goto(220, 240)
pen.pendown()
pen.begin_fill()
pen.circle(25)
pen.end_fill()

pen.penup()
pen.goto(230, 215)
pen.pendown()
pen.begin_fill()
pen.circle(25)
pen.end_fill()

pen.penup()
pen.goto(180, 225)
pen.pendown()
pen.begin_fill()
pen.circle(25)
pen.end_fill()

# House
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.pensize(3)
pen.color("chocolate", "orange") # (stroke, fill)
pen.begin_fill()
for i in range(4):
    pen.forward(170)
    pen.left(90)
pen.end_fill()

# Chimney
pen.penup()
pen.goto(20, 130)
pen.pendown()
pen.color("brown", "firebrick")
pen.begin_fill()
for i in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
pen.end_fill()

# Roof
pen.penup()
pen.goto(-127, 70)
pen.pendown()
pen.begin_fill()
for i in range(3):
    pen.forward(225)
    pen.left(120)
pen.end_fill()

# Window 1
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("black", "white")
pen.begin_fill()
for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

# Window 1 Cross - horizontal line
pen.penup()
pen.goto(0, 25)
pen.pendown()
pen.color("black")
pen.forward(50)

# Window 1 cross- vertical line
pen.penup()
pen.goto(25, 0)
pen.pendown()
pen.left(90)
pen.forward(50)

# Window 2
pen.penup()
pen.goto(-80, 0)
pen.pendown()
pen.right(90)
pen.color("black", "white")
pen.begin_fill()
for i in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

# window 2 cross horizontal
pen.penup()
pen.goto(-80, 25)
pen.pendown()
pen.color("black")
pen.forward(50)


# window 2 cross vertical line
pen.penup()
pen.goto(-55, 0)
pen.pendown()
pen.left(90)
pen.forward(50)

# door
pen.penup()
pen.goto(-40, -97)
pen.pendown()
pen.right(90)
pen.color("red")
pen.begin_fill()
for i in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
pen.end_fill()

# Door Handle
pen.penup()
pen.goto(-30, -60)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(5)
pen.end_fill()


turtle.done()








