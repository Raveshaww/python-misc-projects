from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(pen, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        pen.color(random_color())
        pen.circle(100)
        pen.setheading(pen.heading() + size_of_gap)

rave = Turtle(visible=False)
rave.speed(0)

screen = Screen()
screen.colormode(255)

draw_spirograph(rave, 5)


screen.exitonclick()