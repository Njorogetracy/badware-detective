import re
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('badware_detective')


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
    if (
        re.match(hash_pattern, data_provided)
            or re.match(ip_pattern, str(data_provided))
            or re.match(dm_pattern, str(data_provided))
    ):
        return True
    else:
        return False

    # try:
    #     if (
    #         re.match(hash_pattern, data_provided)
    #         or re.match(ip_pattern, data_provided)
    #         or re.match(dm_pattern, data_provided)
    #     ):
    #         return True
    # except ValueError:
    #     return False


while True:
    loaded_indicator = get_indicator()
    if check_is_indicator_valid(loaded_indicator):
        break
    else:
        print("Invalid Input")
