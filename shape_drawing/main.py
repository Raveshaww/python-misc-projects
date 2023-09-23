# import colorgram
from turtle import Turtle, Screen
import random


# Generates the below color_list
# 
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g , b)
#     rgb_colors.append(rgb)
# 
# print(rgb_colors)

color_list = [(46, 52, 64), (230, 234, 240), (72, 82, 103), (133, 175, 199), (153, 189, 163), (94, 128, 171), (191, 97, 106), (208, 135, 112), (180, 142, 173), (235, 203, 139), (232, 221, 215), (223, 209, 218), (218, 227, 219), (56, 62, 73), (188, 191, 198)]

rave = Turtle(visible=False)
rave.penup()

screen = Screen()
screen.colormode(255)

x = -250
y = -250
while y <= 250:
    if x <= 250:
        rave.goto(x, y)
        rave.dot(20, random.choice(color_list))
        x += 50
    else:
        y += 50
        x = -250
        

screen.exitonclick()