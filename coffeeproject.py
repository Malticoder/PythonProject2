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
    'water' : 300,
    'milk' : 200,
    'coffee' : 100
}
def is_resource_sufficient(order_ingredients):
    """return True when order can be made, False if ingredients are sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            is_enough = False
    return True
def process_coins():
    print("insert coins:")
    total = int(input("how many quarters? :"))* 0.25
    total += int(input("how many dimes? :")) * 0.1
    total += int(input("how many nickles? :")) * 0.05
    total += int(input("how many pennies? :")) * 0.01
    return total
def is_transaction_successful(money_received, drink_cost):
    """return True if payment is accepted, or False when money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that is not enough money. Money refunded")
def make_coffee(drink_name , order_ingredients):
    """deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name} ")





is_on = True
while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])








