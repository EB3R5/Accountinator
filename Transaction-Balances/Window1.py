import tkinter as tk
from tkinter import ttk
import csv
import os

# Define the path to your CSV file
csv_file_path = os.path.join('C:\\Users\\chris\\Github\\Accountinator\\csv', 'data.csv')

# Function to update the balance for a specific account
def update_balance(account, new_balance):
    # Load the existing data
    rows = []
    updated = False
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Account'] == account:
                row['Balance'] = new_balance  # Update the balance
                updated = True
            rows.append(row)
    
    # Save the updated data back to the CSV
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return updated

# Function called when the update button is pressed
def on_update():
    account_name = account_entry.get()
    new_balance = balance_entry.get()
    if update_balance(account_name, new_balance):
        result_label.config(text="Balance updated successfully!")
    else:
        result_label.config(text="Account not found.")

# Create the GUI window
root = tk.Tk()
root.title("Update Account Balance")

# Create and pack the widgets for account name entry
tk.Label(root, text="Account Name:").grid(row=0, column=0, padx=10, pady=5)
account_entry = ttk.Entry(root)
account_entry.grid(row=0, column=1, padx=10, pady=5)

# Create and pack the widgets for balance entry
tk.Label(root, text="New Balance:").grid(row=1, column=0, padx=10, pady=5)
balance_entry = ttk.Entry(root)
balance_entry.grid(row=1, column=1, padx=10, pady=5)

# Update button
update_btn = ttk.Button(root, text="Update Balance", command=on_update)
update_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
