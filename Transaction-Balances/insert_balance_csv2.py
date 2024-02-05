import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

# Function to insert data from CSV into Google Sheet
def insert_data_from_csv(csv_file_path):
    # Define the scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

    # Add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\chris\\Github\\Accountinator\\service.json', scope)

    # Authorize the client sheet
    gc = gspread.authorize(creds)

    # Open the spreadsheet and select the worksheet
    sh = gc.open('Account Activity Foundation')
    worksheet = sh.worksheet('Balance History')
    
    # Read data from CSV file
    with open(csv_file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip the header row if present
        for row in csvreader:
            # Modify the row to shift it one column to the right
            modified_row = [""] + row  # Prepend an empty string to shift the data one column to the right
            # Insert the modified row data
            worksheet.insert_row(modified_row, index=2)  # Insert at the second row
            print("Data inserted successfully for row:", modified_row)

# Path to your CSV file
csv_file_path = 'C:\\Users\\chris\\Github\\Accountinator\\csv\\data.csv'

# Call the function to insert data from CSV
insert_data_from_csv(csv_file_path)
