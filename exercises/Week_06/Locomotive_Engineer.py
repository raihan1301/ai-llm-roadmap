def get_list_of_wagons(*args):  # multiple inputs
    """
    *args multiple inputs this can become a tuple,
    """
    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    misplace_w1, misplace_w2, locomotive, *remaining_wagons = each_wagons_id
    """
    this means in the list 0th will go to misplace_w1, 1st will got to w2, 
    3rd will be locomotive and 4th will be the remaining list
    """
    """
    now we want to return the list in this format
    locomotive, missing_wagons, remaining wagons, misplace 1 and 2
    """
    fixed_wagon = [locomotive, *missing_wagons, *remaining_wagons, misplace_w1, misplace_w2]
    return fixed_wagon


def add_missing_stops(route, **kwargs):
    """
    **kwargs means accept any number of names arguments in dictonary format key and value
    stop_1="Leipzig", stop_2="Hanover" become kwargs = { "stop_1": "Leipzig", "stop_2": "Hanover" }
    """
    """
    now we have to make dict, from kwargs using key as stops and add it with route
    """
    return {**route, "stops" : list(kwargs.values())}
    """
    **route will unpack the route aso it will have all the keys and values
    """

    
def extend_route_information(route, more_info):
    """
    Now in this we have route and more info in dict, we combine both but we dont know if there are more param
    so we use unpacking and make one dict
    if both have same key, later one wins so more_info value will be stored
    """
    return {**route, **more_info}


def fix_wagon_depot(wagons_rows):
    """
    * wagon_rows = this will unpack the outer list
    zip() = this will takes items at the same position: example, first items: 2,5,3 second items: 4,9,7
    map(list, ...) = converts every tuple into a list:
    outer list turn everything into one big giant list

    zip(           
    (1, 2, 3),   
    (4, 5, 6),
    (7, 8, 9)
    )

    [1, 4, 7]
    [2, 5, 8]
    [3, 6, 9]
    """
    return list(map(list, zip(*wagons_rows)))



def main():
    result1 = get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)
    print(result1)

    result2 = fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
    print(result2)

    result3 = add_missing_stops({"from": "New York", "to": "Miami"},
                      stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
                      stop_4="Jacksonville", stop_5="Orlando")
    print(result3)

    result4 = extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"})
    print(result4)

    result5 = fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ])
    print(result5)

main()