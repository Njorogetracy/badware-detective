# # import re
# # import gspread
# # from google.oauth2.service_account import Credentials
# # from pprint import pprint

# # SCOPE = [
# #     "https://www.googleapis.com/auth/spreadsheets",
# #     "https://www.googleapis.com/auth/drive.file",
# #     "https://www.googleapis.com/auth/drive"
# #     ]

# # CREDS = Credentials.from_service_account_file('creds.json')
# # SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# # GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# # SHEET = GSPREAD_CLIENT.open('badware_detective')

# # # indicators = SHEET.worksheet('indicators')
# # # datasheet_Values = indicators.get_all_values()
# # # datasheet_values = indicators.col_values(1)
# # # datasheet_values.append(["test.com", "domain", "N/A"])
# # # pprint(datasheet_values)


# # def get_indicator():
# #     """
# #     Get the indicator from the user,
# #     Indicators to be provided should be domain name,
# #     IP address or File Hash
# #     """
# #     while True:
# #         print()
# #         print()

# #         data_provided = input("Enter your indicator here:\n")

# #         if check_is_indicator_valid(data_provided):
# #             break

# #     return data_provided


# # def check_is_indicator_valid(data_provided):
# #     """
# #     This function checks if the indicator
# #     inputed has the valid syntax
# #     """

# #     hash_pattern = r"^[a-fA-F0-9]{32}$"
# #     ip_pattern = (
# #         r"^(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)"
# #         r"(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$"
# #     )
# #     dm_pattern = (
# #         r'^[a-zA-Z0-9]'
# #         r'([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?'
# #         r'(\.[a-zA-Z0-9]([a-zA-Z0-9\-]){0,61}'
# #         r'[a-zA-Z0-9])*'
# #         r'(\.[a-zA-Z]{2,6}){1}$'
# #     )
# #     try:
# #         if (
# #             re.match(hash_pattern, str(data_provided))
# #                 or re.match(ip_pattern, str(data_provided))
# #                 or re.match(dm_pattern, str(data_provided))
# #         ):
# #             return True
# #     except ValueError:
# #         print("Invalid data: please try again")
# #         return False


# # def add_indicator(data):
# #     """
# #     This function adds the new indicators,
# #     from the usser
# #     """
# #     print("Updating database....")
# #     check_is_indicator_valid(data)
# #     datasheet_values = SHEET.worksheet("indicators")
# #     datasheet_values.append_row(data)
# #     print("Database updated")

# # # def add_indicator(data):
# # #     """
# # #     This function adds the new indicators,
# # #     from the user to the database
# # #     """
# # #     check_is_indicator_valid(data)
# # #     datasheet_values = SHEET.worksheet("indicators")
# # #     # datasheet_values.append(data)

# # #     # datasheet_values = datasheet_values.get_all_values()
# # #     # datasheet_Values.append([data, "Domain", "N/A"])
# # #     # pprint(datasheet_values)
# # #     # indicator_row_update = indicator.col_values(1)
# # #     # datasheet_Values.append(data)
# # #     # pprint(datasheet_Values)

# # #     print("database updating...")

# # #     option = int(input("""
# # #     Choose one of the following options
# # #     1. Add Domain name
# # #     2. Add File Hash
# # #     3. Add IP Address
# # #     0. Exit function
# # #     """))

# # #     while option != 0:
# # #         if option == 1:
# # #             datasheet_values.append_row(data)
# # #             print("Domain name added")
# # #             break
# # #         elif option == 2:
# # #             print("File hash added")
# # #         elif option == 3:
# # #             # datasheet_values.append_row(data)
# # #             # pprint(datasheet_values)
# # #             print("IP Address added")
# # #             break
# # #         else:
# # #             print("Invalid")
# # #             break

# # #         print(option)


# # answer = get_indicator()
# # print(answer)
# # new_data = list(answer)
# # add_indicator(new_data)

# import gspread
# from google.oauth2.service_account import Credentials
# import re

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('badware_detective')

# indicators = SHEET.worksheet('indicators')
# datasheet_Values = indicators.get_all_values()


# def get_indicator():
#     """
#     Get the indicator from the user,
#     Indicators to be provided should be domain name,
#     IP address or File Hash
#     """

#     while True:
#         print()
#         print()

#         data_provided = input("Enter your indicator here:\n")

#         if check_is_indicator_valid(data_provided):
#             break

#     return data_provided


# def check_is_indicator_valid(data_provided):
#     """
#     This function checks if the indicator
#     inputed has the valid syntax
#     """
#     global hash_pattern
#     global ip_pattern
#     global dm_pattern
#     hash_pattern = r"^[a-fA-F0-9]{32}$"
#     ip_pattern = (
#         r"^(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)"
#         r"(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$"
#     )
#     dm_pattern = (
#         r'^[a-zA-Z0-9]'
#         r'([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?'
#         r'(\.[a-zA-Z0-9]([a-zA-Z0-9\-]){0,61}'
#         r'[a-zA-Z0-9])*'
#         r'(\.[a-zA-Z]{2,6}){1}$'
#     )
#     try:
#         if (
#             re.match(hash_pattern, data_provided)
#                 or re.match(ip_pattern, str(data_provided))
#                 or re.match(dm_pattern, str(data_provided))
#         ):
#             return True
#     except ValueError:
#         print("Invalid data: please try again")
#         return False


# def add_indicator(data_provided):
#     """
#     This function adds, data to the database
#     """
#     test_row = ['', '', '']
#     test_indicator = get_indicator()
#     test_row[0] = test_indicator

#     if re.match(hash_pattern, test_indicator):
#         test_row[1] = "MD5 hash"
#         file_name = input("Enter the file name. If uknown, enter 'N/A': ")
#         test_row[2] = file_name
#         indicators.insert_row(test_row, index=3)
#         print("Row added.")
#     elif re.match(dm_pattern, test_indicator):
#         test_row[1] = "Domain"
#         test_row[2] = "N/A"
#         indicators.insert_row(test_row, index=3)
#         print("Row added.")
#     elif re.match(ip_pattern, test_indicator):
#         test_row[1] = "IP address"
#         test_row[2] = "N/A"
#         indicators.insert_row(test_row, index=3)
#         print("Row added.")
#     else:
#         print("Invalid input.")
#         test_row[0] = ""


# answer = get_indicator()
# check_is_indicator_valid(answer)
# add_indicator(answer)
