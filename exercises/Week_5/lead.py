import re
import asyncio
import time

class Lead:  # this is parent class
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


class HighValueLead(Lead):

    def __init__(self, name, email, phone, company, stage, contract_value):
        super().__init__(name, email, phone, company, stage )
        self.contract_value = float(contract_value)

    def is_priority(self):
        priority_threshold = 50000

        return self.is_valid() and self.contract_value >= priority_threshold  # check what happened if you put super.isvalid

    def to_dict(self):
        update_dict = super().to_dict()
        update_dict["Contract Value"] = self.contract_value
        update_dict["Priority Lead"] = self.is_priority()
        
        return update_dict


async def fetch_leads_mock():
    print("fetching two leads....")
    await asyncio.sleep(0.1)

    mock_lead = [ 
        HighValueLead(name = "John Smith", email = "john@gmail.com", phone = "519-555-1234", company = "Secure North", stage = "Qualified", contract_value = 75000),
        HighValueLead(name = "Sara Khan", email = "sara@gmail.com", phone = "416-555-1245", company = "CleanPro", stage = "New", contract_value = 20000)
        ]

    print("Mock leads fetched.")
    return mock_lead


def lead_from_terminal():

    print("Enter your lead information\n")
    name = input("Enter Owner Name: ")
    email = input("Enter Owner Email: ")
    phone = input("Enter Owner Phone: ")
    company = input("Enter Company Name: ")
    stage = input("Enter which stage this company is in: ")
    contract_value = input("Enter Contract Value: ")

    return HighValueLead(name = name, email = email, phone = phone, company = company, stage = stage, contract_value = contract_value)
    # basically when we call the def function it will return the input values to highvaluelead class
    # due to this all this value will be stored in self. variables accordingly both in highvalue lead and the parent of this class which is lead

async def process_lead(lead, delay):
    print(
        f"Started processing {lead.name} "
        f"(estimated {delay} seconds)"
    )

    await asyncio.sleep(delay)
    print(f"Finished processing {lead.name}")

    return lead.to_dict()


async def main(user_lead):
    start = time.perf_counter()

    mock_leads = await fetch_leads_mock()  
    # this will call the fetch_leads_mock and that will create two instance for highValueLead class and store in mock_lead list
    # that list will be returned and stored in mock_leads list

    all_leads = [ user_lead, mock_leads[0], mock_leads[1]]  # creating new list with terminal lead as well as mock lead
    
    print("\nStarting concurrent processing...\n")
    results = await asyncio.gather(
        process_lead(all_leads[0], 2.0),
        process_lead(all_leads[1], 1.5),
        process_lead(all_leads[2], 1.0)
    )

    elapsed = time.perf_counter() - start

    print("\nAll results:")
    for result in results:
        print(result)

    print(f"\nTotal time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    terminal_lead = lead_from_terminal()
    # we can put the terminal lead in def main also but than the event will stop till the user input

    asyncio.run(main(terminal_lead))

"""
But while the user is typing into input(), the event loop is blocked.
For this small terminal program, that would not cause a noticeable problem because no other async tasks have started yet.

At the time input() runs, the async event loop has not started yet, so nothing async is being blocked.

input from terminal is synchronise work

Normal input() waits for a human.
Async functions wait for APIs, databases, files, or other async tasks.
"""