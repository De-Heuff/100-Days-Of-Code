from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Instance creëren van een class is feitelijk een object maken van een class:
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True
while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_on = False
    else:
        drink = menu.find_drink(choice)
        if drink.name == "cappuccino":
            are_you_sure = input(f"That will be {drink.ingredients} to make. Are you sure you want to continue? Y/N")
            if are_you_sure == "N":
                print("Thank you for making a sustainable choice!)")

#TODO 4: Check if resources are sufficient
#the first argument of al methods is called self. It refers to the instance for which the method is being called.
        #let erop dat ik hier de instance gebruik en niet de class!
        check_resources = coffee_maker.is_resource_sufficient(drink)
        if check_resources == True:

#TODO 5: Process coins & #TODO 6: Check transaction succesful
#.cost is het Attribute dat we willen associeren met ons drankje
            print(f"That will be $ {(drink.cost)}")
            is_transaction_succesful = money_machine.make_payment(drink.cost)

#TODO 7: Make coffee and subtract resources
            if is_transaction_succesful:
                coffee_maker.make_coffee(drink)