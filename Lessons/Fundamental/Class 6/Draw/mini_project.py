import turtle

def draw_flower():
    windows = turtle.Screen()
    windows.bgcolor("white")

    pen = turtle.Turtle()
    pen.color("violet")
    pen.speed(10)

    for i in range(12):
        pen.forward(100)
        pen.right(120)
        pen.forward(30)
        pen.right(90)
        pen.forward(30)
    
    pen.forward(31)
    pen.right(90)
    pen.forward(200)

    windows.exitonclick()

draw_flower()