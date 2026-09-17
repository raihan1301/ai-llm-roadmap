from datetime import date
import inflect

def main():
    birth_date = input("Date of Birth in YYYY-MM-DD Format: ")
    birth_date = date.fromisoformat(birth_date)
    minutes = calculate_minutes(birth_date)

    print(convert_to_words(minutes))


def calculate_minutes(birthdate):
    difference = date.today() - birthdate
    print(difference)
    return round(difference.total_seconds() / 60)


def convert_to_words(min):
    engine = inflect.engine()

    words = engine.number_to_words(min, andword="")
    return f"{words.capitalize()} minutes"

main()