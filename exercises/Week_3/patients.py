import json

def main():
    with open("patients.json","r") as input_file:
        data = json.load(input_file)
    
    for hospital in data["hospitals"]:
        print(f"hospital name {hospital["name"]}")

        for department in hospital["departments"]:
            print(f"department name {department["name"]}")

            for patient in department["patients"]:
                print(f"patient name {patient["name"]}")

                if patient["id"] == 102:
                    print(f"patient status {patient["status"]}")
                    patient["status"] = "Discharged"
                
                    print(
                        f"patient found in {hospital["name"]},"
                        f"{department["name"]} department"
                    )

                    break
                break       
            break
        break

    with open("patients.json","w") as output:
        json.dump(data, output, indent = 4)

main()
            
    