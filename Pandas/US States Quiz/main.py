import turtle

screen = turtle.Screen()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # Code to get mouse click coordinates on the image
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

answer_state = screen.textinput(title="Guess the state", prompt="Enter a state's name : ")


turtle.mainloop()
