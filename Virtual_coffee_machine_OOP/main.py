from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    # Instantiate the objects
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    is_on = True

    while is_on:
        options = menu.get_items()
           print(
            "You can check the report of how much 'Milk', 'Water', and 'Coffee' is left in the machine. \nBy typing in 'Report!.'"
        )
        choice = input(f"What would you like? ({options}): ").lower()

        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)

if __name__ == "__main__":
    main()
