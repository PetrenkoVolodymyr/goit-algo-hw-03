import datetime
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays=[]
    for user in users:
        birthday_date_str = user["birthday"].replace(user["birthday"][:4], '2024', 1)
        birthday_date_date = datetime.strptime(birthday_date_str, "%Y.%m.%d").date()

        today = datetime.today().date()
        diff_days = birthday_date_date-today

        if diff_days <= timedelta(days=6) and diff_days>= timedelta(days=0):
            if birthday_date_date.weekday() == 5:
                birthday_date_date = birthday_date_date + timedelta(days=2)
            if birthday_date_date.weekday() == 6:
                birthday_date_date = birthday_date_date + timedelta(days=1)

            birthday_date_str = birthday_date_date.strftime("%Y-%m-%d")

            to_congratulate = {"name": user["name"], "congratulation_date": birthday_date_str}
            upcoming_birthdays.append(to_congratulate.copy())

    return(upcoming_birthdays)

users = [
    {"name": "John Doe", "birthday": "1985.01.25"}, 
    {"name": "John Doe", "birthday": "1985.01.27"},
    {"name": "John QQQ", "birthday": "1985.02.27"},
    {"name": "John TTT", "birthday": "1985.01.02"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
