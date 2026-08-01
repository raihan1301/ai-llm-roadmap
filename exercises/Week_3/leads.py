import csv

def main():

    with open("leads.csv","r") as file, open("clean_leads.csv","w", newline="") as clean_file, open("rejected_leads.csv","w",newline="") as rejected_file:
        data = csv.DictReader(file)

        clean_data = csv.DictWriter(
            clean_file,
            fieldnames=["Name", "Email", "Phone", "Company"]
        )

        rejected_data = csv.DictWriter(
            rejected_file,
            fieldnames = ["Name", "Email", "Phone", "Company", "Reason"]
        )

        clean_data.writeheader()
        rejected_data.writeheader()

        for row in data:
            valid_email = is_valid_email(row["email"])
            valid_phone = is_valid_phone(row["phone"])

            if valid_email and valid_phone:
                clean_data.writerow({
                    "Name" : row["name"],
                    "Email" : row["email"],
                    "Phone" : row["phone"],
                    "Company" : row["company"]
                })
            
            elif not valid_email and not valid_phone:
                rejected_data.writerow({
                    "Name" : row["name"],
                    "Email" : row["email"],
                    "Phone" : row["phone"],
                    "Company" : row["company"],
                    "Reason" : "Email is Not Valid as well as Phone is also not valid"
                })

            elif not valid_email:
                rejected_data.writerow({
                    "Name" : row["name"],
                    "Email" : row["email"],
                    "Phone" : row["phone"],
                    "Company" : row["company"],
                    "Reason" : "Email is Not Valid"
                })

            elif not valid_phone:
                rejected_data.writerow({
                    "Name" : row["name"],
                    "Email" : row["email"],
                    "Phone" : row["phone"],
                    "Company" : row["company"],
                    "Reason" : "Phone is Not Valid"
                })





def is_valid_email(email):
    return "@" in email

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

if __name__ == "__main__":
    main()