import leads

def test_valid_email():
    assert leads.is_valid_email("raihan@gmail.com") is True
    assert leads.is_valid_email("raihangmail.com") is False

def test_valid_phone():
    assert leads.is_valid_phone("5195727866") is True
    assert leads.is_valid_phone("1234") is False