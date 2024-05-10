import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=600, height=100)
window.config(padx=20, pady=20)
def button_click():
    my_label["text"] = input.get()

#Packs each of the widgets next to each other. From top to bottom. Places the widgets on the screen.
#Je kunt geen specifieke positie bepalen.

#Create Label
my_label = tkinter.Label(text="Wat voor snack wil je?", font=("Verdana", 12, "bold"))
#my_label.place(x=0, y=100)
my_label.grid(column=0, row=0)

button = tkinter.Button(text="Klik hier voor snackjes", command=button_click)
button.grid(column=2, row=2)
button.config(padx=20,pady=20)

button2 = tkinter.Button(text="Klik hier voor sausjes", command=button_click)
button2.grid(column=3, row=1)

#Place(): precise positioning with X- and Y-value.
#Grid(): lay-outmanager met een grid. Let op: incompatible with pack.

#component updaten
#my_label["text"] = "Houd jij ook zo van muffins?"

#Entry component
input = tkinter.Entry(width=10)
input.grid(column=4,row=3)
input.get()

#Advanced arguments
#Arguments with default values. Bij het definieren van de functie kun je al default argumenten meegeven, zodat je die
#niet meer mee hoeft te geven in de functie.

#*args = unlimited arguments. *vertelt Python dat de funtie oneindig veel argumenten mee kan nemen.

#**kwargs = unlimited keyword arguments.

window.mainloop()