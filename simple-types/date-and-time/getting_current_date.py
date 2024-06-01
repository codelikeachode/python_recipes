from datetime import datetime, timezone timedelta, UTC
# pip install pytz
import pytz

now = datetime.now()

utcDate = datetime.now(UTC)
# m_date current date in timezone UTC

londonDate
datetime.now(timezone(timedelta(hours=1)))
# m_date current date in timezone UTC +1:00

pacificDate
datetime.now(pytz.timezone("Pacific/Wake"))
# m_date current date in timezone Pacific/Wake UTC +12:00

print(f"{now = }")
print(f"{utcDate = }")
print(f"{londonDate = }")
print(f"{pacificDate = }")