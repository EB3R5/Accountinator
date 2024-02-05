import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Function to insert data from JSON into Google Sheet
def insert_data_from_json(json_file_path):
    # Define the scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

    # Add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/service-account-file.json', scope)

    # Authorize the client sheet
    gc = gspread.authorize(creds)

    # Open the spreadsheet and select the worksheet
    sh = gc.open('Your Spreadsheet Name Here')
    worksheet = sh.worksheet('Your Worksheet Name Here')
    
    # Read data from JSON file
    with open(json_file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
        
        for row in data:
            # Extract values in the order of columns in your Google Sheet
            row_values = [
                row.get("Date", ""),
                row.get("Time", ""),
                row.get("Account", ""),
                row.get("Account #", ""),
                row.get("Account ID", ""),
                row.get("Institution", ""),
                str(row.get("Balance", "")),  # Convert numerical values to string
                row.get("Month", ""),
                row.get("Week", ""),
                row.get("Index", ""),
                row.get("Type", ""),
                row.get("Class", ""),
                row.get("Updated", ""),
                row.get("Updated Date", ""),
                row.get("Updated Time", "")
            ]
            # Insert the row data
            worksheet.append_row(row_values)  # Use append_row for adding to the end of the sheet
            print("Data inserted successfully for row:", row_values)

# Path to your JSON file
json_file_path = 'path/to/your/data.json'

# Call the function to insert data from JSON
insert_data_from_json(json_file_path)
