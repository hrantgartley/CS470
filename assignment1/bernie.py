# this program calculates the total cost of bulk price, sales tax, shipping charge, and total price given the book price and number of books to be ordered
from random import randint


def bernie():
    # book_price = float(input("Enter the unit price of a single book: "))
    # num_books = int(input("Enter the quantity of books to be ordered: "))
    book_price = randint(15, 30)
    num_books = randint(133, 500)
    print(f"Book Price: ${book_price:.2f}")
    print(f"Number of Books: {num_books}")
    print("------------------------------------")

    bulk_price = book_price * num_books
    print(f"Bulk Price: ${bulk_price:.2f}")

    sales_tax = 0.092 * bulk_price
    print(f"Sales Tax: ${sales_tax:.2f}")

    shipping_charge_per_book = 2
    total_shipping_charge = shipping_charge_per_book * num_books
    print(f"Shipping Charge: ${total_shipping_charge:.2f}")

    total_price = bulk_price + sales_tax + total_shipping_charge
    print(f"Total Price: ${total_price:.2f}")


def main():
    bernie()


if __name__ == "__main__":
    main()
