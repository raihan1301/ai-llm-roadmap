class Student_class:
    def __init__(self, name, house):  # initialization of object
        
        #if house not in ["Gryffindor", "hufflepuff", "Kapadia"]:  # now we dont need this here because see [1]
            #raise ValueError("Invalid House")
        self.name = name
        self.house = house  # [1]this will going to call the setter method and we have error handle there
  
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name


    # Getter - means get some value
    @property
    def house(self): #def name should be same of what we kept in self. , so in this case it is self.house
        return self._house  # we also update the var to _house because if we keep the same self.house = house than it will call getter and setter again
    
    # Setter - means set some value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "hufflepuff", "Kapadia"]:
            raise ValueError("Invalid House") 
        self._house = house # we also update the var to _house because if we keep the same self.house = house than it will call getter and setter again

def main():
    student_var = get_student()
    print(student_var)  # this will call str method from class
    print(f"{student_var.name} from {student_var.house}")

    student_var._house = "Valhalla"  # this will get away from setter function because setter is house
    # so never touch the _ var in code
    print(f"{student_var.name} from {student_var.house}")


    # student_var.house = "Valhalla"  # now python will not let access this attribute the house and update value but now it will call setter function
    # print(f"{student_var.name} from {student_var.house}")

def get_student(): 
    name = input("Name: ")  
    house = input("House: ")

    return Student_class(name, house) 

if __name__ == "__main__":
    main()