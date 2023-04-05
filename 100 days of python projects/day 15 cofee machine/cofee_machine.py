from data import MENU, resources

current_resources = resources

def print_report(current_resources):
    for item in current_resources:
        if item =="water" or item =="milk":
            print(f"{item}: {current_resources[item]}ml")
        elif item =="coffee":
            print(f"{item}: {current_resources[item]}g")
        elif item =="money":
            print(f"{item}: ${current_resources[item]}")
    coffee_machine()


def takeOrder(selected_drink):
    drink_cost = MENU[selected_drink]["cost"]
    drink_ingredients = MENU[selected_drink]["ingredients"]
    isAvailable = True
    problematic_ingredient = ""
    for ingredient in drink_ingredients:
        if current_resources[ingredient] - drink_ingredients[ingredient] < 0:
            isAvailable =False
            problematic_ingredient = ingredient
    if isAvailable==False:
        print(f"sorry, not enough {problematic_ingredient}")
        coffee_machine()            
    total_paid = 0
    print("please insert coins.")
    count_quarters = int(input("how many quarters?: "))
    count_dimes = int(input("how many dimes?: "))
    count_nickels = int(input("how many nickels?: "))
    count_pennies = int(input("how many pennies?: "))
    total_paid+= count_quarters*0.25 + count_dimes*0.1 +count_nickels*0.05 + count_pennies*0.01
    
        
    if total_paid < drink_cost:
        print("sorry that's not enough money")
        coffee_machine()

    elif total_paid >= drink_cost and isAvailable == True :
        print(f"here is ${total_paid - drink_cost}. enjoy your {selected_drink}")
        current_resources["money"] += drink_cost
        current_resources["water"] -= drink_ingredients["water"]
        current_resources["milk"] -= drink_ingredients["milk"]
        current_resources["coffee"] -= drink_ingredients["coffee"]
        coffee_machine()

    updated_resources = current_resources
    return updated_resources
        
        
def coffee_machine():
    while True:
        updated_resources = current_resources
        selected_drink = input("what would you like? (espresso/latte/cappuccino): ")
        if selected_drink  in ["espresso","latte","cappuccino"]:
            updated_resources = takeOrder(selected_drink)
            break
        elif selected_drink =="report":
            print_report(updated_resources)
            break
        else:
            print("not a valid response")

coffee_machine()