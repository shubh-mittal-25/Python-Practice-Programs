from tkinter import *

def convert():
    miles = float(miles_input.get())
    km = miles * 1.60934
    label_answer.configure(text=str(km))

window = Tk()
window.title("Miles to Km converter")
window.config(padx=40, pady=40)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_isequalto = Label(text="is equal to ")
label_isequalto.grid(row=1, column=0)

label_answer = Label(text="0")
label_answer.grid(row=1, column=1)

label_KM = Label(text="Km")
label_KM.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()