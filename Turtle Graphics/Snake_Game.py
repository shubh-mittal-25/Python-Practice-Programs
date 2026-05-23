import turtle
import time

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_positions:
    new_segment = turtle.Turtle()
    new_segment.color("white")
    new_segment.shape("square")
    new_segment.penup()
    new_segment.teleport(position[0], position[1])
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1 , 0 , -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].teleport(new_x, new_y)

    segments[0].forward(20)

screen.exitonclick()