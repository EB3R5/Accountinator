import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Setup
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials_path = 'C:\\Users\\chris\\Github\\Accountinator\\accountinator1.json'
spreadsheet_title = 'Test of Budget and Projections Foundation'
worksheet_name = 'Transaction Ontology'
csv_file_path = 'C:\\Users\\chris\\Github\\Accountinator\\csv\\sheet_data1.csv'
json_file_path = 'C:\\Users\\chris\\Github\\Accountinator\\csv\\sheet_data1.json'

# Authenticate with the Google Sheets and Drive API
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
client = gspread.authorize(creds)

# Open the spreadsheet and select the worksheet
spreadsheet = client.open(spreadsheet_title)
worksheet = spreadsheet.worksheet(worksheet_name)

# Fetch all data from the worksheet
records = worksheet.get_all_records()

# Convert the data to a pandas DataFrame
df = pd.DataFrame(records)

# Save the DataFrame to CSV
df.to_csv(csv_file_path, index=False)
print(f"Data saved to CSV at {csv_file_path}")

# Save the DataFrame to JSON
df.to_json(json_file_path, orient='records', lines=True)
print(f"Data saved to JSON at {json_file_path}")
