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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_on = True


def is_resource_sufficient(order_ingredients):
    """Returns True when an order can be made and False when insufficient ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total from the inserted coins"""
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment accepted, or False when insufficient"""
    if money_received >= drink_cost:
        change = round((money_received - drink_cost), 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(drink_name, ordered_ingredients):
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while is_on:
    drink_choice = input("What would you like? (espresso/latte/cappuccino)")
    if drink_choice == "off":
        is_on = False
    elif drink_choice == "report":
        print(f"water = {resources['water']}ml")
        print(f"milk = {resources['milk']}ml")
        print(f"coffee = {resources['coffee']}g")
        print(f"money = ${profit}")
    else:
        drink = MENU[drink_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink_choice, drink["ingredients"])

# TODO: 1. Prompt user by asking, What would you like? (espresso/latte/cappuccino):
# once the drink is dispensed. The prompt should show again to serve the next customer.
# TODO: 2. Turn off the Coffee Machine by entering ofF to the prompt
# TODO: 3. function called report, that return current resource value
# def report():
# water = 100
# milk = 50
# coffee = 76
# money = 2.5

# TODO: 4. Check resources sufficient?
# FOR EACH ORDER CHECK THEIR IS ENOUGH RESOURCES (WATER, MILK & COFFEE) FOR THE SPECIFIED DRINK ELSE
# RETURN Sorry there is not enough {RESOURCE}
# def enough_resources(), parameter specific drink, call report and report.resource - drink.ingredient
# if not negative integer: return true else Sorry there is not enough {RESOURCE}

# TODO: 5. Process coins, if enough_resources() then call new function process_coins
# process_coins, parameter coins_inserted
# coins_inserted = input("Please insert coins.
# how many quarters?:
# how many dimes?:
# how many nickles?:
# how many pennies?:
# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# map coins_inserted to monetary value of the coins
# return monetary_value

# TODO: 6. Check transaction successful
# def successful_transaction():
# if monetary_value > drink.cost:
# money += monetary_value
# customer_change = cost - monetary_value
# Here is ${customer_change} in change.
# return true
# else:
# Sorry that's not enough money. Money refunded.
# return false

# TODO: 7. Make Coffee
# if enough_resources and successful_transaction():
# ingredients to make the drink should be deducted from the coffee machine resources
# Here is your {drink_choice} ☕️. Enjoy!
