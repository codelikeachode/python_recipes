from datetime import datetime, timedelta

# pip install python-dateutil
from dateutil import relativedelta

now = datetime.today()
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)
nextMonth = now + relativedelta.relativedelta(months=1)
nextYear = now.replace(year=now.year + 1)

print("now is", now)
print("yesterday is", yesterday)
print("tomorrow is", tomorrow)
print("nextMonth is", nextMonth)
print("nextYear is", nextYear)
