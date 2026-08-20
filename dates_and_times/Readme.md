# Python Dates & Times

```python
from datetime import datetime, date, time, timedelta
```

# Get the current date and time

```python
from datetime import datetime, date

print(datetime.now())
print(date.today())
```

Example output:

```text
2026-08-21 11:25:43.123456
2026-08-21
```

### Current UTC time

```python
from datetime import datetime, timezone

print(datetime.now(timezone.utc))
```

## Create a specific date

```python
from datetime import date

d = date(2026, 8, 21)

print(d)
print(d.year)
print(d.month)
print(d.day)
```

Output:

```text
2026-08-21
2026
8
21
```

You can also get the weekday:

```python
print(d.weekday())
```

`weekday()` returns:

```text
Monday    = 0
Tuesday   = 1
...
Sunday    = 6
```

## Create a specific time

```python
from datetime import time

t = time(14, 30, 45)

print(t)
print(t.hour)
print(t.minute)
print(t.second)
```

Output:

```text
14:30:45
14
30
45
```

## Create a date + time

```python
from datetime import datetime

dt = datetime(2026, 8, 21, 14, 30, 45)

print(dt)
```

Output:

```text
2026-08-21 14:30:45
```

# Formatting dates - `strftime()`

This is extremely important.

```python
from datetime import datetime

dt = datetime.now()

print(dt.strftime("%d-%m-%Y"))
print(dt.strftime("%Y/%m/%d"))
print(dt.strftime("%d %B %Y"))
print(dt.strftime("%A, %d %B %Y"))
```

Example:

```text
21-08-2026
2026/08/21
21 August 2026
Friday, 21 August 2026
```

### Common format codes

| Code | Meaning      | Example  |
| ---- | ------------ | -------- |
| `%Y` | 4-digit year | `2026`   |
| `%y` | 2-digit year | `26`     |
| `%m` | Month        | `08`     |
| `%d` | Day          | `21`     |
| `%H` | Hour (24h)   | `14`     |
| `%M` | Minute       | `30`     |
| `%S` | Second       | `45`     |
| `%A` | Full weekday | `Friday` |
| `%B` | Full month   | `August` |

# Convert a string to datetime - `strptime()`

Very common when processing input from files or user.

```python
from datetime import datetime

text = "21-08-2026"

dt = datetime.strptime(text, "%d-%m-%Y")

print(dt)
```

Output:

```text
2026-08-21 00:00:00
```

Another example:

```python
text = "21/08/2026 14:30"

dt = datetime.strptime(text, "%d/%m/%Y %H:%M")

print(dt)
```

# Date arithmetic — `timedelta`

Add or subtract days.

```python
from datetime import date, timedelta

today = date.today()

tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print(today)
print(tomorrow)
print(yesterday)
```

### Add weeks

```python
future = today + timedelta(weeks=2)

print(future)
```

### Add hours/minutes

```python
from datetime import datetime, timedelta

now = datetime.now()

print(now + timedelta(hours=5))
print(now + timedelta(minutes=30))
```

# Difference between two dates

```python
from datetime import date

start = date(2026, 8, 1)
end = date(2026, 8, 21)

difference = end - start

print(difference)
print(difference.days)
```

Output:

```text
20 days, 0:00:00
20
```

### Practical example

```python
from datetime import datetime

login = datetime(2026, 8, 21, 9, 0)
logout = datetime(2026, 8, 21, 17, 30)

duration = logout - login

print(duration)
```

Output:

```text
8:30:00
```

# Comparing dates

Dates can be compared directly.

```python
from datetime import date

today = date.today()
deadline = date(2026, 12, 31)

if today < deadline:
    print("Deadline is still ahead")
else:
    print("Deadline has passed")
```

You can also use:

```python
date1 == date2
date1 < date2
date1 > date2
```

# Unix timestamp

A timestamp represents time as seconds from the Unix epoch.

```python
from datetime import datetime

dt = datetime.now()

timestamp = dt.timestamp()

print(timestamp)
```

Convert it back:

```python
dt2 = datetime.fromtimestamp(timestamp)

print(dt2)
```

# Time Zones

For modern applications, prefer **timezone-aware** datetimes.

```python
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)

print(now_utc)
```

For example, converting UTC to India time:

```python
from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime.now(ZoneInfo("UTC"))

india_time = utc_time.astimezone(
    ZoneInfo("Asia/Kolkata")
)

print(utc_time)
print(india_time)
```

`zoneinfo` is built into modern Python, so you don't need an external package.
