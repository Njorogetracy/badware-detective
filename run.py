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

indicators = SHEET.worksheet('indicators')
datasheet_Values = indicators.get_all_records()


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

    result = [sub['Indicator Value'] for sub in datasheet_Values]
    for x in range(len(result)):
        if data_provided == result[x]:
            print(f'Match found at position {x+1}')
            break
    for dictionary in datasheet_Values:
        for key, value in dictionary.items():
            if value == data_provided:
                final_result = str(dictionary)
                break
    final_result = final_result.replace("{", "")
    final_result = final_result.replace("}", "")
    final_result = final_result.replace(", ", "\n")
    final_result = final_result.replace("'", "")
    print(final_result)


def add_indicator(data_provided):
    """
    This function adds the new indicators,
    from the user to the database
    """
    datasheet_Values.append_row(data_provided)
    print("Database updated")


if __name__ == "__main__":
    print(r"""
  _   _   _   _   _   _   _     _   _  
 / \ / \ / \ / \ / \ / \ / \   / \ / \ 
( W | E | L | C | O | M | E ) ( T | O )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ 
  _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ 
( B | A | D | W | A | R | E )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
  _   _   _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( D | E | T | E | C | T | I | V | E )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 

    """)
    option = input("""Choose from the options below:
    1. Search database for indicator
    2. Add new indicator to database
    """)
    while True:
        match option:
            case 1:
                get_indicator()
            case 2:
                get_indicator()
            case default:
                print("Exit 0.")
    # Case statement
    # loaded_indicator = get_indicator()
    # check_is_indicator_valid(loaded_indicator)
    # is_indicator_in_database(loaded_indicator)
    # add_indicator(loaded_indicator)
