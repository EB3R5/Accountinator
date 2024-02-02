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

# Select the first worksheet
worksheet = sh.worksheet('Balance History')

# Data to be inserted, adjust this as per your requirement
data = ["Date", "Description", "Amount", "Category"]

# Insert the data in the second row (index=2, as the index is 1-based)
worksheet.insert_row(data, index=2)

print(f"Successfully inserted data into the spreadsheet: {sh.title}")
