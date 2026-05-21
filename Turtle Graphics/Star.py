import turtle
import random
from turtle_colors import colors_against_white

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.pensize(4)
timmy.teleport(-150,0)
for _ in range(5):
    timmy.color(random.choice(colors_against_white))
    timmy.forward(300)
    timmy.right(144)

screen = turtle.Screen()
screen.exitonclick()


