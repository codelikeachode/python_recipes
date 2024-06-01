from datetime import datetime, timedelta
now = datetime.now()
yesterday = now - timedelta(days=1)

areEqual = now == yesterday
# areEqual is False

areLater = now > yesterday
# areLater is True

areEarlier = now < yesterday
#areEarlier is False

print("now is", now)
print("yesterday is", yesterday)
print(f"{areEqual = }")
print(f"{areLater = }")
print(f"{areEarlier = }")