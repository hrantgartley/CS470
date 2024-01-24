"""
Grant Hartley
Class: CS 470
Description: This program calculates the total price of a book order but also checks for valid input.
        as well as the total price of all orders and number of customers processed.
Date: 2024/23/01
"""


def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# gets a valid integer input from the user (non-negative)
def get_valid_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# calculates the bulk price of the order
def calculate_bulk_price(book_price, num_books):
    return book_price * num_books


# calculates the sales tax for the order
def calculate_sales_tax(bulk_price):
    return 0.092 * bulk_price


# calculates the total shipping charge for the order
def calculate_shipping_charge(num_books):
    shipping_charge_per_book = 2
    return shipping_charge_per_book * num_books


# calculates the total price of the order
def calculate_total_price(bulk_price, sales_tax, total_shipping_charge):
    return bulk_price + sales_tax + total_shipping_charge


# processes customer input and calculates the total price of the order
def process_customer():
    book_price = get_valid_float_input("Enter the unit price of a single book: ")
    num_books = get_valid_int_input("Enter the quantity of books to be ordered: ")

    print(f"Book Price: ${book_price:.2f}")
    print(f"Number of Books: {num_books}")
    print("------------------------------------")

    bulk_price = calculate_bulk_price(book_price, num_books)
    print(f"Bulk Price: ${bulk_price:.2f}")

    sales_tax = calculate_sales_tax(bulk_price)
    print(f"Sales Tax: ${sales_tax:.2f}")

    total_shipping_charge = calculate_shipping_charge(num_books)
    print(f"Shipping Charge: ${total_shipping_charge:.2f}")

    total_price = calculate_total_price(bulk_price, sales_tax, total_shipping_charge)
    print(f"Total Price: ${total_price:.2f}")

    return total_price


def main():
    total_customers = 0
    total_sales = 0

    while True:
        total_customers += 1
        total_sales += process_customer()

        choice = input("Would you like to process another customer? (y/n): ")
        if choice.lower() != "y":
            print("Goodbye!")
            break

    print(f"Number of customers processed: {total_customers}")
    print(f"Total sales for all customers: ${total_sales:.2f}")


if __name__ == "__main__":
    main()
