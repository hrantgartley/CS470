"""
Name: Grant Hartley
Class: CS 470
Desc: This program is a simple cash register for a store that sells carrots, coals, and top hats.
    and calculates the total for each customer. It also asks how many customers will be processed
    it also makes sure the input is a non-negative number
Date: 2024/1/24
"""

COAL_PRICE = 0.25
CARROT_PRICE = 0.75
TOP_HAT_PRICE = 4.50


# as the name suggests it makes sure all number inputed are positive
# i was going to "raise" and exception but causes program execution to halt at that point so canned that idea
def get_non_negative_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# process everything except loop
def process_customer():
    num_carrots = get_non_negative_input("How many carrots would you like? ")
    num_coals = get_non_negative_input("How many coals would you like? ")
    num_hats = get_non_negative_input("How many top hats would you like? ")

    print(f"Carrots: {num_carrots}")
    print(f"Coals: {num_coals}")
    print(f"Top Hats: {num_hats}")
    total = (
        num_carrots * CARROT_PRICE + num_coals * COAL_PRICE + num_hats * TOP_HAT_PRICE
    )
    print(f"Your total is ${total:.2f}")
    print()


# main function not needed but i did it because i can
def main():
    num_customers = get_non_negative_input("How many customers will be processed? ")

    for index in range(num_customers):
        print(f"\nProcessing customer {index + 1}:")
        process_customer()


# makes sure that code is run directly and not imported
if __name__ == "__main__":
    main()
