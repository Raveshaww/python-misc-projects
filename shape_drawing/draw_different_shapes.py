from turtle import Turtle, Screen

def draw_shape(pen, sides, angle):
    for _ in range(sides):
        pen.forward(100)
        pen.right(angle)

rave = Turtle(visible=False)
screen = Screen()

# draw triangle
draw_shape(rave, 3, 120)

# draw square
draw_shape(rave, 4, 90)

# draw pentagon
draw_shape(rave, 5, 72)

# draw hexagon
draw_shape(rave, 6, 60)

# draw heptagon
draw_shape(rave, 7, 51.43)

# draw octagon
draw_shape(rave, 8, 45)

# draw nonagon
draw_shape(rave, 9, 40)

# draw decagon
draw_shape(rave, 10, 36)

screen.exitonclick() 