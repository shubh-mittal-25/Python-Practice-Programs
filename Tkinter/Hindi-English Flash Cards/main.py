from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/Hindi_to_English.csv")
to_learn = data.to_dict(orient="records")

# <----------------------------NEW FLASH CARDS------------------------------->
def flash_card():
    current_card = random.choice(to_learn)
    word = current_card["Hindi"]
    canvas.itemconfig(Hindi_text, text="Hindi")
    canvas.itemconfig(Hindi_word, text=word)

# <----------------------------UI DESIGN------------------------------------->
window = Tk()
window.title("Hindi to English Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

#FLASHCARD
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 265, image=flashcard_img)
Hindi_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel",40,"italic"))
Hindi_word = canvas.create_text(400, 293, text="", fill="black", font=("Ariel",60,"bold"))
canvas.grid(row=0, column=0, columnspan=2)

#BUTTONS
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=flash_card)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR,highlightthickness=0, command=flash_card)
wrong_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=1)

flash_card()

window.mainloop()

