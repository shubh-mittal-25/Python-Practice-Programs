def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(n):
    while n>0:
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        n-=1

jump(6)