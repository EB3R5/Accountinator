import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\chris\\Github\\Accountinator\\service.json', scope)

# Authorize the client sheet
gc = gspread.authorize(creds)

# Open a sheet from a spreadsheet in one go
sh = gc.open('Account Activity Foundation')

# Select the worksheet by its title
worksheet = sh.worksheet('Balance History')

# Data structure for multiple rows with unique values for each row
rows_data = [
    ["2023-01-01", "10:00", "Savings", "12345", "001", "Bank A", "1000.00", "January", "1", "1", "Deposit", "Asset", "2023-01-01"],
    ["2023-01-02", "11:00", "Checking", "54321", "002", "Bank B", "500.00", "January", "1", "2", "Withdrawal", "Asset", "2023-01-02"],
    # Add more rows as needed, each with unique values
    # ...
    # Example for the 10th row
    ["2023-01-10", "14:00", "Investment", "98765", "010", "Bank C", "1500.00", "January", "2", "10", "Interest", "Asset", "2023-01-10"]
]

# Ensure you fill in all rows up to the 10th with your specific data
# This example shows only 3 rows fully defined for brevity

# Insert the data starting from the second row
worksheet.insert_rows(rows_data, index=2)

print(f"Successfully inserted {len(rows_data)} rows into the 'Balance History' worksheet in the spreadsheet: {sh.title}")
