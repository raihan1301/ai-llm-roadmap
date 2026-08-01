import json

def main():
    with open("person.json", "r") as file:
        person = json.load(file)

    person["role"] = "AI/LLM Engineer"
    
    with open("person_updated.json", "w") as output_file:
        json.dump(person, output_file, indent=4)

if __name__ == "__main__":
    main()