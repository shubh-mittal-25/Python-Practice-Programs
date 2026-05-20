import turtle
import random
from turtle_colors import colors_against_white

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("black","red")

def draw_shapes(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)
    sides += 1

for shape_side in range(3,11):
    timmy.color(random.choice(colors_against_white))
    draw_shapes(shape_side)

screen = turtle.Screen()
screen.exitonclick()


