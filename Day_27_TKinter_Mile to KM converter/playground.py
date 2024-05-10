#maak een add-functie, waarin je zoveel mogelijk cijfers mee kan geven en die het totaal optelt.

def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(104, 5, 25, 39, 55, 204, 89)
#je kunt hier ook een index gebruiken om het getal op een bepaalde positie op te halen. Daarom wordt dit ook wel
#unlimited positional arguments genoemd.

def calculate(n, **kwargs): #kwargs is een dictionary
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=3)
#Dit snap ik nog niet goed.

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")
        #ipv [] kun je ook waardes uit een dictionary halen met get()
        #Met get krijg je geen foutmelding als je geen waarde meegeeft in de functie

my_car = Car(make="Nissan", color="red")
print(my_car.model)

