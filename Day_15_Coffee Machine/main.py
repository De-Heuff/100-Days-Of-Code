MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#JE MAG NIET DEZELFDE INPUT ALS BESTAANDE VARIABELE GEBRUIKEN!
def check_inventory(product, resrcs):
    """controleert het aantal beschikbare ingredienten"""
    if MENU[product]["ingredients"]["water"] <= resrcs["water"]:
        if MENU[product]["ingredients"]["milk"] <= resrcs["milk"]:
            #TODO omvormen, dit werkt niet bij espresso omdat die geen melk heeft
            if MENU[product]["ingredients"]["coffee"] <= resrcs["coffee"]:
                return True
            else:
                print(f"Sorry, not enough coffee. Only {resrcs['coffee']} g remain.")
        else:
            print(f"Sorry, not enough milk. Only {resrcs['milk']} oz remain.")
    else:
        print(f"Sorry, not enough water. Only {resrcs['water']} oz remain.")
        return False

def process_coins():
    """berekent het totaal aanal ingevoerde munten"""
    print("Please insert coins")
    total = int(input("Amount of quarters: ")) * 0.25
    total += int(input("Amount of dimes: ")) * 0.10
    total += int(input("Amount of nickels: ")) * 0.05
    total +=  int(input("Amount of pennies: ")) * 0.01
    return total

def check_funds(money_received: object, choice: object) -> object:
    """Berekent of er genoeg geld is voor het product naar keuze, geeft geld terug als het teveel is en
    bereidt het product"""
    if money_received == MENU[choice]["cost"]:
        print(f"Thank you! Enjoy your {choice}")
        produce(choice, resources)
    elif money_received > MENU[choice]["cost"]:
        refund = money_received - MENU[choice]["cost"]
        #TODO: Debug dat dit afrondt!
        print(f"Here is ${refund} in change! Enjoy your {choice}!")
        produce(choice, resources)
    else:
        print(f"Insufficient funds. Money refunded")

def produce(pr, res):
    """Deduct required ingredients from resources and make coffee"""
    res["water"] = res["water"] - MENU[pr]["ingredients"]["water"]
    res["milk"] = res["milk"] - MENU[pr]["ingredients"]["milk"]
    res["coffee"] = res["coffee"] - MENU[pr]["ingredients"]["coffee"]
    resources = {"water": res["water"], "milk": res["milk"], "coffee": res["coffee"]}
    return resources


machine_on = True
while machine_on:
    choice = input("What would you like? espresso/latte/cappuccino")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        check_inventory(choice, resources)
        money_received = process_coins()
        check_funds(money_received, choice)
        #TODO debuggen, gaat nog niet helemaal goed

#ALt + Shift = op meerdere regels dezelfde input invoeren

