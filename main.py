from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

coffee_machine_on = True
while coffee_machine_on:
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        coffee_machine_on = False
    else:
        coffee = user_input
        drink = menu.find_drink(coffee)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)









