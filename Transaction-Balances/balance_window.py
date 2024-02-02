import tkinter as tk
from tkinter import simpledialog
import csv
import os

# Define the path to your CSV file
csv_file_path = os.path.join('C:\\Users\\chris\\Github\\Accountinator\\csv', 'data.csv')

# Function to update a row in the CSV file
def update_csv(date, account_number, new_data):
    # Load the existing data
    rows = []
    updated = False
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == date and row['Account #'] == account_number:
                rows.append(new_data)  # Update with new data
                updated = True
            else:
                rows.append(row)
    
    if not updated:  # If the row wasn't found, append the new data
        rows.append(new_data)
    
    # Save the updated data back to the CSV
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'Time', 'Account', 'Account #', 'Account ID', 'Institution', 'Balance', 'Month', 'Week', 'Index', 'Type', 'Class', 'Updated'])
        writer.writeheader()
        writer.writerows(rows)

# Function called when the update button is pressed
def on_update():
    date = simpledialog.askstring("Input", "Enter Date of the row to update:")
    account_number = simpledialog.askstring("Input", "Enter Account # of the row to update:")
    
    # Collect new data via dialog (can be improved for better user experience)
    new_data = {
        'Date': date,
        'Time': simpledialog.askstring("Input", "Enter new Time:"),
        'Account': simpledialog.askstring("Input", "Enter new Account:"),
        'Account #': account_number,
        'Account ID': simpledialog.askstring("Input", "Enter new Account ID:"),
        'Institution': simpledialog.askstring("Input", "Enter new Institution:"),
        'Balance': simpledialog.askstring("Input", "Enter new Balance:"),
        'Month': simpledialog.askstring("Input", "Enter new Month:"),
        'Week': simpledialog.askstring("Input", "Enter new Week:"),
        'Index': simpledialog.askstring("Input", "Enter new Index:"),
        'Type': simpledialog.askstring("Input", "Enter new Type:"),
        'Class': simpledialog.askstring("Input", "Enter new Class:"),
        'Updated': simpledialog.askstring("Input", "Enter Updated date:")
    }
    update_csv(date, account_number, new_data)
    tk.messagebox.showinfo("Update", "Row updated successfully!")

# Create the GUI window
root = tk.Tk()
root.title("CSV Row Updater")

# Update button
update_btn = tk.Button(root, text="Update Row", command=on_update)
update_btn.pack(pady=20)

root.mainloop()
