import tkinter as tk
from tkinter import ttk
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Function to load categories from JSON
def load_categories_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        return json.load(file)

# Function to insert data into Google Sheets
def insert_into_google_sheet(data):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/service-account-file.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Your Spreadsheet Name").worksheet("Your Worksheet Name")
    
    for item in data:
        row = [item['Category'], item['Group'], selected_type.get(), selected_cashflow_type.get(), item['Rollover To']]
        sheet.append_row(row)

# Load JSON data
categories = load_categories_from_json('categories.json')

# GUI setup
root = tk.Tk()
root.title("Insert Categories to Google Sheet")

# Dropdown for "Type"
type_options = ["Expense", "Income"]  # Example options; adjust as needed
selected_type = tk.StringVar()
type_dropdown = ttk.Combobox(root, textvariable=selected_type, values=type_options)
type_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for "Cashflow Type"
cashflow_type_options = ["Operating Activities", "Investing Activities", "Financing Activities"]
selected_cashflow_type = tk.StringVar()
cashflow_type_dropdown = ttk.Combobox(root, textvariable=selected_cashflow_type, values=cashflow_type_options)
cashflow_type_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Button to insert data
insert_button = ttk.Button(root, text="Insert to Google Sheet", command=lambda: insert_into_google_sheet(categories))
insert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
