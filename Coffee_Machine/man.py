MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100}
money = 0.0

def adjust_resources(inp_coffee):
    for key in resources:
        if MENU[inp_coffee]["ingredients"][key] > resources[key]:
            print(f"Sorry, there is not enough {key}. Cannot make {inp_coffee}.")
            return False

    if inp_coffee == "latte" or inp_coffee == "cappuccino":
        resources["water"] -= MENU[inp_coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[inp_coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[inp_coffee]["ingredients"]["coffee"]

    return True

def calculate_money(coins, coffee):
    total_in_dollars = (
        coins["quarters"] * 0.25
        + coins["dimes"] * 0.10
        + coins["nickels"] * 0.05
        + coins["pennies"] * 0.01
    )
    coffee_charge = MENU[coffee]["cost"]
    global money
    money = round((total_in_dollars - coffee_charge), 2)
    return money

def display_report():
    for key, value in resources.items():
        print(f"{key} : {value}")
    print("Money : ", money)

def run_coffee_machine():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino/off/report): ")

        if user_input.lower() == "off":
            break

        if user_input == "report":
            display_report()
        elif user_input in MENU:
            coins = {
                "quarters": int(input("How many quarters? ")),
                "dimes": int(input("How many dimes? ")),
                "nickels": int(input("How many nickels? ")),
                "pennies": int(input("How many pennies? ")),
            }

            money = calculate_money(coins, user_input)

            if adjust_resources(user_input):
                print(f"Here is ${money} in change.")
                print(f"Here is your {user_input} ☕️. Enjoy!")
        else:
            print("Invalid input. Please choose from espresso, latte, cappuccino, report, or off.")

if __name__ == "__main__":
    run_coffee_machine()
