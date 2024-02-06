import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

def load_accounts_from_json():
    json_file_path = os.path.join(os.path.expanduser('~'), 'Github', 'Accountinator', 'csv', 'Account Activity Foundation_Accounts1.json')
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, dict):
                accounts = [entry['Account'] for entry in data.values()]
            elif isinstance(data, list):
                accounts = [item['Account'] for item in data]
            else:
                messagebox.showerror("Error", "Unexpected JSON structure.")
                return []
            return sorted(set(accounts))  # Sort and remove duplicates
    except FileNotFoundError:
        messagebox.showerror("Error", "JSON file not found.")
        return []
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Invalid JSON format.")
        return []
    except KeyError:
        messagebox.showerror("Error", "Incorrect JSON structure for accounts.")
        return []

def update_balances(account_balances):
    json_file_path = os.path.join(os.path.expanduser('~'), 'Github', 'Accountinator', 'csv', 'accounts_data.json')
    try:
        # Assuming we're appending/updating the file, not overwriting
        data = []
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        for account, balance in account_balances.items():
            updated = False
            for entry in data:
                if entry['Account'] == account:
                    entry['Balance'] = balance
                    entry['Date'] = datetime.now().strftime('%Y-%m-%d')
                    entry['Time'] = datetime.now().strftime('%H:%M:%S')
                    updated = True
                    break
            if not updated:
                # If account does not exist, append a new record
                data.append({
                    'Account': account,
                    'Balance': balance,
                    'Date': datetime.now().strftime('%Y-%m-%d'),
                    'Time': datetime.now().strftime('%H:%M:%S')
                })
        with open(json_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Success", "Balances updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update balances: {e}")

def on_update():
    account_balances = {}
    for account, entry in balance_entries.items():
        balance = entry.get()
        if balance:  # Ensure balance is not empty
            account_balances[account] = balance
    # Handle dropdown selection if any
    selected_account = selected_account_var.get()
    if selected_account and selected_account != "Select Account":
        account_balances[selected_account] = balance_entry_for_selected_account.get()
    update_balances(account_balances)

accounts = load_accounts_from_json()

root = tk.Tk()
root.title("Update Account Balances")
balance_entries = {}
selected_account_var = tk.StringVar(value="Select Account")

for i, account in enumerate(accounts[:10]):
    tk.Label(root, text=account).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = ttk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    balance_entries[account] = entry

if len(accounts) > 10:
    ttk.Label(root, text="Other Accounts").grid(row=10, column=0, padx=10, pady=5, sticky="w")
    accounts_menu = ttk.Combobox(root, textvariable=selected_account_var, values=['Select Account'] + accounts[10:])
    accounts_menu.grid(row=10, column=1, padx=10, pady=5)
    balance_entry_for_selected_account = ttk.Entry(root)
    balance_entry_for_selected_account.grid(row=11, column=1, padx=10, pady=5)

ttk.Button(root, text="Update Balances", command=on_update).grid(row=12, column=0, columnspan=2, pady=20)

root.mainloop()
