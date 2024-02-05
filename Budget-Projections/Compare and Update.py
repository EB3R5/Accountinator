import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json
from tkinter import messagebox

# Dynamically construct the path to the JSON file
user_home_dir = os.path.expanduser('~')
json_file_path = os.path.join(user_home_dir, 'Github', 'Accountinator', 'csv', 'Test of Budget and Projections Foundation_Transaction Ontology2.json')

# Dynamically construct the path to the Google Sheets credentials file
credentials_file_path = os.path.join(user_home_dir, 'Github', 'Accountinator', 'accountinator1.json')

# Authenticate with Google Sheets
def authenticate_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file_path, scope)
    return gspread.authorize(creds)

# Load JSON data
def load_json_data(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "JSON file not found.")
        return None
    except json.JSONDecodeError as e:
        messagebox.showerror("Error", f"Invalid JSON format: {e}")
        return None

# Compare categories and update Google Sheet
def update_google_sheet_with_new_categories(google_sheet, worksheet_name, json_categories):
    gc = authenticate_google_sheets()
    sh = gc.open(google_sheet)
    worksheet = sh.worksheet(worksheet_name)

    existing_categories = worksheet.col_values(1)  # Assuming categories are in column A

    json_data = load_json_data(json_file_path)
    if json_data is None:
        return

    df = pd.DataFrame(json_data)
    json_categories_list = df['Category'].unique().tolist()

    additional_categories = [cat for cat in json_categories_list if cat not in existing_categories]

    if additional_categories:
        next_row = len(existing_categories) + 1
        for category in additional_categories:
            worksheet.update_cell(next_row, 1, category)
            next_row += 1
        messagebox.showinfo("Success", "Google Sheet updated with new categories.")

# Example usage
if __name__ == "__main__":
    google_sheet = 'Test of Budget and Projections Foundation'  # Your Google Sheet name
    worksheet_name = 'Transaction Ontology'  # Your worksheet name
    update_google_sheet_with_new_categories(google_sheet, worksheet_name, json_file_path)
