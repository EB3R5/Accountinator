import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pandas as pd
from datetime import datetime

# Load JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Convert JSON data to a DataFrame
df = pd.DataFrame(data)

# Convert 'Date' to datetime and extract the month name
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')  # 'Jan', 'Feb', etc.

# Authenticate with Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('accountinator1.json', scope)
gc = gspread.authorize(creds)

sh = gc.open('Your Spreadsheet Name')
worksheet = sh.worksheet('Your Worksheet Name')

# Assuming your categories start at row 2 and the months are in columns starting from column 8 (Jan)
categories = worksheet.col_values(1)[1:]  # Skip header row
months_cols = {month: col for col, month in enumerate(worksheet.row_values(1)[7:], start=8)}  # Adjust based on actual structure

for index, row in df.iterrows():
    category = row['Category']
    month = row['Month']
    amount = row['Amount']
    if category in categories:
        cat_row = categories.index(category) + 2  # Adjust for 0-index and header
        month_col = months_cols[month]
        # Get current value (if any) and add the new amount
        current_val = worksheet.cell(cat_row, month_col).value or 0
        new_val = float(current_val) + amount
        worksheet.update_cell(cat_row, month_col, new_val)

print("Sheet updated successfully.")
