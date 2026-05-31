import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Indian States Quiz")
image = "india_states_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states_name.csv")
all_states = data.State.to_list()
guessed_states = []

# # Code to get mouse click coordinates on the image
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct", prompt="Enter a state's name : ")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        pointer = turtle.Turtle()
        pointer.hideturtle()
        pointer.penup()
        pointer.color("red")
        state_data = data[data.State == answer_state]
        pointer.goto(state_data.x.item(), state_data.y.item())
        pointer.write(answer_state)

turtle.mainloop()