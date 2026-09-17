import random

class Package_class:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
    
    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight} Kg"
    
    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():

    number_var = random.randint(1, 100)
    sender_var = input("Enter Sender Name: ")
    recipient_var = input("Enter Recipient Name: ")
    weight_var = float(input("How much is the weight for package (just number in kg): "))
    cost_var = float(input("Enter the current rate of per kg cost: "))

    package = Package_class(number_var, sender_var, recipient_var, weight_var)
    print(f"{package} costs ${package.calculate_cost(cost_var)}")


if __name__ == "__main__":
    main()