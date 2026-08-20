from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime.now(ZoneInfo("UTC"))

india_time = utc_time.astimezone(
    ZoneInfo("Asia/Kolkata")
)

def get_str_time(the_time: datetime):
    return the_time.strftime("%d-%m-%Y %H:%M:%S")

print("UTC Time:", get_str_time(utc_time))
print("IST Time:", get_str_time(india_time))
