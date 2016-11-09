import turtle
i = 1
while True:
    if i % 2 == 0:
        turtle.color('blue')
    if i % 2 != 0:
        turtle.color('red')
    turtle.left(i % 48)
    turtle.forward(10)
    i += 1