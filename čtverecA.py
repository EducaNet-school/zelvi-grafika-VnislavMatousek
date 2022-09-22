import turtle 

def ctverecA():
    turtle.speed(8)
    turtle.pensize(8)
    turtle.goto(0,0)
    turtle.color("orange")  

    for a in range(3):
         turtle.right(120)
         for a in range(4):
            turtle.forward(90)
            turtle.left(90)
ctverecA()
