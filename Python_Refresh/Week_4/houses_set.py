#***************** Version 1 ***************************#

students = [
    {"name" : "Hermione", "house": "Gryffindor"},
    {"name" : "Harry", "house": "Gryffindor"},
    {"name" : "Ron", "house": "Gryffindor"},
    {"name" : "Draco", "house": "Slytherin"},
    {"name" : "Padma", "house": "Ravenclaw"}
]

houses = []

# we want to add only houses one time no duplicate without set function
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)

# ******************************************************#


#***************** Version 2 ***************************#

houses = set()

# we want to add only houses one time no duplicate without set function
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

# ******************************************************#


#***************** Version 3 ***************************#

# this is for filter function

def is_students(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_students, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):  # key is random with var s and s return with name so s:["name"]
    print(gryffindor)


# ******************************************************#


#***************** Version 4 ***************************#

# this will create list and in list there will be a dictionary

mens = ["harry", "raihan", "rizwan"]

kapadia = [{"name": men, "house": "Kapadia"} for men in mens]
print(kapadia)

# ******************************************************#


#***************** Version 5 ***************************#

# this is for enumerate

for i, men in enumerate(mens):
    print(i+1, men) 