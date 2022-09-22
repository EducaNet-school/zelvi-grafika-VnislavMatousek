import turtle

def spirála(): 
    turtle.color("orange")
    turtle.speed(8)
    turtle.pensize(8)
    turtle.goto(0,0)
    for a in range(30):
        turtle.forward(1+a)
        turtle.left(30)

spirála() 

