import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# Define the path to your JSON file
json_file_path = os.path.join('C:\\Users\\chris\\Github\\Accountinator\\json', 'data.json')

# Account names statically listed
accounts = [
    "CREDIT CARD",
    "TOTAL CHECKING",
    "Amazon Store Card",
    "Cell Phone",
    "Medica",
    "Progressive",
    "LES Bill",
    "Psychologist",
    "YMCA",
    "Car Registration"
]

# Function to update the balance and add date-time stamp for specific accounts
def update_balances(account_balances):
    updated = False
    current_date = datetime.now().strftime('%Y-%m-%d')  # Format: YYYY-MM-DD
    current_time = datetime.now().strftime('%H:%M:%S')  # Format: HH:MM:SS
    rows = []

    # Try to read existing data from the JSON file
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            rows = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, we'll create it later
        pass
    except json.JSONDecodeError:
        messagebox.showwarning("Warning", "Invalid JSON format in existing file.")
        return False

    # Update data
    for row in rows:
        if row['Account'] in account_balances:
            try:
                balance = float(account_balances[row['Account']])
                row['Balance'] = f"{balance:.2f}" if balance % 1 else str(int(balance))
            except ValueError:
                messagebox.showwarning("Warning", f"Invalid balance for account {row['Account']}. Please enter a numeric value.")
                return False  # Abort the update due to invalid input
            row['Date'] = current_date
            row['Time'] = current_time
            updated = True
    
    # Write updated data back to the JSON file
    if updated:
        try:
            with open(json_file_path, 'w', encoding='utf-8') as file:
                json.dump(rows, file, indent=4)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to write to JSON file: {e}")
            return False
    return False

# Function called when the update button is pressed
def on_update():
    account_balances = {}
    for account, entry in balance_entries.items():
        balance = entry.get()
        if balance:  # Only update if a balance has been entered
            account_balances[account] = balance
    
    if update_balances(account_balances):
        messagebox.showinfo("Success", "Balances updated successfully!")
    else:
        messagebox.showinfo("Info", "No balances were updated or invalid input detected.")

# Create the GUI window
root = tk.Tk()
root.title("Update Account Balances")

# Dictionary to hold the balance entry widgets
balance_entries = {}

# Generate static account labels and balance entry fields
for i, account in enumerate(accounts):
    tk.Label(root, text=account).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    balance_entry = ttk.Entry(root)
    balance_entry.grid(row=i, column=1, padx=10, pady=5)
    balance_entries[account] = balance_entry  # Store the entry widget for later

# Update button
update_btn = ttk.Button(root, text="Update Balances", command=on_update)
update_btn.grid(row=len(accounts), column=0, columnspan=2, pady=20)

root.mainloop()
