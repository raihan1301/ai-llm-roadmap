import argparse
import re
import pandas as pd

from lead import Lead


REQUIRED_COLUMNS = [
    "name",
    "email",
    "phone",
    "company",
    "stage",
]


def parse_arguments():
    parser = argparse.ArgumentParser(  #so if they do this "python lead_cleaner.py --help" it will say what this pythong function will do
        description="Clean and categorize SmartOps leads."
    )

    # Add required --input argument.
    parser.add_argument(
        "--input",
        required=True,
        help = "path to the leads csv file"
    )

    return parser.parse_args()  #reads what the user typed in the terminal. and return the value


def normalize_phone(phone):
    # Convert value to string.
    # Remove all non-digit characters.
    return re.sub(r"\D", "", str(phone)) #Remove everything that is not a digit. and change it by nothing ""


def normalize_row(row):
    # Return a dictionary containing normalized values.
    return {
        "name" : str(row["name"]).strip(),
        "email" : str(row["email"]).strip().lower(),
        "phone" : normalize_phone(row["phone"]),  
        "company" : str(row["company"]).strip(),
        "stage" : str(row["stage"]).strip()
    }


def get_validation_errors(lead):
    errors = []

    # Validate name, email, phone, company, and stage.
    # we only validate email and phone in lead.py so remaining has to be done here
    
    if not lead.name:
        errors.append("Missing Name")
    if not lead.is_valid_email():
        errors.append("Invalid Email")
    if not lead.is_valid_phone():
        errors.append("Invalid Phone")
    if not lead.company:
        errors.append("Company Name Missing")
    if not lead.stage:
        errors.append("Company Stage Missing")

    return errors


def get_duplicate_reason(lead, seen_emails, seen_phones):
    # Check duplicate email and phone.
    
    duplicate_reasons = []

    if lead.email in seen_emails:
        duplicate_reasons.append("Duplicate Email")
    if lead.phone in seen_phones:
        duplicate_reasons.append("Duplicate Phone")

    return duplicate_reasons



def process_leads(input_path):
    # Confirm file exists and Read CSV with pandas.
    """
    we can use this " with open(input_path, "r") as leads: " this will throw error if file not found
    but in this project we will use panda lib so lets do with that
    """

    try:
        leads = pd.read_csv(input_path).fillna("")  
        """
        Above code: 
        Open this CSV file and convert it into a Pandas table. creates something called a DataFrame.
        Then later we can loop through those rows.

        empty CSV cells may become Pandas NaN. Then this: str(row["company"]).strip() if its empty it will become nan 
        and valid function will fail because nan is a string so it will count as word
        
        .fillna("")  means Now blank cells remain effectively blank.
        """
    except FileNotFoundError:
        raise FileNotFoundError( f"{input_path} does not exist")
   

    # Confirm all required columns exist.
    missing_columns = []

    for column in REQUIRED_COLUMNS:  # loop through the required columns
        if column not in leads.columns:  # if that column not present in leads column
            missing_columns.append(column)  # add into missing column

    if missing_columns:  # if there is any value in list than raise error
        raise ValueError( f"{input_path} has missing required columns: {missing_columns}")

    # These store the final categorized records. [{},{},{}]
    clean_rows = []
    duplicate_rows = []
    error_rows = []

    # these are used to remember which email addresses and phone numbers we've already processed. For duplicate detection, set() is the right choice.
    seen_emails = set()  
    seen_phones = set()

    # Loop through rows.
    for index, row in leads.iterrows():

        """
        it is panda function and iterrows() returns two things for every row. (index, row_data)
        Normalize each row - we already do in lead.py but still we will do it here because we will use the value in duplicate detetction
        we have a function above where we pass all the data for normalization

        row is not a normal Python dict. It is a Pandas Series

        """

        data = normalize_row(row)  
        # Create Lead object.
        lead = Lead(data["name"], data["email"], data["phone"], data["company"], data["stage"])

        # Validate it.
        errors = get_validation_errors(lead)

        # invalid lead
        if errors:
            lead_data = lead.to_dict()
            lead_data["Reason"] = "; ".join(errors)

            """
            we used this above : "; ".join(errors) because if there are many errors it has to be join into one string
            errors = [ "Invalid email", "Missing company" ]  ---> converts to "Invalid email; Missing company"
            """

            error_rows.append(lead_data)
            continue   # this keyword continue means it will skip the rest of the below code and move to next row with top for loop
            # if i remove the continue than it will keep going for below code and enter the other if statements if condition was right

        # Check duplicate.
        duplicate_reasons = get_duplicate_reason(lead, seen_emails, seen_phones)

        if duplicate_reasons:
            lead_data = lead.to_dict()
            lead_data["Reason"] = "; ".join(duplicate_reasons)

            duplicate_rows.append(lead_data)
            continue

        clean_rows.append(lead.to_dict())

        seen_emails.add(lead.email)
        seen_phones.add(lead.phone)  # this so next time if same data comes it will be found as duplicate
    

    # Write clean.csv.
    pd.DataFrame(clean_rows).to_csv("clean.csv", index=False)

    """
    pd.DataFrame(clean_rows) means takes your list of dictionaries and turns it into a table.
    .to_csv("clean.csv", index=False) means writes that table into clean.csv.
    index=False means Do not add the Pandas row numbers 0,1,2,3... as an extra CSV column.
    """

    # Write duplicates.csv.
    pd.DataFrame(duplicate_rows).to_csv("duplicates.csv", index=False)

    # Write errors.csv.
    pd.DataFrame(error_rows).to_csv("errors.csv", index=False)

    # below we will return the summary in a dict and it will be returned to main function
    return {
        "total": len(leads),
        "clean": len(clean_rows),
        "duplicates": len(duplicate_rows),
        "errors": len(error_rows),
    }


def print_summary(summary):
    # Print a readable console summary.
    print()
    print("SmartOps Lead Cleaner Summary")
    print("-----------------------------")
    print(f"Total rows:       {summary['total']}")
    print(f"Clean leads:      {summary['clean']}")
    print(f"Duplicate leads:  {summary['duplicates']}")
    print(f"Invalid leads:    {summary['errors']}")

    # here we have use the dict values we got from the dict keys


def main():
    args = parse_arguments()

    try:
        summary = process_leads(args.input)  # whatever is the input it will be send to this function process_leads
        print_summary(summary)

    except FileNotFoundError as error:
        print(f"File error: {error}")

    except ValueError as error:
        print(f"Data error: {error}")


if __name__ == "__main__":
    main()