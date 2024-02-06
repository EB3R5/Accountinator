import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

def insert_data_from_json(json_file_path):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

    # Dynamically construct the path to the credentials file
    credentials_file_path = os.path.join(os.path.expanduser('~'), 'Github', 'Accountinator', 'accountinator1.json')

    # Add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file_path, scope)

    # Authorize the client sheet
    gc = gspread.authorize(creds)

    # Open the spreadsheet and select the worksheet
    sh = gc.open('Account Activity Foundation')
    worksheet = sh.worksheet('Balance History')
    
    # Read data from JSON file
    with open(json_file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
        
        for row in data:
            row_values = [""] + [
                row.get("Date", ""),
                row.get("Time", ""),
                row.get("Account", ""),
                row.get("Account #", ""),
                row.get("Account ID", ""),
                row.get("Institution", ""),
                str(row.get("Balance", "")),  # Convert numerical values to string if necessary
                row.get("Month", ""),
                row.get("Week", ""),
                row.get("Index", ""),
                row.get("Type", ""),
                row.get("Class", ""),
                row.get("Updated", ""),
                row.get("Updated Date", ""),
                row.get("Updated Time", "")
            ]
            worksheet.append_row(row_values)
            print("Data inserted successfully for row:", row_values)

# Dynamically construct the path to your JSON file
json_file_path = os.path.join(os.path.expanduser('~'), 'Github', 'Accountinator', 'csv', 'accounts_data.json')

# Call the function to insert data from JSON
insert_data_from_json(json_file_path)
