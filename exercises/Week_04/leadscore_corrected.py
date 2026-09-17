import re


class Lead:
    def __init__(self, name, email, phone, company, stage):
        self.name = name.strip()
        self.email = email.strip()
        self.phone = phone.strip()
        self.company = company.strip()
        self.stage = stage.strip()

    def __str__(self):
        return (
            f"{self.name} | {self.company} | "
            f"{self.stage} | Score: {self.score()}"  # we called score function here 
        )

    def is_valid_email(self):
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        return re.fullmatch(email_regex, self.email) is not None

    def is_valid_phone(self):
        phone_regex = (
            r"^(\+?\d{1,3})?[-.\s]?"
            r"(\(?\d{3}\)?)?[-.\s]?"
            r"\d{3}[-.\s]?\d{4}$"
        )

        return re.fullmatch(phone_regex, self.phone) is not None

    def is_valid(self):
        return self.is_valid_email() and self.is_valid_phone()

    def score(self):
        lead_score = 0

        if self.name:
            lead_score += 5

        if self.is_valid_email():
            lead_score += 5

        if self.is_valid_phone():
            lead_score += 5

        if self.company:
            lead_score += 5

        if self.stage:
            lead_score += 5

        return lead_score

    def to_dict(self):
        return {
            "Owner Name": self.name,
            "Owner Email": self.email,
            "Owner Phone": self.phone,
            "Company Name": self.company,
            "Company Stage": self.stage,
            "Lead Score": self.score(),
            "Valid Lead": self.is_valid(),
        }


def main():
    name = input("Enter Owner Name: ")
    email = input("Enter Owner Email: ")
    phone = input("Enter Owner Phone: ")
    company = input("Enter Company Name: ")
    stage = input("Enter which stage this company is in: ")

    lead = Lead(name, email, phone, company, stage)

    print()
    print(lead)
    print(lead.to_dict())

    if lead.is_valid():
        print("Email and phone are valid.")
    else:
        print("Email or phone is invalid.")


if __name__ == "__main__":
    main()