def get_rounds(round):
    next_round = [round, round+1, round+2]
    return next_round

def concatenate_rounds(rounds_1, rounds_2):
    combine_rounds = rounds_1 + rounds_2
    #  rounds_1.extend(rounds_2); return rounds_1  we can do like this as well
    return combine_rounds

def list_contains_round(rounds, round_no):
    if round_no in rounds:
        return True
    return False

def card_average(rounds):
    sum_round = 0
    for round in rounds:
        sum_round = sum_round + round

    average = sum_round/len(rounds)
    return average

def approx_average_is_average(rounds):
    """
    She has thought of two ways of getting an average-like number:
    Take the average of the first and last number in the hand.
    Using the median (middle card) of the hand.
    """
    average = card_average(rounds)
    middle_value = 0

    if(len(rounds) % 2 != 0):
        middle_value = int(len(rounds) / 2) + 1

    start_value = rounds[0]
    end_value = rounds[len(rounds) - 1]

    two_num = (start_value + end_value) / 2

    if average == middle_value or average == two_num:
        return True

def average_even_is_average_odd(rounds):
    """
    Implement a function average_even_is_average_odd(<hand>) that returns a Boolean indicating 
    if the average of the cards at even indexes is the same as the average of the cards at odd indexes.
    """
    even_num = []
    odd_num = []

    for round in rounds:
        if round % 2 == 0:
            even_num.append(round)

        odd_num.append(round)

    even_average = card_average(even_num)
    odd_average = card_average(odd_num)

    if even_average == odd_average:
        return True
    return False
    

def maybe_double_last(rounds):
    """
    Implement a function maybe_double_last(<hand>) that takes a hand and checks if the last card is a Jack (11). 
    If the last card is a Jack (11), double its value before returning the hand.
    """
    if rounds[-1] == 11:
        rounds[-1] = 22

    return rounds


def main():
    result1 = get_rounds(27)
    print(result1)

    result2 = concatenate_rounds([27, 28, 29], [35, 36])
    print(result2)

    result3 = list_contains_round([27, 28, 29, 35, 36], 30)
    print(result3)

    result4 = card_average([5, 6, 7])
    print(result4)

    result5 = approx_average_is_average([2, 3, 4, 8, 8])
    print(result5)

    result6 = average_even_is_average_odd([1, 2, 3, 4])
    print(result6)

    result7 = maybe_double_last([5, 9, 11])
    print(result7)

main()