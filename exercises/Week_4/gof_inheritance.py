class Dog:
    species = "canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound="dubdub"):
            return f"{self.name} bark {sound}"


class JackRussell(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    def speak(self, sound="chub"):
            return super().speak(sound)

class Bulldog(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

def main():
    miles = JackRussell("Miles", 4)  # this will instantiate Dog Class because dog is parent class for JackRuseell
    print(miles)
    print(miles.speak()) # we are accessing the child class jackrussell speak method from parent class instance

    # you can still call miles with different speak as you can update the value
    print(miles.speak("Grrr"))

    solem = Dachshund("Solem", 4)  # this will instantiate Dog Class because dog is parent class for JackRuseell
    print(solem)
    print(solem.speak())

    print(solem.speak("tata"))

main()

# you can use type() to know object belongs to which type like type(miles)
# if you want to check instance you can do with isinstance(miles, Dog)  it takes object and class as parameter