# define contants
COAL_PRICE = 0.25
CARROT_PRICE = 0.75
HAT_PRICE = 4.50


# function to calculate and return total price
def get_total_price(num_coals, num_carrots, num_hats):
    return num_coals * COAL_PRICE + num_carrots * CARROT_PRICE + num_hats * HAT_PRICE


def read_customer_data(file_name):
    customers = []
    coals = []
    carrots = []
    hats = []
    with open(file_name, "r") as file:
        for line in file:
            data = line.strip().split()
            customers.append(data[0])
            coals.append(int(data[1]))
            carrots.append(int(data[2]))
            hats.append(int(data[3]))
    return customers, coals, carrots, hats


def main():
    customers, coals, carrots, hats = read_customer_data("data.txt")

    print("Customer\tCoal\tCarrot\tTophat\tTotal")
    for i in range(len(customers)):
        total_price = get_total_price(coals[i], carrots[i], hats[i])
        print(
            f"{customers[i]}\t\t{coals[i]}\t{carrots[i]}\t{hats[i]}\t{total_price:.2f}"
        )


if __name__ == "__main__":
    main()
