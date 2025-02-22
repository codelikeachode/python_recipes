from datetime import datetime

victoryDate = datetime(year=1945, month=5, day=9, hour=1)
now = datetime.now()
delta = now - victoryDate

days = delta.days
minutes = delta.total_seconds() / 60
seconds = delta.total_seconds()

print("victoryDate is", victoryDate)
print("now is", now)
print(f"{days = }")
print(f"{minutes = }")
print(f"{seconds = }")
