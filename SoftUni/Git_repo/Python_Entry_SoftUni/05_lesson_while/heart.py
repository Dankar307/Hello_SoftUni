import turtle

turtle.pensize(7)


def draw_heart_curve():
    for i in range(150):
        turtle.right(1.5)
        turtle.forward(1.5)


turtle.color("black", "black")

turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)
draw_heart_curve()

turtle.left(121)
draw_heart_curve()
turtle.forward(111.65)

turtle.end_fill()


turtle.fillcolor('red')
turtle.hideturtle()
turtle.done()