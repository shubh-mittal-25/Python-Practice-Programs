import turtle

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0,0),(-20,0),(-40,0)]
for position in starting_positions:
    timmy = turtle.Turtle()
    timmy.color("white")
    timmy.shape("square")
    timmy.teleport(position[0],position[1])

screen.exitonclick()