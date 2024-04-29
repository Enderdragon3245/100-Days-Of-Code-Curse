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
def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, You Wake enough {resources[item]}")
        return False
    return True

def Check_Coins(Check):
    if profit > drink["cost"]:
        return

def process_coins():
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

is_on = True
while is_on:
    Check = str(input("What would you like? (espresso/latte/cappuccino):")).lower()
    if Check == "off":
         is_on = False
    elif Check == "report":
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffe: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[Check]
        if is_resources_sufficient(drink["ingredients"]):
            paymoney = process_coins()
            


