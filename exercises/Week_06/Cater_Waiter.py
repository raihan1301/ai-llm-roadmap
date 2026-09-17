from sets_categories_data import ALCOHOLS 
from sets_categories_data import VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE
from sets_categories_data import SPECIAL_INGREDIENTS
from sets_categories_data import example_dishes, EXAMPLE_INTERSECTION

def clean_ingredients(dish_name, ingredients):
    """
    this function should return the tuple
    ingredients should not be duplicate and hence we use set
    """
    return dish_name, set(ingredients)

def check_drinks(drink_name, ingredients):
    for ingredient in ingredients:
        if ingredient in ALCOHOLS:
            return drink_name + " Cocktail"
        else:
            return drink_name + " Mocktail"

def categorize_dish(dish_name, ingredients):
    for v, name in ((VEGAN, "VEGAN"),
        (VEGETARIAN, "VEGETARIAN"),
        (PALEO, "PALEO"),
        (KETO, "KETO"),
        (OMNIVORE, "OMNIVORE")):
        if set(ingredients) <= set(v):
            """
            Are all dish ingredients contained inside the allowed ingredients for this category?
            The <= with sets means subset.
            """
            return f"{dish_name}: {name}"
        

def tag_special_ingredients(dish):
    dish_name, ingredients = dish
    if SPECIAL_INGREDIENTS.intersection(set(ingredients)):
        allerges = SPECIAL_INGREDIENTS.intersection(set(ingredients))
        return dish_name, allerges

def compile_ingredients(dishes):
    return set.union(*dishes)
    """
    this will unpack dishes so all the dict and union will combine them, 
    we did not use ** because that is useful in key the keywods args and values
    set will remove the duplicate
    """

def separate_appetizers(dishes, appetizers):
    """
    so some name are same in dishes and apetizers
    we have to remove the apetizers name from dishes and remove duplicate as well if exist in dishes
    """
    return list(set(dishes) - set(appetizers))

def singleton_ingredients(dishes, INTERSECTIONS):
    singleton = (dish - INTERSECTIONS for dish in dishes)
    return set.union(*singleton)

def main():
    result1 = clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 
                                                        'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 
                                                        'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])
    print(result1)

    result2 = check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'])
    print(result2)

    result3 = categorize_dish('Sticky Lemon Tofu', {'tofu', 'soy sauce', 'salt', 'black pepper', 'cornstarch', 'vegetable oil', 'garlic', 
                                                    'ginger', 'water', 'vegetable stock', 'lemon juice', 'lemon zest', 'sugar'})
    print(result3)

    result4 = tag_special_ingredients(('Arugula and Roasted Pork Salad', ['pork tenderloin', 'arugula', 'pears', 'blue cheese', 
                                                                          'pine nuts', 'balsamic vinegar', 'onions', 'black pepper']))
    print(result4)

    dishes = [ {'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
           {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
           'balsamic vinegar', 'onions', 'black pepper'},
           {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}]

    result5 = compile_ingredients(dishes)
    print(result5)

    dishes =    ['Avocado Deviled Eggs','Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
             'Grilled Flank Steak with Caesar Salad','Vegetarian Khoresh Bademjan','Avocado Deviled Eggs',
             'Barley Risotto','Kingfish Lettuce Cups']
          
    appetizers = ['Kingfish Lettuce Cups','Avocado Deviled Eggs','Satay Steak Skewers',
              'Dahi Puri with Black Chickpeas','Avocado Deviled Eggs','Asparagus Puffs',
              'Asparagus Puffs']

    result6 = separate_appetizers(dishes, appetizers)
    print(result6)

    result7 = singleton_ingredients(example_dishes, EXAMPLE_INTERSECTION)
    print(result7)

main()