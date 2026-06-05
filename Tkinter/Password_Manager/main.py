from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100, bg="white")

canvas = Canvas(width=200, height=200, bg="white" , highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#LABELS
label1 = Label(text="Website : ", bg="white", font=("Arial", 12))
label1.grid(column=0, row=1)
label2 = Label(text="Email/Username : ", bg="white", font=("Arial", 12))
label2.grid(column=0, row=2)
label3 = Label(text="Password : ", bg="white", font=("Arial", 12))
label3.grid(column=0, row=3)

#ENTRY
website_textField = Entry(width=50)
website_textField.grid(column=1, row=1, columnspan=2)
email_textField = Entry(width=50)
email_textField.grid(column=1, row=2, columnspan=2)
password_textField = Entry(width=32)
password_textField.grid(column=1, row=3)

#BUTTONS
gen_pass_button = Button(text="Generate Password")
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width = 43)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()