# def main():
#     student = get_student()

#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
    
#     print(f"{student[0]} from {student[1]}")

# def get_student():  # return the list
#     name = input("Name: ")
#     house = input("House: ")

#     return [name, house]

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():  # return the dict
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")

    return student  # return {"name": name, "house" : house}

if __name__ == "__main__":
    main()