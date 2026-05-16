MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}

def report():
    global resources
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources["milk"]} ml")
    print(f"Coffee: {resources["coffee"]} gm")
    print(f"Money: ${resources["money"]} ")

def add():
    global resources
    inp = True
    while inp:
        what_to_add = input("What ingredient do you want to add? (water, milk, coffee)\n").lower()
        if what_to_add == "water":
            quantity = int(input("How much water do you want to add? (in ml)\n"))
            resources["water"] += quantity
            print(f"The amount of water in the machine is {resources['water']} ml")
            inp = False
        elif what_to_add == "milk":
            quantity = int(input("How much milk do you want to add? (in ml)\n"))
            resources["milk"] += quantity
            print(f"The amount of milk in the machine is {resources['milk']} ml")
            inp = False
        elif what_to_add == "coffee":
            quantity = int(input("How much coffee do you want to add? (in gm)\n"))
            resources["coffee"] += quantity
            print(f"The amount of coffee in the machine is {resources['coffee']} gm")
            inp = False
        else:
            print("Invalid input. Try again.")

def check_ingredients(type):
    global resources, MENU
    if type == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    elif type == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    elif type == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    else:
        coffee()

def coins(coffee_type):
    global MENU, resources
    print("Please insert coins.")
    quarter = float(input("How many quarters : "))
    dime = float(input("How many dimes : "))
    nickle = float(input("How many nickle : "))
    pennie = float(input("How many pennies : "))
    money_given = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (pennie * 0.01)
    if MENU[coffee_type]["cost"] > money_given:
        return -1
    else:
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        resources["money"] += MENU[coffee_type]["cost"]
        return money_given - MENU[coffee_type]["cost"]

def coffee():
    global MENU, resources
    coffee_type = input("Select your required coffee ('espresso' / 'latte' / 'cappuccino')\n").lower()
    if check_ingredients(coffee_type):
        balance = round(coins(coffee_type),2)
        if balance == -1:
            print("You don't have enough money to make this coffee.")
            return
        else:
            print(f"Here is your change : ${balance}")
            print(f"Enjoy your {coffee_type} ☕")
    elif check_ingredients(coffee_type) == False and (coffee_type == "espresso" or "latte" or "cappuccino"):
        print("The machine doesn't have enough ingredients.")
        return


while True:
    coffee_machine = input("Type 'on' to turn on the coffee machine. : ").lower()
    if coffee_machine == "on":
        print(f"The Coffee Machine has been turned ON.")
    else:
        print("Invalid input. Try again.")

    while coffee_machine == 'on':

        print("\nType 'report' to see the ingredients inside the machine.")
        print("Type 'add' to add more ingredients.")
        print("Type 'coffee' to use the machine.")
        print("Type 'off' to turn off the machine.")
        choice = input("==> ").lower()

        if choice == "report":
            report()
        elif choice == "add":
            add()
        elif choice == "coffee":
            coffee()
        elif choice == "off":
            print("The Coffee Machine has been turned OFF.\n")
            coffee_machine = "off"
