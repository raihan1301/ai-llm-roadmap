#***************** Version 1 *********************#

# class Student_class:
#     ...

# def main():
#     student_var = get_student()
#     print(f"{student_var.name} from {student_var.house}")

# def get_student(): 
#     student = Student_class()  # create object from class
#     student.name = input("Name: ")  # we are putting this attribute in our class
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()

# ******************************************************#


#***************** Version 2 ***************************#

# class Student_class:
#     def __init__(self, name, house):  # initialization of object
#         self.name = name
#         self.house = house

# def main():
#     student_var = get_student()
#     print(f"{student_var.name} from {student_var.house}")

# def get_student(): 
#     name = input("Name: ")  
#     house = input("House: ")
#     student = Student_class(name, house)   # this can also said as constructor call
#     return student

# if __name__ == "__main__":
#     main()


# ******************************************************#


#***************** Version 3 ***************************#

# class Student_class:
#     def __init__(self, name, house):  # initialization of object
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["Gryffindor", "hufflepuff", "Kapadia"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return "A student"

# def main():
#     student_var = get_student()
#     print(student_var)  # this will call str method from class
#     print(f"{student_var.name} from {student_var.house}")

# def get_student(): 
#     name = input("Name: ")  
#     house = input("House: ")
#     return Student_class(name, house)

# if __name__ == "__main__":
#     main()

# ******************************************************#


#***************** Version 4 ***************************#

class Student_class:
    def __init__(self, name, house, patronus):  # initialization of object
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "hufflepuff", "Kapadia"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus  # so we getting this value from get_student 
                                 #once inside the self you can call it from any function inside the class
    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):  # create our own function inside our class
        match self.patronus:   #self.patronus is defined in init function above already  # match and case are keyword
            case "Stag":
                return "Horse"
            case "Otter":
                return "Fish"
            case _:
                return "nothing"

def main():
    student_var = get_student()
    print(student_var)  # this will call str method from class
    print(f"{student_var.name} from {student_var.house}")
    
    print("Expecto patronus")
    print(student_var.charm())

    student_var.house = "Valhalla"  # we are changing house value directly even if its not in list which is not good
    print(f"{student_var.name} from {student_var.house}")

def get_student(): 
    name = input("Name: ")  
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student_class(name, house, patronus) 

if __name__ == "__main__":
    main()

    # property and decorator are in different file