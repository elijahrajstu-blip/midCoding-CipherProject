import turtle

t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()


import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(12):
    for j in range(57):
        t.forward(100)
        t.right(90)
    t.right(30)
    t.color("blue")
    t.pensize(10)


turtle.done()