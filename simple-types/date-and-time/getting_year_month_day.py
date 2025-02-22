from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
dayOfWeek = now.isoweekday()

print("now is", now)
print(f"{year = }")
print(f"{month = }")
print(f"{day = }")
print(f"{hour = }")
print(f"{minute = }")
print(f"{second = }")
print(f"{dayOfWeek = }")
