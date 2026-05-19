import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

x = -230
y = -100
for turtle_index in range(6):
    new_turtle = turtle.Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.teleport(x, y)
    turtles.append(new_turtle)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win! the {winning_turtle} turtle is the winner.")
            else:
                print(f"You lose! the {winning_turtle} turtle is the winner.")
        step = random.randint(0,10)
        turtle.penup()
        turtle.forward(step)

screen.exitonclick()