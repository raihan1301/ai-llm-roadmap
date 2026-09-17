import re

class Lead_Class:

    def __init__(self, name, email, phone, company, stage):
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company
        self.stage = stage
        self.lead_Dict = {}
        self.lead_Score = 0
    
    def __str__(self):
        return str(self.lead_Dict)
    
    def is_valid(self, email, phone):
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"
        phone_regex = r"^(\+?\d{1,3})?[-.\s]?(\(?\d{3}\)?)?[-.\s]?\d{3}[-.\s]?\d{4}$"

        if email:
            if re.fullmatch(email_regex, email):
                return True
        
        if phone:
            if re.fullmatch(phone_regex, phone):
                return True

    def score(self):
        self.lead_Score += 5
    
    def to_dict(self):
        self.lead_Dict = {
            "Owner Name" : self.name,
            "Owner Email" : self.email,
            "Owner Phone" : self.phone,
            "Company Name" : self.company,
            "Company Stage" : self.stage,
            "Lead Score" : self.lead_Score
        }


def main():
    name_var = input("Enter Owner Name: ")
    email_var = input("Enter Owner Email: ")
    phone_var = input("Enter Owner Phone: ")
    company_var = input("Enter Company Name: ")
    stage_var = input("Enter which stage this company in: ")

    lead = Lead_Class(name_var, email_var, phone_var, company_var, stage_var)
    
    if name_var:
        lead.score()

    if email_var:
        is_valid = lead.is_valid(phone="",email=email_var)
        if is_valid:
            lead.score()
    
    if phone_var:
        is_valid = lead.is_valid(phone=phone_var, email="")
        if is_valid:
            lead.score()
    
    if company_var:
        lead.score()
    
    if stage_var:
        lead.score()
    
    lead.to_dict()

    print(lead)

if __name__ == "__main__":
    main()
    



    
