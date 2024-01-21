from data import MENU, resources
from art import coffee

machine_resouces = resources


def is_resource_sufficient(order_ingredients):
    """check if the order can be made - resources"""
    for item in order_ingredients:
        if order_ingredients[item] >= machine_resouces[item]:
            print(f"Sorry there is not enought {item}.")
            return False
    return True


def process_coins():
    """return total calculated coins"""
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """return True is payment is accepted or return False if not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        machine_resouces[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_machine_works = True
profit = 0
print(coffee)
while is_machine_works:
    print(f"""Welcome: You can get:
    espresso: ${MENU['espresso']['cost']} 
    late: ${MENU['latte']['cost']}
    cappuccino: ${MENU['cappuccino']['cost']}"""
          )
    user_choice = (input("What do you want?\n - "))

    if user_choice == "off":
        is_machine_works = False
    elif user_choice == "report":
        print("Machine resources report: ")
        print(f"Water: {machine_resouces['water']}")
        print(f"Milk: {machine_resouces['milk']}")
        print(f"Coffee: {machine_resouces['coffee']}")
        print(f"Coffee: ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(drink_name=user_choice, order_ingredients=drink["ingredients"])
