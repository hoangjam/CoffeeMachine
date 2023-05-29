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

def display_resources(resources):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return f"Resources available:\n Water: {water}ML\n Milk: {milk}ML\n Coffee:{coffee}ML"


print(display_prices(MENU))
is_on = True

while is_on:
    user_choice = input("What would you like? Espresso(e)/Latte(l)/Cappuccino(c): ")
    if user_choice == "off":
        print("Shutting down")
        is_on = False
    elif user_choice == "report":
        print(display_resources(resources))
