def get_coordinate(treasure_pair):
    return treasure_pair[1]


def convert_coordinate(coordinate):
    result = (coordinate[0], coordinate[1])
    # you can use tuple(coordinate) as well
    return result


def compare_records(treasure_pair, coordinate_quadrant):
    coordinate = get_coordinate(treasure_pair)
    converted_coordinate = convert_coordinate(coordinate)

    if converted_coordinate == coordinate_quadrant[1]:
        return True

    return False


def create_record(treasure_pair, coordinate_quadrant):
    match = compare_records(treasure_pair, coordinate_quadrant)

    if match:
        return treasure_pair + coordinate_quadrant

    return "Not a Match"


def clean_up(combined_record_group):
    return "".join([f"{(record[0], record[2], record[3], record[4])}\n" for record in combined_record_group])



def main():
    result1 = get_coordinate(('Scrimshawed Whale Tooth', '2A'))
    print(result1)

    result2 = convert_coordinate("2A")
    print(result2)

    result3 = compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple'))
    print(result3)

    result4 = create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
    print(result4)

    result5 = clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')))
    print(result5)

main()
