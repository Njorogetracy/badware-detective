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

    hash_pattern = r"^[a-fA-F0-9]{32}+$"
    ip_pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    dm_pattern = r"^(?!-)[A-Za-z0-9-]+([\\-\\.]{1}[a-z0-9]+)*\\.[A-Za-z]{2,6}$"
    try:
        if (
            re.match(hash_pattern, data_provided)
            or re.match(ip_pattern, data_provided)
            or re.match(dm_pattern, data_provided)
        ):
            return True
    except ValueError:
        print("Invalid input")

    while True:
        data_provided = get_indicator()
        if check_is_indicator_valid(data_provided):
            break
        else:
            print("Input does not match the pattern try again")


get_indicator()
validity = check_is_indicator_valid
validity(check_is_indicator_valid)
