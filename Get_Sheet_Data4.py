import os
import glob
import tkinter as tk
from tkinter import simpledialog
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Function to generate a unique filename if the file already exists
def generate_unique_filename(base_path, filename, extension):
    # Check if the file exists
    if not os.path.exists(f"{base_path}\\{filename}{extension}"):
        return f"{base_path}\\{filename}{extension}"
    else:
        # Find all files in the directory with the base filename
        existing_files = glob.glob(f"{base_path}\\{filename}*{extension}")
        existing_indices = [int(f.split(filename)[-1].split(extension)[0]) for f in existing_files if f.split(filename)[-1].split(extension)[0].isdigit()]
        
        # Generate a new filename with an appended number
        new_index = 1 if not existing_indices else max(existing_indices) + 1
        return f"{base_path}\\{filename}{new_index}{extension}"

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
base_path = 'C:\\Users\\chris\\Github\\Accountinator\\csv'

# Ask user for spreadsheet title and worksheet name
spreadsheet_title, worksheet_name = get_user_input()

# Generate dynamic, unique file paths based on user input
base_filename = f'{spreadsheet_title}_{worksheet_name}'
csv_file_path = generate_unique_filename(base_path, base_filename, '.csv')
json_file_path = generate_unique_filename(base_path, base_filename, '.json')

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

# Save the DataFrame to JSON with the desired format
json_data = df.to_json(orient='records')

# Wrap the JSON data with [] to create an array
json_array = f"[{json_data}]"

# Save the JSON array to a file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_array)

print(f"Data saved to JSON at {json_file_path}")
