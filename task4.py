import datetime
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays=[]
    for user in users:

        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        today = datetime.today().date()
        curr_birthday = datetime(today.year, birthday.month, birthday.day).date()

        diff = curr_birthday - today

        if diff <= timedelta(days=6) and diff>= timedelta(days=0):
            if curr_birthday.weekday() == 5:
                cong_date = curr_birthday + timedelta(days=2)
            if curr_birthday.weekday() == 6:
                cong_date = curr_birthday + timedelta(days=1)

            cong_date_str = cong_date.strftime("%Y-%m-%d")

            to_congratulate = {"name": user["name"], "congratulation_date": cong_date_str}
            upcoming_birthdays.append(to_congratulate.copy())

    return(upcoming_birthdays)

users = [
    {"name": "John Doe", "birthday": "1985.01.25"}, 
    {"name": "John Doe", "birthday": "1985.01.27"},
    {"name": "John QQQ", "birthday": "1985.02.27"},
    {"name": "John TTT", "birthday": "1985.02.01"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
