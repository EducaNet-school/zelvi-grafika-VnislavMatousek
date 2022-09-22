import turtle

def polygon(): 
    sides = int(input("sides: "))
    lenght = int(input("lenght:"))

    turtle.speed(8)
    turtle.pensize(8)
    turtle.goto(0,0)
    turtle.color("orange")

    for a in range(sides):
        turtle.forward(lenght)
        turtle.left(360/sides)

polygon()
