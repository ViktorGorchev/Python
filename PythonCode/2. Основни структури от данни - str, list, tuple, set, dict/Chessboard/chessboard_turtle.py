import turtle
side=40
x = 0
y = 0
for row in range(8):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for col in range(8):
        if col % 2 != 0 and row % 2 == 0:
            turtle.begin_fill()
        if col % 2 == 0 and row % 2 != 0:
            turtle.begin_fill()
        for square_side in range(4):
            turtle.forward(side)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)
    y -= side
turtle.exitonclick()