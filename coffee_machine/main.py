from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system, name

def clear():
    """Clears the screen for nice output."""
    if name == 'nt':
        system('cls')
    else:
        system('clear')

coffee_machine = CoffeeMaker()
menu = Menu()
cash_register = MoneyMachine()

while True:
    clear()
    print("1: Order a drink")
    print("2: Print report")
    print("3: Shutdown machine")
    menu_choice = int(input("What would you like to do? "))

    if menu_choice == 1:
        clear()
        drink = input(f"What would you like? ({menu.get_items()}):\n").lower()
        drink = menu.find_drink(drink)
    
        if coffee_machine.is_resource_sufficient(drink):
            cash_register.make_payment(drink.cost)
            coffee_machine.make_coffee(drink)
        input("\nPress enter to continue")
    elif menu_choice == 2:
        clear()
        coffee_machine.report()
        cash_register.report()
        input("\nPress enter to continue")
    elif menu_choice == 3:
        exit()
    else:
        print("\nInvalid choice")
        input("\nPress enter to continue")