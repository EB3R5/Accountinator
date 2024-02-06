import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# Function to read account names from JSON file
def load_accounts_from_json(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # If data is a dictionary, process it as initially intended
            if isinstance(data, dict):
                accounts = [entry['Account'] for entry in data.values()]
            # If data is unexpectedly a list, handle it appropriately
            elif isinstance(data, list):
                accounts = [item['Account'] for item in data]
            else:
                messagebox.showerror("Error", "Unexpected JSON structure.")
                return []
            return accounts
    except FileNotFoundError:
        messagebox.showerror("Error", "JSON file not found.")
        return []
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Invalid JSON format.")
        return []
    except KeyError:
        messagebox.showerror("Error", "Incorrect JSON structure for accounts.")
        return []

# Adjust the path as needed
json_file_path = os.path.join(os.path.expanduser('~'), 'Github', 'Accountinator', 'csv', 'accounts_data.json')

# Load account names dynamically from the JSON file
accounts = load_accounts_from_json(json_file_path)


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
        account_name = row.get('Account')
        if account_name in account_balances:
            try:
                balance = float(account_balances[account_name])
                row['Balance'] = f"{balance:.2f}" if balance % 1 else str(int(balance))
                row['Date'] = current_date
                row['Time'] = current_time
                updated = True
            except ValueError:
                messagebox.showwarning("Warning", f"Invalid balance for account {account_name}. Please enter a numeric value.")
                return False  # Abort the update due to invalid input
    
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
    account_balances = {account: entry.get() for account, entry in balance_entries.items() if entry.get()}
    
    if update_balances(account_balances):
        messagebox.showinfo("Success", "Balances updated successfully!")
        for entry in balance_entries.values():  # Clear entries after update
            entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Info", "No balances were updated or invalid input detected.")

# Create the GUI window
root = tk.Tk()
root.title("Update Account Balances")

# Dictionary to hold the balance entry widgets
balance_entries = {}

# Generate dynamic account labels and balance entry fields based on loaded accounts
for i, account in enumerate(accounts):
    tk.Label(root, text=account).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    balance_entry = ttk.Entry(root)
    balance_entry.grid(row=i, column=1, padx=10, pady=5)
    balance_entries[account] = balance_entry  # Store the entry widget for later

# Update button
update_btn = ttk.Button(root, text="Update Balances", command=on_update)
update_btn.grid(row=len(accounts) + 1, column=0, columnspan=2, pady=20)

root.mainloop()
