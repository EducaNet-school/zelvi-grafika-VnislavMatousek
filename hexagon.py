import turtle

turtle.speed(8)
turtle.pensize(8)
turtle.goto(0,0)
turtle.color("orange")

for a in range(6):
      turtle.forward(100)
      turtle.left(60)

def test():
   turtle.left(60)
   turtle.forward(100)
   turtle.right(120)
   turtle.forward(100)

for i in range(5):
   test()
   turtle.left(120)
