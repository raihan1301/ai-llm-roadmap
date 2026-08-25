import lead_cleaner

def test_normalize_phone():
    result = lead_cleaner.normalize_phone("(519) 555-1234")
    assert result == "5195551234"

def test_normalized_row():
    result = lead_cleaner.normalize_row({
        "name" : "  Raihan  ", 
        "email" : "RAIHAN@GMAIL.COM ",
        "phone" : "(519) 572-7862",
        "company" : " SmartOps ",
        "stage" : "Live "})

    assert result == {
        "name" : "Raihan", 
        "email" : "raihan@gmail.com",
        "phone" : "5195727862",
        "company" : "SmartOps",
        "stage" : "Live"
    }

def test_validation_errors():
    lead = lead_cleaner.Lead(
        "Raihan",
        "wrong-email",
        "5195727862",
        "SmartOps",
        "Live"
    )

    """
    validation_errors need Lead object not dict so we have to create an object first for lead 
    remember we import Lead in leadcleaner, even though it is class so we have to create an object first

    lead_cleaner.Lead is creating an object and storing in lead
    """

    result = lead_cleaner.get_validation_errors(lead)
    assert "Invalid Email" in result

def test_duplicate_reason():
    lead = lead_cleaner.Lead(
            "Raihan",
            "raihan@gmail.com",
            "5195727862",
            "SmartOps",
            "Live"
        )

    seen_emails = {"raihan@gmail.com"}   # seen_emails is also set but set is mentioned by {}
    seen_phones = set()

    result = lead_cleaner.get_duplicate_reason(lead, seen_emails, seen_phones)
    assert result == ["Duplicate Email"]


def test_process_leads(tmp_path):
    csv_file = tmp_path / "test_leads.csv" 

    csv_file.write_text(
        "name,email,phone,company,stage\n"
        "Raihan,raihan@gmail.com,5195551234,SmartOps,Live\n"
        "Duplicate,raihan@gmail.com,4165551234,ABC,New\n"
        "Invalid,bad-email,6475551234,XYZ,New\n"
    )

    result = lead_cleaner.process_leads(csv_file)

    assert result["total"] == 3
    assert result["clean"] == 1
    assert result["duplicates"] == 1
    assert result["errors"] == 1