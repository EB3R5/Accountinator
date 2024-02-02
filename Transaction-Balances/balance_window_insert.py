import tkinter as tk
from tkinter import ttk
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Function to insert data into Google Sheet
def insert_data():
    # Gather data from the entry fields
    row_data = [
        date_entry.get(),
        time_entry.get(),
        account_entry.get(),
        account_num_entry.get(),
        account_id_entry.get(),
        institution_entry.get(),
        balance_entry.get(),
        month_entry.get(),
        week_entry.get(),
        index_entry.get(),
        type_entry.get(),
        class_entry.get(),
        updated_entry.get()
    ]
    
    # Define the scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

    # Add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\chris\\Github\\Accountinator\\service.json', scope)

    # Authorize the client sheet
    gc = gspread.authorize(creds)

    # Open the spreadsheet and select the worksheet
    sh = gc.open('Account Activity Foundation')
    worksheet = sh.worksheet('Balance History')
    
    # Insert the row data
    worksheet.insert_row(row_data, index=2)  # Insert at the second row
    
    print("Data inserted successfully.")

# Create the GUI window
root = tk.Tk()
root.title("Update Balance History")

# Create and pack the widgets for data entry
labels = ["Date", "Time", "Account", "Account #", "Account ID", "Institution", "Balance", "Month", "Week", "Index", "Type", "Class", "Updated"]
for i, label in enumerate(labels):
    ttk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    globals()[label.lower().replace(' ', '_') + '_entry'] = ttk.Entry(root)
    globals()[label.lower().replace(' ', '_') + '_entry'].grid(row=i, column=1, padx=10, pady=5)

# Submit button
submit_btn = ttk.Button(root, text="Submit", command=insert_data)
submit_btn.grid(row=len(labels), column=0, columnspan=2, pady=10)

root.mainloop()
