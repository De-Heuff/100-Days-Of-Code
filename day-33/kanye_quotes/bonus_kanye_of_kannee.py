from tkinter import *
from tkinter import messagebox  # Voor pop-ups
import requests
import random

# Variabelen
score = 0
current_quote = ""
current_author = ""  # Houdt de auteur bij
is_kanye = False  # Houdt bij of de huidige quote van Kanye is

# Functie om een nieuwe quote op te halen
def get_new_quote():
    global current_quote, current_author, is_kanye

    # Willekeurig kiezen: Kanye of Niet-Kanye?
    if random.choice([True, False]):
        response = requests.get("https://api.kanye.rest")
        quote_data = response.json()
        current_quote = quote_data["quote"]
        current_author = "Kanye West"
        is_kanye = True
    else:
        response = requests.get("https://zenquotes.io/api/random")
        quote_data = response.json()
        current_quote = quote_data[0]["q"]
        current_author = quote_data[0]["a"]  # 'a' bevat de auteur
        is_kanye = False

    canvas.itemconfig(quote_text, text=current_quote)

# Functie om antwoord te checken
def check_answer(is_kanye_guess):
    global score
    if is_kanye_guess == is_kanye:
        score += 1
        result_text.set(f"✅ Correct! Score: {score}")
    else:
        result_text.set(f"❌ Fout! Score: {score}")

    # Als het GEEN Kanye-quote was, toon een pop-up met de echte auteur
    if not is_kanye:
        messagebox.showinfo("Niet Kanye!", f"Deze quote is van: {current_author}")

    get_new_quote()  # Haal een nieuwe quote op

# GUI Setup
window = Tk()
window.title("Kanye Quote of Niet?")
window.config(padx=50, pady=50)

# Canvas voor de quote
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Klik om te beginnen!", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0, columnspan=2)

# Knoppen voor Kanye/Niet Kanye
kanye_button = Button(text="Kanye!", command=lambda: check_answer(True))
kanye_button.grid(row=1, column=0)

not_kanye_button = Button(text="Niet Kanye!", command=lambda: check_answer(False))
not_kanye_button.grid(row=1, column=1)

# Resultaat label
result_text = StringVar()
result_label = Label(textvariable=result_text, font=("Arial", 14, "bold"))
result_label.grid(row=2, column=0, columnspan=2)

# Start het spel met de eerste quote
get_new_quote()

window.mainloop()