import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

# Authenticate with Google Sheets
def authenticate_google_sheets(credentials_file_path):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file_path, scope)
    return gspread.authorize(creds)


def update_google_sheet_with_new_categories(google_sheet, worksheet_name, json_file_path, credentials_file_path):
    gc = authenticate_google_sheets(credentials_file_path)
    sh = gc.open(google_sheet)
    worksheet = sh.worksheet(worksheet_name)
    
    # Convert sheet data to DataFrame
    sheet_data = worksheet.get_all_records()
    sheet_df = pd.DataFrame(sheet_data)
    
    # Load JSON data
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    json_df = pd.DataFrame(json_data)
    
    # Explicitly replace NaN values with Python None
    json_df = json_df.where(pd.notnull(json_df), None)
    
    # Find new categories not in Google Sheet
    new_categories_df = json_df[~json_df['Category'].isin(sheet_df['Category'])]
    
    # Append new categories to Google Sheet
    if not new_categories_df.empty:
        for index, row in new_categories_df.iterrows():
            # Convert row to list, ensuring NaN (now None) values are handled
            clean_row = row.tolist()
            worksheet.append_row(clean_row)
        print(f"Added {len(new_categories_df)} new categories to the Google Sheet.")
    else:
        print("No new categories to add.")

# Paths
user_home_dir = os.path.expanduser('~')
credentials_file_path = os.path.join(user_home_dir, 'Github', 'Accountinator', 'accountinator1.json')
json_file_path = os.path.join(user_home_dir, 'Github', 'Accountinator', 'csv', 'Test of Budget and Projections Foundation_Transaction Ontology2.json')

# Example usage
if __name__ == "__main__":
    google_sheet = 'Test of Budget and Projections Foundation'
    worksheet_name = 'Transaction Ontology'
    update_google_sheet_with_new_categories(google_sheet, worksheet_name, json_file_path, credentials_file_path)
