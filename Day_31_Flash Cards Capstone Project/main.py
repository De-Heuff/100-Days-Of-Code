from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
DATAFILE = "Russisch flash cards - Blad1.csv"
DATAFILE_TRAINED = "data/words_to_learn.csv"

#--------------------------IMPORT DATA--------------------------------------------------#
try:
    flash_card_ru=pandas.read_csv(DATAFILE_TRAINED)
except FileNotFoundError:
    flash_card_ru = pandas.read_csv(DATAFILE)

#----------------------------VALIDATE DATA--------------------------------------------------#

if "Russisch" in flash_card_ru.columns and "Nederlands" in flash_card_ru.columns:
    flash_card_ru.dropna(subset=["Russisch", "Nederlands"], inplace=True)
else:
    flash_card_ru = pandas.read_csv(DATAFILE)
    flash_card_ru.dropna(subset=["Russisch", "Nederlands"], inplace=True)

#-----------------------------CREATE STUDY FILE ---------------------------------------------#
russian_to_dutch = dict(zip(flash_card_ru["Russisch"], flash_card_ru["Nederlands"]))

current_russian_word = ""
current_dutch_word = ""

#------------------------CREATE FUNCTIONS--------------------------------------------------------#
def next_word():
    global current_russian_word, current_dutch_word, flip_timer
    window.after_cancel(flip_timer)
    current_russian_word, current_dutch_word = random.choice(list(russian_to_dutch.items()))
    canvas.itemconfig(random_word, text=current_russian_word, fill="black")
    canvas.itemconfig(card_title, text="Russisch", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(random_word, text=current_dutch_word, fill="white")
    canvas.itemconfig(card_title, text="Nederlands", fill="white")

def right_card():
    global russian_to_dutch
    if current_russian_word in russian_to_dutch:
        del russian_to_dutch[current_russian_word]
        flash_cards_trained = pandas.DataFrame(list(russian_to_dutch.items()), columns=["Russisch", "Nederlands"])
        flash_cards_trained.to_csv(DATAFILE_TRAINED, index=False)
    next_word()
def wrong_card():
    next_word()

#-----------------------------------UI SETUP-----------------------------------------------#
window = Tk()
window.title("Russian Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=".\images\card_front.png")
card_back = PhotoImage(file=".\images\card_back.png")
canvas_image = canvas.create_image(410, 275, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(410, 150, text="", font=("Arial", 40, "italic"))
random_word = canvas.create_text(400, 275, text="", font=("Arial", 60, "bold"))

wrong_button_image = PhotoImage(file=".\images\wrong.png")
wrong_button = Button(image=wrong_button_image, borderwidth=0, highlightthickness=0, command=wrong_card)
wrong_button.grid(row=1, column=0)

right_button_image = PhotoImage(file=".\images\ight.png")
right_button = Button(image=right_button_image, borderwidth=0, highlightthickness=0, command=right_card)
right_button.grid(row=1, column=1)

next_word()

window.mainloop()

