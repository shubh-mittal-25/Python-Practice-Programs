import turtle

timmy = turtle.Turtle()

screen = turtle.Screen()

def forward():
    timmy.forward(10)

def backward():
    timmy.backward(10)

def left():
    timmy.left(10)

def right():
    timmy.right(10)

def clear_screen():
    timmy.reset()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()