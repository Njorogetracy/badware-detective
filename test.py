import gspread
from google.oauth2.service_account import Credentials
# import json
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('badware_detective')

indicators = SHEET.worksheet('indicators')
datasheet_Values = indicators.get_all_records()
# pprint(datasheet_Values)

result = [sub['Indicator Value'] for sub in datasheet_Values]
# pprint(str(result))

data = input("Enter value\n")

for x in range(len(result)):
    if data == result[x]:
        pprint(f'Match found at position {x+1}')
for dictionary in datasheet_Values:
    for key, value in dictionary.items():
        # print(key, value)
        if value == data:
            final_result = str(dictionary)
            break

final_result = final_result.replace("{", "")
final_result = final_result.replace("}", "")
final_result = final_result.replace(", ", "\n")
final_result = final_result.replace("'", "")
final_result = final_result.replace("[dropped by decoy app]", "")

print(final_result)

