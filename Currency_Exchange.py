"""Required classes for the currency calculator"""
def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    foreign_money_equivalent = float(budget / exchange_rate)
    return foreign_money_equivalent


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    remaining_budget = float(budget - exchanging_value)
    return remaining_budget


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    total_bill_money = int(denomination * number_of_bills)
    return total_bill_money


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    total_bills = int(budget // denomination)
    return total_bills


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    leftover_bills = float(budget % denomination)
    return leftover_bills


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    # Changing the spread integer percentage to a decimal
    decimal_spread = spread / 100
    # Adding the percentage of spread to add the exchange rate
    actual_exchange_rate = exchange_rate + (exchange_rate * decimal_spread)
    # Calculating the exchanged money
    converted_money = exchange_money(budget, actual_exchange_rate)
    converted_bills = int(get_number_of_bills(converted_money, denomination) * denomination)
    return converted_bills