from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
DELAY = 5

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Hindi_to_English.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}
# <----------------------------NEW FLASH CARDS------------------------------->
def countdown(seconds):
    countdown_label.config(text=str(seconds))
    if seconds > 0:
        timer = window.after(1000, countdown, seconds - 1)
    else:
        countdown_label.config(text="Correct?")
        flip_card()

def flash_card():
    global current_card
    current_card = random.choice(to_learn)
    new_word = current_card["Hindi"]
    canvas.itemconfig(lang_text, text="Hindi", fill="black")
    canvas.itemconfig(word, text=new_word, fill="black")
    canvas.itemconfig(background, image=hindi_img)
    countdown(5)

# <----------------------------FLIP FLASH CARDS------------------------------->
def flip_card():
    global current_card
    new_word = current_card['English']
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word, text=new_word, fill="white")
    canvas.itemconfig(word, text=new_word)
    canvas.itemconfig(background, image=english_img)

def is_known():
    to_learn.remove(current_card)
    n_data = pandas.DataFrame(to_learn)
    n_data.to_csv("data/words_to_learn.csv", index=False)
    flash_card()
# <----------------------------UI DESIGN------------------------------------->
window = Tk()
window.title("Hindi to English Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


#FLASHCARD
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
hindi_img = PhotoImage(file="images/card_front.png")
english_img = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 265, image=hindi_img)
lang_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 293, text="", fill="black", font=("Ariel",60,"bold"))
canvas.grid(row=0, column=0, columnspan=3)

#BUTTONS
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR,highlightthickness=0, command=flash_card)
wrong_button.grid(row=1, column=2)

countdown_label = Label(text="", font=("Ariel", 50, "bold"), bg=BACKGROUND_COLOR ,fg="green")
countdown_label.grid(row=1, column=1)



flash_card()

window.mainloop()

