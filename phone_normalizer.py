"""Module that normalize phone numbers to valid format with Ukraine code (+38)"""
import re


def normalize_phone(phone_number):
    """
    Normalize phone numbers of different formats to a standard format 
    with the Ukraine country code (+38).

    For example, +38(050)123-32-34 will be normalized to +380501233234.

    :param phone_number: The phone number to normalize.
    :return: The normalized phone number.
    """

    # will find and replace all non digit chars except '+'
    pattern = r"[^\d+]"
    phone_number = re.sub(pattern, "", phone_number)

    # Ensure the phone number starts with '+38'
    phone_number = (
        phone_number if phone_number.startswith("+")
        else f"+{phone_number}" if phone_number.startswith("380")
        else f"+38{phone_number}"
    )
    return phone_number
