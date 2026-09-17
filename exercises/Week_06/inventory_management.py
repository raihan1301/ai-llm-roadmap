def create_inventory(list_item: list):
    dict_inventory = {}
    for item in list_item:
        dict_inventory[item] = dict_inventory.get(item, 0) + 1

    return dict_inventory


def add_items(inventory, list_item):
    dict_inventory = create_inventory(list_item)

    for key, value in inventory.items():
        dict_inventory[key] = dict_inventory.get(key, 0) + value

    return dict_inventory


def decrement_items(inventory, list_item):
    for item in list_item:
        inventory[item] = max(inventory.get(item, 0) - 1, 0)
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    inventory_list = []
    for key, value in inventory.items():
        inventory_list.append((key, value))

    # we can also do inventory_list = list(my_inventory.items())
    return inventory_list


def main():
    result1 = create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
    print(result1)

    result2 = add_items({"coal":1}, ["wood", "iron", "coal", "wood"])
    print(result2)

    result3 = decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])
    print(result3)

    result4 = remove_item({"coal":2, "wood":1, "diamond":2}, "coal")
    print(result4)

    result5 = list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})
    print(result5)

main()
