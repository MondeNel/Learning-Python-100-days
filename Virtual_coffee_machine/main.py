from data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



# Initial resources in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Initial money in the coffee machine
money = 0

#Check for machine resources
def is_resource_sufficient(order_ingredients):
    """
    Check if the machine has enough resources to make the drink.
    
    Args:
    order_ingredients (dict): Ingredients required for the selected drink.
    
    Returns:
    bool: True if resources are sufficient, False otherwise.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

#Check for coins
def process_coins():
    """
    Calculate the total amount of money from inserted coins.
    
    Returns:
    float: Total amount of money inserted.
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

#Check to see if the user has inserted the coins to buy the drinks
def is_transaction_successful(money_received, drink_cost):
    """
    Check if the user has inserted enough money to buy the drink.
    
    Args:
    money_received (float): Total money inserted by the user.
    drink_cost (float): Cost of the selected drink.
    
    Returns:
    bool: True if the transaction is successful, False otherwise.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

#Manages the ingredients from the machine
def make_coffee(drink_name, order_ingredients):
    """
    Deduct the required ingredients from the machine resources and serve the coffee.
    
    Args:
    drink_name (str): Name of the drink.
    order_ingredients (dict): Ingredients required for the selected drink.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


#Handles user input and coffee-making process
def coffee_machine():
    """
    Main function to run the coffee machine.
    Handles user input and manages the coffee-making process.
    """
    is_on = True

    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        else:
            drink = MENU.get(choice)
            if drink:
                if is_resource_sufficient(drink["ingredients"]):
                    payment = process_coins()
                    if is_transaction_successful(payment, drink["cost"]):
                        make_coffee(choice, drink["ingredients"])

# Run the coffee machine
coffee_machine()