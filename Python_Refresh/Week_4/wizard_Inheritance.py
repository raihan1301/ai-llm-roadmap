class Wizard_Class:   # now student class and professor class both need name so  this is parent class
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name


class Student_Class(Wizard_Class):
    def __init__(self, name, house):  # now we have init method, i also want to use the functionality from wizard class
        super().__init__(name)   # so super means we are calling main class and after dot operator which function to use and it takes one variable so we pass name
        self.house = house


class Professor_Class(Wizard_Class):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject 


wizard = Wizard_Class("Abbas")
student = Student_Class("Raihan", "Kapadia")
professor = Professor_Class("Robin", "CS50P")