from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break" , fg=RED)
    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break" , fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work" , fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,countdown, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark_label.config(text=mark)
# ---------------------------- UI SETUP -----------------------------------#
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50 , bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME , 30 , "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME,50,"bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start" , command=start_timer)
start_button.config(font=(FONT_NAME,10) , highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset")
reset_button.config(font=(FONT_NAME,10) , highlightthickness=0)
reset_button.grid(row=2, column=2)

checkmark_label = Label()
checkmark_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME,15))
checkmark_label.grid(row=3, column=1)

window.mainloop()