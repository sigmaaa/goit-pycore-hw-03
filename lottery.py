"""Random ticket generators."""

import random

def get_numbers_ticket(min, max, quantity):
    """
    Returns random numbers in the range from min to max in the selected quantity.
    
    :param min: Minimum value of the range (inclusive).
    :param max: Maximum value of the range (inclusive).
    :param quantity: Number of random values to generate.
    :return: Set of unique random numbers.
    """
    validate_min_number(min)
    validate_max_number(max)
    validate_quantity(min, max, quantity)
    ticket_nums = {}
    ticket_nums = set()
    while len(ticket_nums) < quantity:
        ticket_nums.add(random.randint(min, max))
    return sorted(ticket_nums)


def validate_min_number(min):
    """
    Validates that min number is not less than 1 otherwise raises ValueError.
    
    :param min: Minimum number to validate.
    :raises ValueError: If min is less than 1.
    """
    try:
        if min < 1:
            raise ValueError(f"Passed min number is {
                             min}. The minimum number must not less than 1")
    except ValueError as exc:
        raise exc


def validate_max_number(max):
    """
    Validates that max number is not greater than 1000 otherwise raises ValueError.
    
    :param max: Maximum number to validate.
    :raises ValueError: If max is greater than or equal to 1000.
    """
    try:
        if max >= 1000:
            raise ValueError(f"Passed max number is {
                             max}. The max number must be not greater than 1000")
    except ValueError as exc:
        raise exc


def validate_quantity(min, max, quantity):
    """
    Validates that quantity is between min and max.
    
    :param min: Minimum value of the range.
    :param max: Maximum value of the range.
    :param quantity: Quantity to validate.
    :raises ValueError: If quantity is not within the valid range.
    """
    try:
        if quantity < min or quantity > max:
            raise ValueError(f"the quantity {
                             quantity} isn't in the valid range of values beetwen {min} and {max}")
    except ValueError as exc:
        raise exc


print(get_numbers_ticket(1, 36, 20))
