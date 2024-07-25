from time import sleep
from datetime import time, timedelta, date, datetime, timezone

# print(time(), type(time()))
# print(date.today(), type(date.today()))
# print(datetime.now(), type(datetime.now()))
# print(datetime(1999, 10, 21))

# now = datetime.now()

# print("year:", now.year)
# print("month:", now.month)
# print("day:", now.day)
# print("hour:", now.hour)
# print("minute:", now.minute)
# print("second:", now.second)
# print("microsecond:", now.microsecond)
# print(now.strftime("%H:%M - %d/%m/%y"))

# print(datetime(now.year, now.month, now.day + 10))
# print(now + timedelta(days=1))

# Exersice: StopWatch:
# base_time = datetime.now()
# try:
#     while True:
#         sleep(1)
#         print(datetime.now() - base_time, end="\r")
# except KeyboardInterrupt:
#     print("\nFinished:", datetime.now() - base_time)

import zoneinfo
utc_timezone = zoneinfo.ZoneInfo("UTC")
tehran_timezone = zoneinfo.ZoneInfo("Asia/Tehran")

print(datetime.now(tz=tehran_timezone))

