import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

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

# Path to your CSV file
csv_file_path = 'C:\\Users\\chris\\Github\\Accountinator\\balance_history_data.csv'

# Initialize an empty list to hold rows from the CSV
rows_data = []

# Read data from the CSV file
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rows_data.append(row)

# Insert the data starting from the second row
# Note: If your CSV file includes a header row, you might want to skip it or adjust the starting index accordingly
worksheet.insert_rows(rows_data, index=2)

print(f"Successfully inserted {len(rows_data)} rows into the 'Balance History' worksheet in the spreadsheet: {sh.title}")
