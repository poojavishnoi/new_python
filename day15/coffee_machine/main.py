menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 100,
            "coffee" : 18,
        },
        "cost": 130,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 140,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 150,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def money_return(payment):
    if payment >= menu[choice]["cost"]:
        remaining_money = True
        return payment - menu[choice]["cost"]


def reduce(coffee_water, coffee_milk , coffee):
    resources["water"] -= coffee_water
    resources["milk"] -= coffee_milk
    resources["coffee"] -= coffee
    print(resources)


def compare(choice):

    if choice in menu:
        #if resources["water"] < coffee_water or resources["milk"] < coffee_milk or resources["coffee"] < coffee:
        #   print(f"Sorry there is not enough ingredient.")
        for y in menu[choice]:
            if y == "ingredients":
                coffee_water = menu[choice][y]["water"]
                coffee_milk = menu[choice][y]["milk"]
                coffee = menu[choice][y]["coffee"]

            if resources["water"] < coffee_water or resources["milk"] < coffee_milk or resources["coffee"] < coffee:
                print(f"Sorry there is not enough ingredient.")
                return 0
            else:
                reduce(coffee_water, coffee_milk , coffee)
                coffee_money = menu[choice][y]
                return coffee_money




#ask user's choice
payment = 0
money = 0
repeat = True
output = ""
remaining_money = False
while repeat:
    choice = input("What would you like to have? (espresso, latte, cappuccino):\n")
    if choice == "report":
        for x in resources:
            if x == "coffee":
                print(f"{x} : {resources[x]}g")
            else:
                print(f"{x} : {resources[x]}ml")
        print(f"Money : Rs {money}")
    elif choice == "off":
        break
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        continuation = compare(choice)
        if continuation != 0:
            payment = int(input("Enter the money:\n"))
            return_money = money_return(payment)
            if not remaining_money:
                print(f"Here is your Rs {return_money}")
                money += payment

            print(f"Enjoy your {choice} ☕")






