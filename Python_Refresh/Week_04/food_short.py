class Food_class:

    base_hearts = 1 #class variable

    def __init__(self, ingredients):
        self.ingredients =ingredients
        self.hearts = Food_class.calculate_hearts(ingredients)
    
    @classmethod
    def calculate_hearts(cls, ingredients):
        
        hearts = cls.base_hearts

        for ingredient in ingredients:
            hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingredients=[])
        food.hearts = hearts
        return food

def main():
    mushroom_skewer = Food_class(ingredients=["Mushroom", "Hearty Mushroom"])  # we initialize the ingredients and hearts here
    print(f" this skewer heals {mushroom_skewer.hearts} hearts!")

    mushroom_skewer = Food_class.from_nothing(hearts = 2)
    print(f" this skewer heals {mushroom_skewer.hearts} hearts!")


main()