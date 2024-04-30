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
#TODO 3: Print report (functie)


def print_report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${profit}")


#TODO 4: Check if resources are sufficient (functie)
def resources_sufficient(product, res):
    """Berekent of er genoeg resources zijn om de keuze te maken"""
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        print (f"Sorry, not enough water to make {choice}")
        if MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
            print(f"Sorry, not enough coffee to make {choice}")
            if choice == "cappuccino" or choice == "latte" and MENU[choice]["ingredients"]["milk"] > resources["milk"]:
                print(f"Sorry, not enough milk to make {choice}")
            else:
                return True
        else:
            return True
    else:
        return True

#TODO 5: Process coins (functie)
def process_coins():
    """berekent het totaal aanal ingevoerde munten"""
    print("Please insert coins")
    total = int(input("Amount of quarters: ")) * 0.25
    total += int(input("Amount of dimes: ")) * 0.10
    total += int(input("Amount of nickels: ")) * 0.05
    total += int(input("Amount of pennies: ")) * 0.01
    return total


#TODO 6: Check if transaction is successful and make coffee (functie)
def transaction_succesful(money, price):
    if money_received < MENU[choice]["cost"]:
        print(f"Sorry, not enough money to make {choice}. Money refunded")
    elif money_received >= MENU[choice]["cost"]:
        refund = float(round(money_received - MENU[choice]["cost"], 2))
        print(f"Here is ${refund}. Enjoy your {choice}")
        make_coffee(choice, resources)
        global profit
        profit += MENU[choice]["cost"]
        return True

def make_coffee(pr, res):
    """Deduct required ingredients from resources and make coffee"""
    res["water"] = res["water"] - MENU[pr]["ingredients"]["water"]
    res["coffee"] = res["coffee"] - MENU[pr]["ingredients"]["coffee"]
    if choice == "cappuccino" or choice == "latte":
        res["milk"] = res["milk"] - MENU[pr]["ingredients"]["milk"]
    resources = {"water": res["water"], "milk": res["milk"], "coffee": res["coffee"]}
    return resources


    #TODO 1: prompt user what they would like
machine_on = True
while machine_on:
    choice = input("What would you like to drink? espresso, latte or cappuccino? ")

#TODO 2: Turn off coffee machine by entering off
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print_report()
    else:
        resources_sufficient(choice, resources)
        money_received = process_coins()
        transaction_succesful(money_received, choice)

