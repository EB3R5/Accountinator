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
    if not os.path.exists(os.path.join(base_path, f"{filename}{extension}")):
        return os.path.join(base_path, f"{filename}{extension}")
    else:
        # Find all files in the directory with the base filename
        existing_files = glob.glob(os.path.join(base_path, f"{filename}*{extension}"))
        existing_indices = [int(f.split(os.sep + filename)[-1].split(extension)[0]) for f in existing_files if f.split(os.sep + filename)[-1].split(extension)[0].isdigit()]
        
        # Generate a new filename with an appended number
        new_index = 1 if not existing_indices else max(existing_indices) + 1
        return os.path.join(base_path, f"{filename}{new_index}{extension}")

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

# Dynamically construct the paths
user_home_dir = os.path.expanduser('~')
credentials_path = os.path.join(user_home_dir, 'Github', 'Accountinator', 'accountinator1.json')
base_path = os.path.join(user_home_dir, 'Github', 'Accountinator', 'csv')

# Ensure the credentials file exists
if not os.path.exists(credentials_path):
    print(f"Credentials file not found at {credentials_path}")
    exit(1)

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
# Save the DataFrame to JSON with 'index' orientation
df.to_json(json_file_path, orient='index', indent=4)
print(f"Data saved to JSON in 'index' orientation at {json_file_path}")

