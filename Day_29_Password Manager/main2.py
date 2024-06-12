from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(5, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 6))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    a = website_entry.get()
    b = user_name_entry.get()
    c = password_entry.get()
    new_data = {
        a: {
            "email": b,
            "password": c,
        }
    }

    if len(a) == 0 or len(c) == 0:
        messagebox.showerror(title="You made an oopsie", message="Please don't leave any fields empty!")
        return

    else:
        try:
            with open("data.json", "r") as data_file:
                #Read from JSON
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open("data.json", "w") as data_file:
                # Update JSON with New Data
                data.update(new_data)
                #write updated data to JSON
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

# ---------------------------- Search function ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Read from JSON
            dict = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
        return

    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Data file is corrupted.")
        return

    else:
        website_data = dict.get(website)
        if website_data:
            email = website_data.get("email")
            password = website_data.get("password")
            messagebox.showinfo(title="Data", message=f"These are the details for {website}: \n E-mail: {email} \n Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exist.")

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

website_entry = Entry(width=33)
website_entry.grid(row=2, column=1, columnspan=2, sticky="w")
website_entry.focus()

user_name_entry = Entry(width=53)
user_name_entry.grid(row=3, column=1, columnspan=2, sticky="w")
user_name_entry.insert(0, "grogu@koekjes.tat")

password_entry = Entry(width=33)
password_entry.grid(row=4, column=1, sticky="w")

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=4, column=2, sticky="w")

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=5, column=1, columnspan=2, sticky="we")

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=2, column=2, sticky="w")

window.mainloop()
