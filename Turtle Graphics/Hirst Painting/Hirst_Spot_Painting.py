# import colorgram
#
# colors = colorgram.extract("hirst-spot-painting.jpg",30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle
import random

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
timmy.hideturtle()
turtle.colormode(255)


color_list = [(199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), (28, 80, 59), (194, 190, 192), (17, 78, 98), (213, 184, 173), (145, 116, 121), (176, 197, 202)]

x = -250
y = -250
timmy.shape("turtle")
for _ in range(10):
    timmy.teleport(x,y)
    for _ in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    y+=50

screen = turtle.Screen()
screen.exitonclick()