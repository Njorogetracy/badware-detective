import re
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
datasheet_Values = indicators.get_all_values()
# pprint(datasheet_Values)


def get_indicator():
    """
    Get the indicator from the user,
    Indicators to be provided should be domain name,
    IP address or File Hash
    """

    data_provided = input("Enter your indicator here:\n")
    return data_provided


def check_is_indicator_valid(data_provided):
    """
    This function checks if the indicator
    inputed has the valid syntax
    """

    hash_pattern = r"^[a-fA-F0-9]{32}$"
    ip_pattern = (
        r"^(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)"
        r"(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$"
    )
    # exception="^(0\.0\.0\.0)|(255\.255\.255\.255)$"
    dm_pattern = (
        r'^[a-zA-Z0-9]'
        r'([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?'
        r'(\.[a-zA-Z0-9]([a-zA-Z0-9\-]){0,61}'
        r'[a-zA-Z0-9])*'
        r'(\.[a-zA-Z]{2,6}){1}$'
    )
    try:
        if (
            re.match(hash_pattern, data_provided)
                or re.match(ip_pattern, str(data_provided))
                or re.match(dm_pattern, str(data_provided))
        ):
            return True
    except ValueError:
        return False
    while True:
        if check_is_indicator_valid(loaded_indicator):
            break
        else:
            print("Invalid Input")


def is_indicator_in_database(data_provided):
    """
    This function checks if the indicator inputted
    is present in the database and returns the information,
    of the indicator type and value from the database
    """
    data = SHEET.worksheet("indicators")
    search_for_indicator = data.get_all_records()
    # pprint(search_for_indicator[1][1])
    # pprint(search_for_indicator)
    for x in range(len(search_for_indicator)):
        if x == data_provided:
            pprint(x)
            break
        else:
            print("not found")
    # if data_provided in search_for_indicator:
    #     print("Indicator is present")
    #     # indicator_present = data.cell(search_for_indicator)
    #     # index(data_provided) + 1, 2).value
    #     # print(indicator_present)
    # else:
    #     print("Indicator not present in database")


loaded_indicator = get_indicator()
valid_indicator = check_is_indicator_valid(loaded_indicator)
is_indicator_in_database(valid_indicator)
