import turtle

počet = 20 
šířka = 20 

for a in range(počet+1):
    for b in range(4):
        turtle.pendown()
        turtle.forward(šířka*a)
        turtle.right(90)
    turtle.penup()
    turtle.setpos(turtle.xcor()-šířka/2,turtle.ycor()+šířka/2)


