from turtle import Turtle, Screen
import random

rave = Turtle(visible=False)
rave.speed(0)
rave.width(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


screen = Screen()
screen.colormode(255)
screen.screensize(25000,25000)
directions = [0, 90, 180, 270]


for _ in range(200):
    rave.color(random_color())
    rave.right(random.choice(directions))
    rave.forward(50)


screen.exitonclick()