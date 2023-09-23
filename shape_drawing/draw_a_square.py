from turtle import Turtle, Screen

rave = Turtle()
rave.shape("turtle")
rave.color("blue")

for _ in range(4):
    rave.forward(100)
    rave.right(90)

screen = Screen()

screen.exitonclick() 