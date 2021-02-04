from data import MENU, resources


# commands: Type 'report' for info about resources and cash taken.
#           type 'off' to turn off the machine and stop the program.
#           or select the options of coffee to have the coffee.

should_stop = False

total_cash = 0
water_left = resources["water"]
coffee_left = resources["coffee"]
milk_left = resources["milk"]

while not should_stop:

    type_of_coffee = input("Select your coffee: 'cappuccino', 'latte', 'espresso': ").lower()

    if type_of_coffee == "report":
        print(f"Water left: {water_left}")
        print(f"Coffee left: {coffee_left}")
        print(f"Milk left: {milk_left}")
        print(f"Total cash: {total_cash}")

    elif type_of_coffee == "off":
        print("Turning off machine.")
        should_stop = True
    else:
        water_needed = MENU[type_of_coffee]["ingredients"]["water"]
        coffee_needed = MENU[type_of_coffee]["ingredients"]["coffee"]
        milk_needed = MENU[type_of_coffee]["ingredients"]["milk"]
        price_coffee = round(MENU[type_of_coffee]["cost"], 2)

        print(f"{type_of_coffee} selected. Please pay ${price_coffee}")

        quarters_coins = int(input("How many quarters are you inserting: "))
        dimes_coins = int(input("How many dimes are you inserting: "))
        nickel_coins = int(input("How many nickels are you inserting: "))
        pennies_coins = int(input("How many pennies are you inserting: "))

        coins_inserted = (quarters_coins * 0.25) + (dimes_coins * 0.1) + (nickel_coins * 0.05) + (pennies_coins * 0.01)
        print(f"You have inserted a total of ${coins_inserted}.")

        change = round(coins_inserted - price_coffee, 2)

        if coins_inserted > price_coffee:

            print(f"Your change is ${change}")
        elif coins_inserted < price_coffee:
            print("Insufficient money, coins refunded")
            total_cash -= round(coins_inserted, 2)

        if milk_left < milk_needed or water_left < water_needed or coffee_left < coffee_needed:
            print("Not enough ingredients. Sorry. Please take your money back.")

        else:
            print(f"Here is your {type_of_coffee}. Enjoy!")
            total_cash += round(coins_inserted - change, 2)

            water_left -= water_needed
            coffee_left -= coffee_needed
            milk_left -= milk_needed


