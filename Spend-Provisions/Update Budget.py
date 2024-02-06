import pandas as pd
import gspread
import os
import tkinter as tk
from tkinter import ttk, messagebox
import json
from oauth2client.service_account import ServiceAccountCredentials

# Set up the connection to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
user_home_dir = os.path.expanduser('~')
credentials_path = os.path.join(user_home_dir, 'Github', 'Accountinator', 'accountinator1.json')  # Update the path as necessary
client = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope))

workbook2 = client.open("Test of Budget and Projections Foundation1")
sheet2 = workbook2.worksheet("Projection 1")  # Adjust to the correct worksheet name if different

# Assuming your JSON file structure and function definitions for loading and saving JSON

# Path to the JSON file
json_file_path = os.path.join(user_home_dir, 'Github', 'Accountinator', 'csv', 'Test of Budget and Projections Foundation1_Transaction Ontology.json')

def load_json():
    try:
        with open(json_file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "JSON file not found.")
        return None
    except json.JSONDecodeError as e:
        messagebox.showerror("Error", f"Invalid JSON format: {e}")
        return None

def save_json(data):
    try:
        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Success", "Data updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

# GUI Components
root = tk.Tk()
root.title("Update Category Values")

# Assume month_var, month_menu, category_var, category_menu, value_entry, and update_button are defined as above

# You may need to fetch categories from the JSON or Google Sheet to populate category options dynamically
category_options = [category["Category"] for category in load_json()]  # Update to dynamically load categories if they're not static
category_var = tk.StringVar(value=category_options[0])
category_menu = ttk.Combobox(root, textvariable=category_var, values=category_options, state="readonly")
category_menu.grid(row=0, column=1)

# Rest of the GUI setup for month selection, value entry, and update button

root.mainloop()
