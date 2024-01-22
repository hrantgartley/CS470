# desc this program calculates the total cost of items given the number of each item
from random import randint

COAL_PRICE = 0.25
CARROT_PRICE = 0.75
TOP_HAT_PRICE = 4.50


def sally():
    # num_carrots = int(input("How many carrots would you like? "))
    # num_coals = int(input("How many coals would you like? "))
    # num_hats = int(input("How many top hats would you like? "))

    num_carrots = randint(1, 25)
    num_coals = randint(1, 25)
    num_hats = randint(1, 25)
    print(f"Carrots: {num_carrots}")
    print(f"Coals: {num_coals}")
    print(f"Top Hats: {num_hats}")
    total = (
        num_carrots * CARROT_PRICE + num_coals * COAL_PRICE + num_hats * TOP_HAT_PRICE
    )
    print(f"Your total is ${total:.2f}")


def main():
    sally()


if __name__ == "__main__":
    main()
