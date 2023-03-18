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

    print(r"Select '1' to query the database for an indicator, "
          r"or '2' to add an indicator to the database.")
    print(r"The indicator can be a domain name,"
          r"IP address (IPV4) or MD5 hash.")
    print("For example:")
    print("Domain name: test.com, blog.mine.com, myexample.net")
    print(r"IP address: x.x.x.x, where x, "
          r"can be a value between 0 and 255 (192.1.2.165)")
    print(r"MD5 hash: a 32 digit hexadecimal value, "
          r"e.g. ec55d3e698d289f2afd663725127bace")
    print(r"Important to note, while adding indicators to the database, "
          r"IP addresses and domain names do not require file names, "
          r"since they are atomic indicators i.e. they are standalone "
          r"MD5 hashes are computed indicators, since their values "
          r"are computed from thier correspoding files, "
          r"therefore require file names.")


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
        else:
            print("Invalid input try again")

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
            print("Match found.")
            break
    else:
        print("Indicator value not found.")

        add_to_database = input("Do you want to add it to the database? (y/n): ")  # noqa
        if add_to_database.lower() == 'y':
            add_indicator(data_provided)
        elif add_to_database.lower() == 'n':
            print("Value not added to database.")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

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


def add_indicator(data_provided):
    """
    This function allows user to
    data to the database
    """
    test_row = ['', '', '']
    test_row[0] = data_provided
    while True:
        if re.match(hash_pattern, data_provided):
            test_row[1] = "MD5 hash"
            file_name = input("Add the file name. If unknown, enter 'N/A':\n")
            test_row[2] = file_name.upper()
            indicators.insert_row(test_row, index=3)
            print("Hash pattern added to database.")
            break
        elif re.match(dm_pattern, data_provided):
            test_row[1] = "Domain"
            test_row[2] = "N/A"
            indicators.insert_row(test_row, index=3)
            print("Domain name added to database.")
            break
        elif re.match(ip_pattern, data_provided):
            test_row[1] = "IP address"
            test_row[2] = "N/A"
            indicators.insert_row(test_row, index=3)
            print("IP address added to database.")
            break
        else:
            print("Invalid input.")
            test_row[0] = ""


def search_indicator():
    """
    This function runs the first program
    option, to query the database for the
    indicator
    """
    loaded_indicator = get_indicator()
    check_is_indicator_valid(loaded_indicator)
    is_indicator_in_database(loaded_indicator)
    goodbye()


def append_indicator():
    """
    This function is the second option,
    after start program nests and runs,
    it allows you to add values,
    to the database
    """
    loaded_indicator = get_indicator()
    check_is_indicator_valid(loaded_indicator)
    add_indicator(loaded_indicator)
    goodbye()


def error_handler():
    """
    This function returns the error,
    if the user inputs invalid option
    """
    print("Invalid Choice")


def goodbye():
    """
    This function exits the program
    """
    print("\nWould you like to exit the program?\n")
    exit_answer = input("Enter Y for Yes or N for No\n")
    while True:
        if exit_answer == "Y" or exit_answer == "y":
            print("Thank you for using the program. Goodbye!")
            print(r"""
                 _____           _ _
                |   __|___ ___ _| | |_ _ _ ___
                |  |  | . | . | . | . | | | -_|
                |_____|___|___|___|___|_  |___|
                                    |___|
            """)
            exit()
        elif exit_answer == "N" or exit_answer == "n":
            start_program()
        else:
            exit_answer = input("Wrong input. Enter 'Y' for Yes or 'N' for No.\n")  # noqa


def start_program():
    """"
    This function starts the program
    """
    while True:
        try:
            choice = int(input("""Choose from the options below:
                1. Search database for indicator
                2. Add new indicator to database
                0. Exit program\n
                """))
            if choice == 1:
                search_indicator()
            elif choice == 2:
                append_indicator()
            elif choice == 0:
                goodbye()
            else:
                error_handler()
        except ValueError:
            print("Invalid input, Please enter valid input")


if __name__ == "__main__":
    welcome()
    start_program()
