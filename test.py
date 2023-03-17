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

    print("Pick 1 to query database for malicious indicators / 2 to add to database.")  # noqa
    print("The indicator can be a Domain name, IP address(IPV4) or MD5 hash")  # noqa
    print("Example:")
    print("Domain name: test.com, blog.mine.com, myexample.net")
    print("IP address: x.x.x.x where x can be a value between 0 and 255(192.1.2.165)")  # noqa
    print("MD5 hash: a 32 digit hexadecimal value e.g. ec55d3e698d289f2afd663725127bace\n")  # noqa


def get_indicator():
    """
    Get the indicator from the user,
    Indicators to be provided should be domain name,
    IP address or File Hash
    """

    while True:
        data_provided = input("Enter your indicator here:\n")

        if check_is_indicator_valid(data_provided):
            break

    return data_provided


def check_is_indicator_valid(data_provided):
    """
    This function checks if the indicator
    inputed has the valid syntax
    """
    global hash_pattern
    global ip_pattern
    global dm_pattern

    hash_pattern = r"^[a-fA-F0-9]{32}$"
    ip_pattern = (
        r"^(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)"
        r"(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$"
    )
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
    else:
        print("Value not found. Add to database")
        add_indicator(data_provided)

    final_result = None
    for dictionary in datasheet_Values:
        for key, value in dictionary.items():
            if value == data_provided:
                final_result = str(dictionary)
                final_result = final_result.replace("{", "")
                final_result = final_result.replace("}", "")
                final_result = final_result.replace(", ", "\n")
                final_result = final_result.replace("'", "")
                print(final_result)
                goodbye()
        if final_result is not None:
            break
    else:
        print("Value not found. Add to database")
        add_indicator(data_provided)
        print(final_result)


def add_if_not_found():
    """
    Add indicator is not found in database
    """

    while True:
            if re.match(hash_pattern, final_result):
                test_row[1] = "MD5 hash"
                file_name = input("Enter the file name. If uknown, enter 'N/A': ")
                test_row[2] = file_name
                indicators.insert_row(test_row, index=3)
                print("Row added.")
                break
            elif re.match(dm_pattern, test_indicator):
                test_row[1] = "Domain"
                test_row[2] = "N/A"
                indicators.insert_row(test_row, index=3)
                print("Row added.")
                return
            elif re.match(ip_pattern, test_indicator):
                test_row[1] = "IP address"
                test_row[2] = "N/A"
                indicators.insert_row(test_row, index=3)
                print("Row added.")
                return
            else:
                print("Invalid input.")
                test_row[0] = ""


ans = get_indicator()
check_is_indicator_valid(ans)
is_indicator_in_database(ans)