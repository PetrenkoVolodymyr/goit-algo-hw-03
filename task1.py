import datetime
from datetime import datetime

def get_days_from_today(date):
    today = datetime.today()
    try:
        date_transformed = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return("Введено некоректну дату")
    else:
        diff = today - date_transformed
        return(diff.days)


print(get_days_from_today("2021-10-09"))