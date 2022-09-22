import turtle 

def ctverecB():
    turtle.speed(8)
    turtle.pensize(8)
    turtle.color("orange")

    for a in range(4):
        turtle.forward(90)
        turtle.left(90)

    turtle.penup()
    turtle.goto(200,0)
    turtle.pendown()


    for a in range(4):
        turtle.forward(90)
        turtle.left(90)

ctverecB()
