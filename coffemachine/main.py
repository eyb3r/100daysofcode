MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,
}


COINS = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickels': 0.05,
    'pennies': 0.01,
}


def report():
    output = f'''Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${resources['money']:.2f}
'''
    print(output)


def resources_sufficient(command):
    if resources['water'] < MENU[command]['ingredients']['water']:
        output = (False, 'water')
    elif resources['milk'] < MENU[command]['ingredients']['milk']:
        output = (False, 'milk')
    elif resources['coffee'] < MENU[command]['ingredients']['coffee']:
        output = (False, 'coffee')
    else:
        output = True
    return output


def update_resources(coffee):
    for ing in ['water', 'milk', 'coffee']:
        resources[ing] -= MENU[coffee]['ingredients'][ing]
    resources['money'] += MENU[coffee]['cost']


def process_payment(coffee):
    print("Please insert coins.")
    total = 0
    for coin, value in COINS.items():
        total += int(input(f'how many {coin}?:')) * value
    total -= MENU[coffee]['cost']
    if total >= 0:
        print(f"Here is ${total:.2f} in change.")
        print(f"Here is your {coffee} ☕. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")
    update_resources(coffee)


def transaction(item_name):
    resource_check = resources_sufficient(item_name)
    if resource_check == True:
        process_payment(item_name)
    else:
        print(f"Sorry, there is not enough {resource_check[1]}")


commands = ["espresso", "latte", "cappuccino", "report", "off"]
current_command = ''
while True:
    current_command = input(' What would you like? (espresso/latte/cappuccino):')
    if current_command not in commands:
        continue
    if current_command == 'off':
        break
    elif current_command == 'report':
        report()
    else:
        transaction(current_command)
