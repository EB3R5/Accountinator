import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\chris\\Github\\Accountinator\\service.json', scope)  # Replace with the path to your downloaded JSON file

# Authorize the client sheet
gc = gspread.authorize(creds)

# Open a sheet from a spreadsheet in one go
sh = gc.open('Account Activity Foundation')  # Make sure the name matches exactly or use the spreadsheet ID

print(f"Successfully opened the spreadsheet: {sh.title}")
