from vanity import is_valid

def test_valid_plates():
    assert is_valid("CS50") is True

def test_first_two_letter():
    assert is_valid("A123") is False
    assert is_valid("50CS") is False
    assert is_valid("AB25") is True 