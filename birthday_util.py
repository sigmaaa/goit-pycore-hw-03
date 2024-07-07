"""The module that helps determine when to wish people a happy birthday"""
from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    Determine upcoming birthdays within the next 7 days for a list of users.

    :param users: List of dictionaries containing user information including name and birthday.
    :return: Dictionary mapping user names to their upcoming birthdays formatted as "%Y.%m.%d".
    """
    upcoming_birthdays = []
    current_date = datetime.today().date()

    for user in users:
        user_birthday = datetime.strptime(
            user["birthday"], "%Y.%m.%d").date().replace(year=current_date.year)

        # Check if the birthday is within the next 7 days and not in the past
        if current_date < user_birthday <= current_date + timedelta(days=7):
            # Adjust on Monday if birthday falls on a weekend (Saturday or Sunday)
            if user_birthday.weekday() >= 5:
                user_birthday += timedelta(7-user_birthday.weekday())

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date:": user_birthday.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays
