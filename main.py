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


def check_resources(order):
    for item in order:
        if order[item] > resources[item]:
            print(f"There is not enough {item} in the resources.")
            return False
    return True

def coins():
    input("Please insert coins: ")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction(pay, cost):
    if pay >= cost:
        change = round(pay - cost, 2)
        print(f"Here is ${change} in change!")
        global profit
        profit += cost
        return True
    else:
        print("Your payment is not enough")
        return False

def coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")

is_on = True

while is_on:
    choice = input("What drink would you like?: Latte, Espresso, Cappuccino: ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}g")
        print(f"Profit ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = coins()
            if transaction(payment, drink['cost']):
                coffee(choice, drink['ingredients'])