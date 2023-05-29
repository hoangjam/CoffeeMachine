"""
print report
check resources are sufficient
process coins
check if transaction success
make coffee
"""

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


def display_prices(menu):
    name1 = "Espresso"
    name2 = "Latte"
    name3 = "Cappuccino"
    cost1 = menu['espresso']['cost']
    cost2 = menu['latte']['cost']
    cost3 = menu['cappuccino']['cost']

    return f"Prices:\n {name1}: ${cost1}\n {name2}: ${cost2}\n {name3}: ${cost3}\n"


def display_resources(ingredients):
    water = ingredients["water"]
    milk = ingredients["milk"]
    coffee = ingredients["coffee"]

    return f"Resources available:\n Water: {water}ML\n Milk: {milk}ML\n Coffee:{coffee}ML"


def ingredient_check(selection):
    # If there are enough ingredients, return True, so we can charge customer.
    for i in selection:
        if selection[i] > resources[i]:
            print(f"There is not enough {i} to make your drink, sorry!")

            return False

    return True


def process_money():
    print("Please insert your coins")
    total = 0
    total += int(input("Toonies: ")) * 2.00
    total += int(input("Loonies: ")) * 1.00
    total += int(input("Quarters: ")) * 0.25
    total += int(input("Dimes: ")) * 0.10
    total += int(input("Nickels: ")) * 0.05

    return total


def charge_customer(paid_amount, cost):
    if paid_amount < cost:
        print("Insufficient funds, your coins have been refunded")

        return False
    elif paid_amount >= cost:
        change = round(paid_amount - cost, 2)
        print(f"Your change is ${change}.")

        return True


def make_drink(order):
    for i in order["ingredients"]:
        resources[i] -= order["ingredients"][i]
    print(f"Here is your drink, please enjoy!\n")


print(display_prices(MENU))
is_on = True

while is_on:
    user_choice = input("What would you like? Espresso(e)/Latte(l)/Cappuccino(c): ")
    if user_choice == "off":
        print("Shutting down")
        is_on = False
    elif user_choice == "report":
        print(display_resources(resources))
    elif user_choice == "e":
        choice = MENU["espresso"]
    elif user_choice == "l":
        choice = MENU["latte"]
    elif user_choice == "c":
        choice = MENU["cappuccino"]

    ingredient_check(choice["ingredients"])
    paid = process_money()
    if charge_customer(paid, choice["cost"]):
        print("Vending")
        make_drink(choice)


