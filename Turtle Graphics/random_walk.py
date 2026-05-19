import turtle
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

directions = [0 , 90 , 180 , 270]

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
timmy.pensize(10)

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen = turtle.Screen()
screen.exitonclick()




