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

    while True:
        print()
        print()

        data_provided = input("Enter your indicator here:\n")

        if check_is_indicator_valid(data_provided):
            break

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
        print("Invalid data: please try again")
        return False


def is_indicator_in_database(data_provided):
    """
    This function checks if the indicator inputted
    is present in the database and returns the information,
    of the indicator type and value from the database
    """

    result = [sub['Indicator Value'] for sub in datasheet_Values]
    for val in range(len(result)):
        if data_provided == result[val]:
            print(f'Match found at position {val+1}')
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


# def add_indicator(data_provided):
#     """
#     This function adds the new indicators,
#     from the user to the database
#     """
#     datasheet_Values.append_row(data_provided)
#     print("Database updated")


def search_indicator():
    """
    This function runs the first program
    option, to query the database for the
    indicator
    """
    loaded_indicator = get_indicator()
    check_is_indicator_valid(loaded_indicator)
    is_indicator_in_database(loaded_indicator)


def error_handler():
    """
    This function returns the error,
    if the user inputs invalid option
    """
    print("Invalid Choice")


def welcome():
    """"
    This function starts the program
    """
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


def goodbye():
    """
    This function exits the program
    """
    print("Thank you for using the program. Goodbye")


def start_program():
    """"
    This function starts the program
    """
    choice = int(input("""Choose from the options below:
    1. Search database for indicator
    2. Add new indicator to database
    0. Exit program\n
    """))
    while choice != 0:
        if choice == 1:
            search_indicator()
        elif choice == 2:
            print("option 2 selected")
        elif choice == 0:
            goodbye()
            break
        else:
            error_handler()

        choice = int(input("""Choose from the options below:
        1. Search database for indicator
        2. Add new indicator to database
        0. Exit program\n
        """))


if __name__ == "__main__":
    welcome()
    start_program()
                                                                                                                       
