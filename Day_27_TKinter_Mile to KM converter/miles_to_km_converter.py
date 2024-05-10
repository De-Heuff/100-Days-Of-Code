from tkinter import *

def action():
    output["text"] = float(entry.get()) * 1.609344

#TODO1: Create window

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#TODO2: Create labels: 1) is equal to 2) Miles 3) KM 4) output

is_equal_to = Label(text="is equal to", font=("Leelawadee", 14))
is_equal_to.grid(column=1, row=2)

miles = Label(text="miles", font=("Leelawadee", 14))
miles.grid(column=3, row=1)
miles.config(padx=10, pady=10)

km = Label(text="km", font=("Leelawadee", 14))
km.grid(column=3, row=2)
km.config(padx=10, pady=10)

output = Label(text="waiting for input", font=("Leelawadee", 14))
output.grid(column=2, row=2)
output.config(padx=20, pady=20)

#TODO3: Create button Calculate

#calls action() when pressed
button = Button(text="Calculate", font=("Leelawadee", 14), command=action)
button.grid(column=2, row=3)

#TODO4: Create Entry
entry = Entry(width=20)
entry.grid(column=2, row=1)


#TODO5: create output label


window.mainloop()