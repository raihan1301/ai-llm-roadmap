import csv

# check views.py for better refactoring

def main():
    with open("scourgify.csv","r") as file, open("scourgify_new.csv","w", newline="") as output_file:
        reader = csv.DictReader(file)

        writer = csv.DictWriter(
            output_file,
            fieldnames=["First_Name", "Last_Name", "House"]
        )

        writer.writeheader()
        
        for row in reader:
            first_name, last_name = row["name"].split(",")

            writer.writerow({
                "First_Name" : first_name.strip(),
                "Last_Name": last_name.strip(),
                "House": row["house"]
            })

main()