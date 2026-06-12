from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score : 0", bg=THEME_COLOR, fg="white", font = ("Arial",16,"bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,125,
            text="QUESTION",
            fill="black",
            font = ("Arial",20,"italic")
        )
        self.canvas.grid(row=1, column=0, pady=50, columnspan=2)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.false_button = Button(image=false_img , bg=THEME_COLOR , highlightthickness=0)
        self.false_button.grid(row=2, column=1 , padx=20, pady=20)
        self.true_button = Button(image=true_img, bg=THEME_COLOR , highlightthickness=0)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        self.window.mainloop()
