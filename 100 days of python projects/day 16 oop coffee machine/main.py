from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
latte = MenuItem("latte",200,150,24,2.5)
espresso = MenuItem("espresso",50,0,18,1.5)
cappuccino = MenuItem("cappuccino",250,100,24,3.0)


def print_report():
    my_coffee_maker.report()
    my_money_machine.report()
    take_order()

def take_order():
    while True:
        options = my_menu.get_items()
        selected_drink = input(f"what would you like? {options}: ")
        if selected_drink  in ["espresso","latte","cappuccino"]:          
            deal_order( my_menu.find_drink(selected_drink))
        elif selected_drink =="report":
            print_report()
            break
        else:
            print("not a valid response")


def deal_order(drink):
    if my_coffee_maker.is_resource_sufficient(drink) == False:        
        take_order() 
          
    my_money_machine.make_payment(drink.cost)
    my_coffee_maker.make_coffee(drink)
    take_order()
    

take_order()
