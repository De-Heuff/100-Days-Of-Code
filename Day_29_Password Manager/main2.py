from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 6))]

    password_list = password_numbers + password_symbols + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# TODO Create a function called save()

def save():

# TODO Write to the data inside the entries to a data.txt file when add button is clicked
    a = website_entry.get()
    b = user_name_entry.get()
    c = password_entry.get()

    if len(a) or len(c) == 0:
        messagebox.showerror(title="You made an oopsie", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=a, message=f"These are the details entered: \n {b} \n {c} \n OK to save?")

    if is_ok == True:

        with open("data.txt", "a") as f:
            f.write(f"{a} | {b} | {c} \n")
    # TODO Each website and e-mail should be on a new line in the file
        website_entry.delete(0, "end")
        password_entry.delete(0, "end")
# TODO Clear entries
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_pass = PhotoImage(file="logo.png")
canvas.create_image(100, 110, image=my_pass)
canvas.grid(column=1, row=1)

website = Label(text="Website:")
website.grid(column=0, row=2, sticky="w")

user_name = Label(text="E-mail/Username:")
user_name.grid(column=0, row=3, sticky="w")

password = Label(text="Password:")
password.grid(column=0, row=4, sticky="w")

website_entry = Entry(width=35)
website_entry.grid(row=2, column=1, columnspan=2, sticky="w")
website_entry.focus()

user_name_entry = Entry(width=35)
user_name_entry.grid(row=3, column=1, columnspan=2, sticky="w")
user_name_entry.insert(0, "grogu@koekjes.tat")

password_entry = Entry(width=35)
password_entry.grid(row=4, column=1, sticky="w")

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=4, column=2, sticky="w")

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=5, column=1, columnspan=2, sticky="we")

window.mainloop()