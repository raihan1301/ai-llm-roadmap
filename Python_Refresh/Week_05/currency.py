def exchange_money(budget, exchange_rate):
    """
    If your currency is USD and you want to exchange USD for EUR with an exchange rate of 1.20, then 1.20 USD == 1 EUR.
    budget is in usd and exchange rate is in eur

    budget = The amount of money you are planning to exchange.
    exchange_rate = The amount of domestic currency equal to one unit of foreign currency.

    This function should return the value of the exchanged currency.
    """

    exchanged_currency = budget/exchange_rate
    return exchanged_currency

def get_change(budget, exchange_value):
    """
    budget = Amount of money before exchange.
    exchange_value = Amount of money that is taken from the budget to be exchanged.

    This function should return the amount of money that is left from the budget.
    """
    budget_left = budget - exchange_money(exchange_value, 1.2)
    return budget_left

def get_value_of_bills(denomination, no_of_bills):
    """
    denomination = The value of a single bill.
    number_of_bills = The total number of bills.

    The total you receive must be divisible by the value of one "bill" or unit, which can leave behind a fraction or remainder. 
    Your function should return only the total value of the bills 
    """
    return denomination * no_of_bills

def get_number_of_bills(amount, denomnation):
    """
    This function should return the number of currency bills that you can receive within the given amount.
    How many whole bills of currency fit into the starting amount? Remember -- you can only receive whole bills, not fractions of bills, 
    so remember to divide accordingly
    """

    return int(amount/denomnation)

def get_leftover_of_bills(amount, denomination):
    """
    function, taking amount and denomination.
    This function should return the leftover amount that cannot be returned from your starting amount given the denomination of bills
    """

    return amount - get_value_of_bills(denomination, 5)

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    function, taking budget, exchange_rate, spread, and denomination.
    spread is 10 which means actual rate is 1.32 instead of 1.2 usd == 1 eur

    This function should return the maximum value of the new currency after calculating the exchange rate plus the spread
    """

    rate = exchange_rate + (exchange_rate * (spread/100))
    print(f"rate: {rate:2f}")

    exchange = exchange_money(budget, rate)
    print(f"exchange: {exchange}")

    bills = get_number_of_bills(exchange, denomination)
    print(f"bills: {bills}")

    value = int(get_value_of_bills(bills,denomination))
    print(f"value: {value}")

def main():
    exchangeable_value(127.25, 1.20, 10, 20)
    exchangeable_value(127.25, 1.20, 10, 5)

main()