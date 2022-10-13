def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_to_return = 0
    if card == 'J' or card == 'Q' or card == 'K':
        value_to_return += 10
    elif card == 'A':
        value_to_return += 1
    else:
        value_to_return += int(card)

    return value_to_return

print(value_of_card('Q'))