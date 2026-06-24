import sys

# file = open("Order.txt", "r")
# content = file.read()
# print(content)
# file.close

# orders = [
#     "Curry",
#     "Chocolate",
#     "Rice"
# ]

# with open('order.txt', "a+") as file:
#     file.write('\n'.join(orders))
#     file.close()

# a+ append

# New file

# QUESTION 1 22 / 6
# import sys

# args = sys.argv

# if len(args) > 1:
#     order = " ".join(args[1:])

#     with open("orders.txt", "a") as file:
#         file.write(order + "\n")

# QUESTION 2

import sys

filename = sys.argv[1]

file = open(filename, "r")
lines = file.readlines()
file.close()

orders = [line.strip() for line in lines]

counts = {}

for order in orders:
    if order in counts:
        counts[order] += 1
    else:
        counts[order] = 1

for dish, count in counts.items():
    print(dish, ":", count)
