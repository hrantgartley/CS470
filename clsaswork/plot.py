import matplotlib.pyplot as plt

x = ["Jan", "Feb", "Mar", "Apr", "May"]
y = [22, 23, 27, 43, 55]

# plt.bar(x, y)
plt.plot(x, y)
plt.title("Sales")
plt.xlabel("Months")
plt.ylabel("Car Sales")

plt.show()
