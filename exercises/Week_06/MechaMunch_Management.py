def add_item(cart, items):

    for item in items:
        cart[item] = cart.get(item, 0) + 1
    return cart

def read_notes(items):
    cart = add_item({} ,items)
    #  cart = dict.fromkeys(notes,1)
    return cart

def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart

def send_to_store(cart,aisle_map):
    complete_cart = {}

    for key, value in cart.items():
        complete_cart[key] = [value] + aisle_map[key]

    return sorted(complete_cart.items(), reverse=True)        

def update_store_inventory(cart, inventory):
    for key in cart.keys():
        inventory[key][0] -= cart[key][0]
        if inventory[key][0]<=0:
            inventory[key][0]="Out of Stock"
    return inventory


def main():
    result1 = add_item({'Banana': 3, 'Apple': 2, 'Orange': 1}, ('Apple', 'Apple', 'Orange', 'Apple', 'Banana'))
    print(result1)

    result2 = read_notes(['Blueberries', 'Pear', 'Orange', 'Banana', 'Apple'])
    print(result2)

    result3 = sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 4})
    print(result3)

    result4 = send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
                  {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]})
    print(result4)

    result5 = update_recipes( {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
                                'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
                                (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),))
    print(result5)

    result6 = update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
                                    {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]})
    print(result6)

main()
