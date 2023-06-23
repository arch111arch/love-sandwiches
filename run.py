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

    print("Please enter sales data from the last market.")
    print("Data should be 6 sumbers, separated by commas.")
    print("Example: 11,22,33,44,55,66\n")
    data_str = input("Enter you data here: \n")
    data_str = data_str
    #print(f"The data you provided is : {data_str}")
    
    sales_data = data_str.split(",")

    validate_data(sales_data)

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
        get_sales_data()


    print(values)

get_sales_data()
