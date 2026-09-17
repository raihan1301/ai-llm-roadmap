#***************** Version 1 ***************************#

# import random

# class Hat_class:

#     def __init__(self):  # whenever class is initiate like in line 15 this init class will run and add all the value in houses
#         self.houses = ["Gryffindor", "Ravenclaw", "Kapadia"]

#     def sort(self, name):
#         house = random.choice(self.houses)  # self.house is initiated above and pass in random function
#         print(name, "is in", {house})


# hat = Hat_class()
# hat.sort("Harry")   # this will sort which house he belongs to

# ******************************************************#


#***************** Version 2 ***************************#

import random

class Hat_class:

    houses = ["Gryffindor", "Ravenclaw", "Kapadia"]  # this can be acessible in any of the method below inside the class

    @classmethod   # we use cls
    def sort(cls, name):
        house = random.choice(cls.houses)  # self.house was instance variable accessible by self but now after cls it is class variable
        print(name, "is in", {house})


# hat = Hat_class()  # if we use classmethod we do no thave to instanciate the class object

Hat_class.sort("Harry")   # we use class name and than method after dot operator