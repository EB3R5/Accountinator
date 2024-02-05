import tkinter as tk
from tkinter import simpledialog
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Function to get user input for spreadsheet title and sheet name
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    spreadsheet_title = simpledialog.askstring("Input", "What is the title of the spreadsheet?")
    worksheet_name = simpledialog.askstring("Input", "What is the name of the sheet?")
    
    return spreadsheet_title, worksheet_name

# Setup
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credentials_path = 'C:\\Users\\chris\\Github\\Accountinator\\accountinator1.json'

# Ask user for spreadsheet title and worksheet name
spreadsheet_title, worksheet_name = get_user_input()

# Generate dynamic file paths based on user input
csv_file_path = f'C:\\Users\\chris\\Github\\Accountinator\\csv\\{spreadsheet_title}_{worksheet_name}.csv'
json_file_path = f'C:\\Users\\chris\\Github\\Accountinator\\csv\\{spreadsheet_title}_{worksheet_name}.json'

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
