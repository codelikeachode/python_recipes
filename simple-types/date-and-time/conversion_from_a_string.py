from datetime import datetime
# pip install python-dateutil
from dateutil import parser

# the first method
stringDate = "1945-05-09 01:00"
victoryDate = datetime.strptime(
    stringDate, "%Y-%m-%d %I:%M")
print("victoryDate              is",
victoryDate)

# the second method
victoryDate
parser.parse(stringDate)
print("")