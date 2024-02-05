import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

# Define the path to your CSV file
csv_file_path = os.path.join('C:\\Users\\chris\\Github\\Accountinator\\csv', 'data.csv')

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
    
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
        for row in rows:
            if row['Account'] in account_balances:
                # Convert balance to float then format it as a string without trailing zeros if it's an integer
                try:
                    balance = float(account_balances[row['Account']])
                    row['Balance'] = f"{balance:.2f}" if balance % 1 else str(int(balance))
                except ValueError:
                    messagebox.showwarning("Warning", f"Invalid balance for account {row['Account']}. Please enter a numeric value.")
                    return False  # Abort the update due to invalid input
                row['Date'] = current_date
                row['Time'] = current_time
                updated = True
    
    if updated:
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        return True
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
