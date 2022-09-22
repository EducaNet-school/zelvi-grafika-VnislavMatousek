import turtle

def spirála():

    a = 5

    for b in range(a*4):
        turtle.forward(b*8)
        turtle.right(90)

spirála()
