from turtle import Turtle, Screen

screen = Screen()
screen.title("Hi Rave!")

rave = Turtle()
rave.shape("turtle")
rave.color("blue")

for _ in range(15):
    rave.forward(10)
    rave.penup()
    rave.forward(10)
    rave.pendown()

screen.exitonclick() 