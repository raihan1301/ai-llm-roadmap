import csv

def main():
    
    calories= {}

    while True:
        decision = ask_decision("question")

        if decision.lower() == "yes":
            with open ("calories.txt","a",newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["Fruit", "Calories"])
            
                record = Add_Record()
                writer.writerow(record)

        if decision.lower() != "yes":
            decision = ask_decision("response")

            if decision.lower() != "yes":
                break

            with open ("calories.txt",newline="") as file:
                reader = csv.DictReader(file)

                response = Give_Response()

                for fruit in reader:
                    if fruit["Fruits"].lower() == response.lower():
                        print(f" {response} has {fruit['Calories']} calorie")

def ask_decision(type):
    if type == "question":
        decision = input("Do you want to add a fruit, type yes ? ")
    else:
        decision = input("Do you want to find a calorie for fruit, type yes ? ")
            
    return decision


def Add_Record():
    Fruit = input("Enter fruit name = ")
    calories = input(f"How much calorie {Fruit} contains ?")

    return {"Fruit" : Fruit, "Calories": calories}

def Give_Response():
    Fruit = input("Enter fruit name to see the calorie = ")
    return Fruit

main()