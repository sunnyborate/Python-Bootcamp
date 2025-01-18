# Coffee Machine prompt
#100daysofcoding Day 15

Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

profit = 0
resources = {
    "water": 5000,
    "milk": 2000,
    "coffee": 2500,
}

#print(Menu["latte"]["ingredients"]["milk"])

def check(choice, resources):
    if resources["water"] >= Menu[choice]["ingredients"]["water"] and resources["milk"] >= Menu[choice]["ingredients"]["milk"] and resources["coffee"] >= Menu[choice]["ingredients"]["coffee"]:
        return True
    else:
        return False

# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01    
def check_profit(choice, deposit):
    total = deposit[0]*0.25 + deposit[1]*0.10 + deposit[2]*0.05 + deposit[3]*0.01
    if total == Menu[choice]["cost"]:
        return True
    elif total > Menu[choice]["cost"]:
        return round(total - Menu[choice]["cost"], 2)
    else:
        return False
    
is_on = True
while is_on == True:
    a = input("What would yo u like to order? (espresso/latte/cappuccino): ")
    
    if a == "off":
        is_on = False
        break
    elif a == "espresso" or a == "latte" or a == "cappuccino":
        quarters = int(input("Put the number of quarters: "))
        dimes = int(input("Put the number of dimes: "))
        pennies = int(input("Put the number of pennies: "))
        nickles = int(input("Put the number of nickles: "))
        deposit = [quarters, dimes, nickles, pennies]
        money = check_profit(a, deposit)
        x = check(a, resources)
        if money == True and x == True:
            resources["water"] -= Menu[a]["ingredients"]["water"]
            resources["milk"] -= Menu[a]["ingredients"]["milk"]
            resources["coffee"] -= Menu[a]["ingredients"]["coffee"]
            print("Thank you for your purchase!")
            print(f"Here is your {a}")
            profit += Menu[a]["cost"]
        elif money == False and x == True:
            print("Insufficient amount.")
            print("Order Cancelled")
            print("Giving refund.")
        elif money == True and x == False:
            print("Insufficient resources,")
            print("We are sorry for the inconvinence but the order cannt be made.")
            print(f"Refunding ${money}")
        else:
            resources["water"] -= Menu[a]["ingredients"]["water"]
            resources["milk"] -= Menu[a]["ingredients"]["milk"]
            resources["coffee"] -= Menu[a]["ingredients"]["coffee"]
            print("Thank you for your purchase!")
            print(f"Here is your {a}")
            print(f"Returning change of ${money}")
            profit += Menu[a]["cost"]
    elif a == "report":
        print("Resources are as follow: ")
        print(f"water: {resources["water"]} ml")
        print(f"milk: {resources["milk"]} ml")
        print(f"coffee: {resources["coffee"]} g")
        print(f"Profit: ${profit}")
    else:
        print("Enter valid input")
        
