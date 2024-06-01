from datetime import datetime

now = datetime.now()
shortStyle = now.strftime("%m/%d/%y%H:%M %p")
# shortStyle is "06/05/24 11:45 AM"

customStyle = now.strftime("%Y-%m-%d")
# customStyle is "2022-06-05"

standardStyle = str(now)
# customStyle is "2022-06-05 11:45:00.898000"

strFormat = "Today {0:%d} {0:%B}"\
    .format(now, "day", "month")
# m_string is Today 05 May

print(f"{shortStyle = }")
print(f"{customStyle = }")
print(f"{standardStyle = }")
print(f"{strFormat = }")