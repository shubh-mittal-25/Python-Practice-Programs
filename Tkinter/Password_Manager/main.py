from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_textField.delete(0, END)
    password_textField.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_textField.get()
    email = email_textField.get()
    password_text = password_textField.get()
    new_data = {
        website_name : {
            "email" : email,
            "password" : password_text,
        }
    }
    if website_name == "" or email == "" or password_text == "":
        messagebox.showerror("Error", "Please enter all fields")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_textField.delete(0, "end")
            password_textField.delete(0, "end")

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    website_name = website_textField.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found")
    else:
        if website_name in data:
            messagebox.showinfo(website_name, f"Email/Username : {data[website_name]["email"]}\n"
                                              f"Password : {data[website_name]["password"]}\n")
            pyperclip.copy(data[website_name]["password"])
        else:
            messagebox.showinfo("Not Found", f"No details for {website_name} exists")

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
website_textField = Entry(width=32)
website_textField.focus()
website_textField.grid(column=1, row=1)
email_textField = Entry(width=50)
email_textField.insert(0, "shubh_mittal_125")
email_textField.grid(column=1, row=2, columnspan=2)
password_textField = Entry(width=32)
password_textField.grid(column=1, row=3)

#BUTTONS
gen_pass_button = Button(text="Generate Password" , command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width = 43, command = save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width = 14, command=search)
search_button.grid(column=2, row=1)

window.mainloop()