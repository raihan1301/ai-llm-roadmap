class Student_class:
    def __init__(self, name, house):  # initialization of object
        self.name = name
        self.house = house  # [1]this will going to call the setter method and we have error handle there
  
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):     # i can call this method without instancing the object
        name = input("Name: ")  
        house = input("House: ")
        return cls(name, house)   #return new student object in reference to the class


def main():
    student_var = Student_class.get()
    print(student_var)
    print(f"{student_var.name} from {student_var.house}")
 

if __name__ == "__main__":
    main()