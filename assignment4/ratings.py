from matplotlib import pyplot as plt

"""
Name: read_ratings
Incoming data: filename
Outgoing data: names, ratings
Return: names, ratings
"""


def read_ratings(filename):
    names = []
    ratings = []
    with open(filename, "r") as file:
        for line in file:
            name, rating = line.strip().split(",")
            names.append(name)
            ratings.append(float(rating))
    return names, ratings


"""
Name: plot_ratings
Incoming data: names, ratings
Outgoing data: None
Return: None
"""


def plot_ratings(names, ratings):
    plt.bar(names, ratings)
    plt.xlabel("Professors")
    plt.ylabel("Ratings")
    plt.title("Professor Ratings")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


"""
Name: sort_ratings
Incoming data: names, ratings
Outgoing data: names_sorted, ratings_sorted
Return: names_sorted, ratings_sorted
"""


def sort_ratings(names, ratings):
    names_sorted, ratings_sorted = zip(*sorted(zip(names, ratings), key=lambda x: x[1]))
    return names_sorted, ratings_sorted


def main():
    filename = "./ratings-1.csv"
    names, ratings = read_ratings(filename)
    names_sorted, ratings_sorted = sort_ratings(names, ratings)
    plot_ratings(names_sorted, ratings_sorted)


if __name__ == "__main__":
    main()
