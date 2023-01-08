from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_list = Menu()
name_list = menu_list.get_items()
machine = CoffeeMaker()
counter = MoneyMachine()


while True:
    command = input(f"What would you like? ({name_list}):")
    if command == 'off':
        break
    elif command == 'report':
        machine.report()
        counter.report()
    elif command in name_list:
        item = menu_list.find_drink(command)
        if machine.is_resource_sufficient(item):
            if counter.make_payment(item.cost):
                machine.make_coffee(item)
            else:
                pass
        else:
            pass
    else:
        continue


