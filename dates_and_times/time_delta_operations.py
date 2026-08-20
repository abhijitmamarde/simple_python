from datetime import date, timedelta

today = date.today()

tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

def print_date(message, the_date: date):
    print(message, the_date.strftime("%d-%m-%Y"))

print_date("Today is:", today)
print_date("Tomorrow will be:", tomorrow)
print_date("Yesterday was:", yesterday)