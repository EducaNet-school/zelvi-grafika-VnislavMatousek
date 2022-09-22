import turtle

def ctverec():
    turtle.speed(8)
    turtle.pensize(8)
    turtle.goto(0,0)
    turtle.color("orange")

    for a in range(4):
        turtle.forward(150)
        turtle.left(90)


ctverec()
