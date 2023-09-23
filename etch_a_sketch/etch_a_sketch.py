from turtle import Turtle, Screen

screen = Screen()
rave = Turtle()

def move_forwards():
    rave.forward(10)

def turn_left():
    rave.left(10)

def turn_right():
    rave.right(10)

def move_backwards():
    rave.backward(10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)

screen.exitonclick()
