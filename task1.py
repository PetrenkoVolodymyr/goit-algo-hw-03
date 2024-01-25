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