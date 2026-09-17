def main():
    time_input = input("what time is it? ")
    time = convert(time_input)

    response = meal(time)
    print(response)

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

def meal(time):
    if 7.0 <= time <= 8.0:
        return "breakfast time"
    elif 13.0 <= time <= 14.0:
        return "lunch time"
    elif 21.0 <= time <= 22.0:
        return "dinner time"
    else:
        return "No meal available"

if __name__ == "__main__":
    main()