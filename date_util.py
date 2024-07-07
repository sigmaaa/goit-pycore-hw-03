"""Python Datetime module supplies classes to work with date and time"""
from datetime import datetime


def validate_iso_format(date_text):
    """
    Validate that the date_text is in ISO format YYYY-MM-DD.

    :param date_text: Date string to validate.
    :raises ValueError: If date_text is not in the correct format.
    """
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError(
            "Incorrect data format, should be YYYY-MM-DD") from exc


def get_days_from_today(date_text):
    """
    Return the number of days between the current date and the date_text.

    :param date_text: Date string in ISO format YYYY-MM-DD.
    :return: Number of days between today and the date_text.
    """
    validate_iso_format(date_text)
    return (datetime.today() - datetime.fromisoformat(date_text)).days

print(get_days_from_today("2024-01-22"))