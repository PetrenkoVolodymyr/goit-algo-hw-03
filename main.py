# TASK 1

import datetime as dt
from datetime import datetime as dtdt

def get_days_from_today(date):
    today = dtdt.today()
    try:
        date_transformed = dtdt.strptime(date, '%Y-%m-%d')
    except ValueError:
        return("Введено некоректну дату")
    else:
        diff = today - date_transformed
        return(diff.days)


print(get_days_from_today("2021-10-09"))

# # TASK 2

# import random

# def get_numbers_ticket(min, max, quantity):
#     if type(min) == int and type(max) == int and type(quantity) == int and min>0 and max<=1000 and quantity<=max-min+1:
#         list=[]
#         while len(list) < quantity:
#             num = random.randint(min, max)
#             if num in list:
#                 continue
#             else:
#                 list.append(num)
#         return(sorted(list))
#     else:
#         return('Введено некоректні дані')

# print(get_numbers_ticket(1,49,6))

# # TASK 3

# import re
# def normalize_phone(phone_number):
#     sanitized_numbers=[]
#     for item in phone_number:    
#         pattern = r"[+0-9]"
#         phone_list = re.findall(pattern, item)
#         if len(phone_list) == 10:
#             phone_list = [*["+","3","8"], *phone_list]
#         if phone_list[0] != "+":
#             phone_list = ["+", *phone_list]
#         phone = ""    
#         for x in phone_list: 
#             phone += x  
#         sanitized_numbers.append(phone)
#     return("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# raw_numbers = [   "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   "]

# print(normalize_phone(raw_numbers))


# # TASK 4

# import datetime
# from datetime import datetime, timedelta

# def get_upcoming_birthdays(users):
#     upcoming_birthdays=[]
#     for user in users:
#         birthday_date_str = user["birthday"].replace(user["birthday"][:4], '2024', 1)
#         birthday_date_date = datetime.strptime(birthday_date_str, "%Y.%m.%d").date()

#         today = datetime.today().date()
#         diff_days = birthday_date_date-today

#         if diff_days <= timedelta(days=6) and diff_days>= timedelta(days=0):
#             if birthday_date_date.weekday() == 5:
#                 birthday_date_date = birthday_date_date + timedelta(days=2)
#             if birthday_date_date.weekday() == 6:
#                 birthday_date_date = birthday_date_date + timedelta(days=1)

#             birthday_date_str = birthday_date_date.strftime("%Y-%m-%d")

#             to_congratulate = {"name": user["name"], "congratulation_date": birthday_date_str}
#             upcoming_birthdays.append(to_congratulate.copy())

#     return(upcoming_birthdays)

# users = [
#     {"name": "John Doe", "birthday": "1985.01.25"}, 
#     {"name": "John Doe", "birthday": "1985.01.27"},
#     {"name": "John QQQ", "birthday": "1985.02.27"},
#     {"name": "John TTT", "birthday": "1985.01.02"}
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)
