def generate_seat_letters(number):
    letters = ["A","B","C","D"]

    for index in range(number):
        yield letters[index % 4]
    """
    This is a generator function. Instead of creating and returning a whole list of seat letters, 
    it produces one value at a time using yield. The list contains A, B, C, D, and index % 4 keeps cycling through indexes 0, 1, 2, 3, 
    0, 1.... So if you request 6 letters, it generates A, B, C, D, A, B. 
    The important concept is that yield pauses the function after returning each value and continues from that position 
    the next time a value is requested.
    """

def generate_seats(number):
    for index in range(number):
        row = (index // 4) + 1

        #arilines skips row 13
        if row >=13:
            row += 1

        seat_letter = ["A","B","C","D"][index % 4]
        yield f"{row}{seat_letter}"
    """
    This function also uses a generator, but now it combines the row number with a seat letter. 
    Since there are four seats per row, index // 4 determines which row we're on: 
    indexes 0-3 belong to row 1, 4-7 belong to row 2, and so on. We add 1 because Python indexes start at zero. 
    If the calculated row reaches 13 or higher, we add one so row 13 is skipped. 
    The seat letter again comes from index % 4, and yield produces values such as 1A, 1B, 1C, 1D, 2A, etc. 
    """

def assign_seats(passengers):
    seat_assignments = {}

    seats = generate_seats(len(passengers))

    for passenger in passengers:
        seat_assignments[passenger] = next(seats)
        """
        as we know generate_seats is generator and it yield after giving one value so line 35 will only get one generated seat
        so for seat assignment on line 38 we ask generator of generate_Seats to give us next seats so we can assign it
        """

    return seat_assignments
    """
    This function takes a list of passenger names and creates an empty dictionary called seat_assignments. 
    It asks generate_seats() to create exactly as many seats as there are passengers. 
    Then the loop goes through each passenger, and next(seats) requests the next available seat from the generator. 
    That passenger becomes the dictionary key and the generated seat becomes the value. 
    So you end up with something like {"Raihan": "1A", "Nasira": "1B"}. 
    Unlike the first two functions, this function returns a normal dictionary rather than a generator.
    """

def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        code = seat + flight_id

        code = code.ljust(12, "0")
        yield code
    """
    This function creates a unique ticket code by joining the seat number with the flight ID. 
    For example, 1A + CO1234 becomes 1ACO1234. The exercise requires the final code to contain exactly 12 characters, 
    so ljust(12, "0") pads the right side with zeroes until the string reaches length 12. 
    Then yield returns each ticket code one at a time. 
    Importantly, we're looping through seat_numbers rather than removing items from the input list, so the original list is not modified.
    """

def main():
    letters = generate_seat_letters(4)
    print(next(letters))
    print(next(letters))

    seats = generate_seats(10)
    print(next(seats))
    print(next(seats))

    passengers = ['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']
    assigned_seats = assign_seats(passengers)
    print(assigned_seats)

    seat_numbers = ['1A', '17D']
    flight_id = 'CO1234'
    ticket_ids = generate_codes(seat_numbers, flight_id)

    print(next(ticket_ids))
    print(next(ticket_ids))

main()