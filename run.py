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
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():

    """
    Get sales figures inout from the user
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be 6 sumbers, separated by commas.")
        print("Example: 11,22,33,44,55,66\n")
        data_str = input("Enter you data here: \n")
        
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break
    return(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises Valueerror if strings cannot be converted into int,
    or if there aren´t exactly 6 values.
    """
    try:
        [int(x) for x in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required. You provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        print('')
        return False

    return True

    print(values)

def update_sales_worksheet(data):
    """
    Update the sales worksheet, add a new row with the list provided from the user input.
    """
    print("Updating sales worksheet ... \n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock to calculate the surplus for each item type.

    + Posititve suprlus indicates waste, thrown away at the end of the day.
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data ... \n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[len(stock)-1]
    sales = SHEET.worksheet("sales").get_all_values()
    sales_row = sales[len(sales)-1]
    
    print(stock_row)



print("Welcome to the Love Sandwiches Data Automation")
def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(x) for x in data]
    print(sales_data)
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)


main()