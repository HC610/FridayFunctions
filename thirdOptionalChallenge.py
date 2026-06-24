import sys
import json

def add_order():
    filename = sys.argv[1]
    table_number = str(sys.argv[2])
    neworder = sys.argv[3]

    with open(filename) as jsonfile:
        orders = json.load(jsonfile)

    with open(filename, "w") as updated_json:
        if table_number in orders:
            # Finds the key and appends
            orders[table_number].append(neworder)
        else:
            orders[table_number] = [neworder]
        json.dump(orders, updated_json)

add_order()


    



