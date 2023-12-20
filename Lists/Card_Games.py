"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    # Next values after the given number
    next_one = number + 1
    another_one = number + 2
    # Making a list of the number and its next values
    each_list = [number, next_one, another_one]

    return each_list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    # Concatenating the two lists
    combined_list = rounds_1 + rounds_2

    return combined_list


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    # Checking if the value exists in the list
    if number in rounds:
        return True

    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    # Finding the sum and the length of the elements in the list
    sum_of_all_cards = sum(hand)
    length_of_list = len(hand)
    # Calculating the average of the elements in the list
    avg_of_hand = sum_of_all_cards / length_of_list

    return avg_of_hand


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    # Calling the average() to find the true average
    calculated_avg = card_average(hand)

    # Calculating the median
    middle_index = int((len(hand) - 1) / 2)
    median = hand[middle_index]
    # Calculating the average using first & last values
    new_avg = (hand[0] + hand[-1]) / 2
    # Checked if the alternate average equal the true average
    if calculated_avg in (new_avg, median):
        return True

    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    # Calculating the average of even- and odd-indexed values
    even_index_val_avg = card_average(hand[::2])
    odd_index_val_avg = card_average(hand[1::2])
    # Checking if the even- and odd-indexed averages
    if even_index_val_avg == odd_index_val_avg:
        return True

    return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    # Finding out the last value in the list
    last_value = hand[-1]
    # Checking if the last value in the list is -11
    if last_value == 11:
        hand[-1] = last_value * 2

    return hand
