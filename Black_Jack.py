"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    # Checking the value of the card entered
    if card in ('J', 'Q', 'K'): # --> If the card is a face card
        # Returning the value of the face card
        return 10 
    if card == 'A': # --> If the card is an ace
        # Returning the value of the ace card
        return 1
    # If the card is any numerical value from 2 to 10,
    # returning the value entered itself as an integer
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    # Storing the value of the cards by running them through "value_of_card()"
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    # Comparing the value of the two cards
    if card_one_value > card_two_value:
        # Returning the higher value of the two cards
        return card_one
    if card_one_value < card_two_value:
        # Returning the higher value of the two cards
        return card_two
    # Returning both cards if the values are the same as a default
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # Storing the possible ace values
    low_ace_value = 1
    high_ace_value = 11
    # Checking if the card one in hand is an Ace, face, or number card
    if card_one == 'A':
        value_card_one = high_ace_value
    else:
        # Running the card_one through the value_of_card() 
        value_card_one = value_of_card(card_one)
    # Checking if the card two in hand is an Ace, face, or number card
    if card_two == 'A':
        value_card_two = high_ace_value
    else:
        # Running the card_two through the value_of_card()  
        value_card_two = value_of_card(card_two)
    # Storing total value sum of two cards with ace
    total_sum = value_card_one + value_card_two + high_ace_value
    # Checking whether 'total_sum' is less than or equal to 21
    if total_sum <= 21:
        # Returning '11' for the value of the upcoming ace card
        return high_ace_value
    # Returning the default '1' for the value of the upcoming ace card
    return low_ace_value

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # Setting the ace value to '11' if its already in hand
    hand_ace_value = 11
    # Checking if the card one in hand is an Ace, face, or number card
    if card_one == 'A':
        card_one_val = hand_ace_value
    else:
        # Running the card_one through the value_of_card() 
        card_one_val = value_of_card(card_one)
    # Checking if the card one in hand is an Ace, face, or number card
    if card_two == 'A':
        card_two_val = hand_ace_value
    else:
        # Running the card_two through the value_of_card() 
        card_two_val = value_of_card(card_two)

    # Checking if the two cards in hand are 'A'(value of 11) and a face card or vice versa
    if card_one_val == 11 and card_two_val == 10 or card_one_val == 10 and card_two_val == 11:
        return True
    # Returning if the cards one and two are not of values of '11' and '10'
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    # Storing the values of the two cards
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    # Comparing the identity or the value of the two cards
    if card_one == 'Q' and card_two == 'K' or card_one == 'K' and card_two == 'Q': 
        # Return 'True' if the first two cards are 'Q' and 'K' or vice versa
        return True
    if value_card_one is value_card_two:
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    # Storing the values of the two cards
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    # Sum of the values of the two cards
    sum_value_cards = value_card_one + value_card_two
    # Checking whether the sum of two cards is 9, 10, or 11
    if sum_value_cards in (9, 10, 11):
        # Returning True if the condition is met
        return True
    # Returning the default response
    return False
