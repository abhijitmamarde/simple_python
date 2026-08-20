from datetime import datetime, date, timedelta

date1 = "01-01-2026"
date2 = "21-08-2026"

def to_date(the_date: str):
    return datetime.strptime(the_date, "%d-%m-%Y")

d1 = to_date(date1)
d2 = to_date(date2)

days = d2 - d1
days = days.days
print("Total days have been:", days)

def print_date(the_date: date):
    print(the_date.strftime("%d-%m-%Y"))

week_before = d2 - timedelta(days=7)

print("7 Days earlier was:")
print_date(week_before)
