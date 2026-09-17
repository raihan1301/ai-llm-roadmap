def value_of_card(card):
    """Determine the scoring value of a card.
 
    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """

    if(card in 'JQK'):
          return 10
    if card == 'A':
          return 1
    return int(card)

def returning_two_values(card_one, card_two):
    """
    For scoring purposes, the value of J, Q or K is 10. The function should return which card has the higher value for scoring. 
    If both cards have an equal value, return both. Returning both cards can be done by using a comma in the return statement:

    """

    if(value_of_card(card_one) > value_of_card(card_two)):
        return card_one
    if(value_of_card(card_one) < value_of_card(card_two)):
        return card_two
    return(card_one, card_two)

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.
 
    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 11 (if already in hand); numerical value otherwise.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """

    if(card_one == 'A' or card_two == 'A'):
        return 1
    if(value_of_card(card_one) + value_of_card(card_two) <= 10):
         return 11
    return 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.
 
    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    return (card_one == 'A' and value_of_card(card_two) == 10) or (card_two == 'A' and value_of_card(card_one) == 10)
    # this will return true if score is 21 in two cards exact

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.
 
    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)
    # if the value of both card are queal it will be true

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.
 
    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    return 9 <= (value_of_card(card_one) + value_of_card(card_two)) <= 11

def main():
    result1 = value_of_card('K')
    print(result1)

    result2 = returning_two_values('K', '10')
    print(result2)

    result3 = value_of_ace('6', 'K')
    print(result3)

    result4 = is_blackjack('10', '9')
    print(result4)

    result5 = can_split_pairs('10', 'A')
    print(result5)

    result6 = can_double_down('A', '9')
    print(result6)

main()

