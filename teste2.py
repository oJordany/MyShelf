from datetime import date
import re

todaysDate = str(date.today())
print(todaysDate)
dateSeparated = list()
for match in re.finditer(r'\d{2,4}', todaysDate):
    dateSeparated.append(int(match.group()))

print(str(date.today()))