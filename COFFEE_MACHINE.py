MENU = {
                 "espresso": {
                                        "ingredients": {
                                                                "water": 50,
                                                                "milk": 0,
                                                                "coffee": 18,
                                                              },
                                        "cost": 12,
                                        },
                 "latte":       {
                                    "ingredients": {
                                                            "water": 200,
                                                            "milk": 150,
                                                            "coffee": 24,
                                                          },
                                    "cost": 15,
                                    },
                 "cappuccino": {
                                    "ingredients": {
                                                            "water": 250,
                                                            "milk": 100,
                                                            "coffee": 24,
                                                          },
                                    "cost": 17,
                                    }
                }

resources = {
                    "water": 300,
                    "milk": 200,
                    "coffee": 100,
                    }


def coffee(x):
    if x == 1:
        return "espresso"
    elif x == 2:
        return "latte"
    elif x == 3:
        return "cappuccino"
    else:
        print("Wrong Input")
        go()


def menu(material):
    print("Resources Details : ")
    print(f'Water = {material["water"]}')
    print(f'MILK  = {material["milk"]}')
    print(f'COFFEE = {material["coffee"]}\n')
    print("\t'MENU'")
    print("1) ESPRESSO        $12")
    print("2) LATTE              $15")
    print("3) CAPPUCCINO    $17")
    choice = int(input("Enter your choice no. : "))
    coffee_num = coffee(choice)
    cash_input = int(input("No. of $5 coin   : ")) * 5
    cash_input += int(input("No. of $10 coin : ")) * 10
    cash_input += int(input("No. of $20 coin : ")) * 20
    return coffee_num, cash_input


def credit_debit(coffee_num, cash):
    coffee_price = MENU[coffee_num]
    cash_return = cash - coffee_price["cost"]
    if cash_return < 0:
        print("Cash given is less then the price")
    elif cash_return >= 0:
        print(f"Your order is : {coffee_num}")
        print(f"Your change is {cash_return}")
        return
    input("Press enter to go back")
    go()


def substance(coffee_num, material):
    making1 = MENU[coffee_num]
    making_req = making1["ingredients"]
    material["water"] -= making_req["water"]
    material["coffee"] -= making_req["coffee"]
    material["milk"] -= making_req["milk"]
    if material["water"] < 0 or material["coffee"] < 0 or material["milk"] < 0:
        print("Insuffient Resources")
        exit(1)
    else:
        return material


def go():
    global resources
    while True:
        coffee_name, cash_given = menu(resources)
        credit_debit(coffee_name, cash_given)
        resources = substance(coffee_name, resources)


go()
