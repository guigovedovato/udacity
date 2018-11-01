import turtle

def draw_factory(shape, color, speed):
    draw = turtle.Turtle()
    draw.shape(shape)
    draw.color(color)
    draw.speed(speed)
    return draw

def draw_square(draw, distance):
    for x in range(4):
        draw.forward(distance)
        draw.right(90)

def draw_circle(draw, angle):
    draw.circle(angle)

def draw_triangle(draw, distance, angle):
    for x in range(3):
        draw.forward(distance)
        draw.left(angle)

def draw_clicle_square(draw, distance):
    for x in range(36):
        draw_square(draw, distance)
        draw.right(10)

window = turtle.Screen()
window.bgcolor("white")

draw_square(draw_factory("turtle", "yellow", 2), 100)
draw_circle(draw_factory("turtle", "blue", 4), 65)
draw_triangle(draw_factory("turtle", "green", 6), 100, 120)

draw_clicle_square(draw_factory("turtle", "red", 20), 100)

window.exitonclick()
