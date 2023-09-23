from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

x = -240
y = -150
turtles = []
colors = ["red", "blue", "green", "purple", "orange"]

# Creates a turtle, assigns a color, and moves them to the starting line
for _ in range(0,5):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[0])
    colors.pop(0)
    turtle.penup()
    turtle.goto(x, y)
    turtles.append(turtle)
    y += 75

user_choice = screen.textinput(title="Place a bet", prompt="Which turtle do you think is going to win?")

# This is to prevent the race from starting early
if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print("You won!")
            else:
                print(f"Sorry, the winning color was: {winning_color}.")    
            
            is_race_on = False

screen.exitonclick()