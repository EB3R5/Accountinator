import os
import tkinter as tk
from tkinter import ttk, messagebox
import json

# Use os.path.join for constructing file paths to ensure OS compatibility
# Get the current user's home directory
user_home_dir = os.path.expanduser('~')

# Predefined options for the dropdown menus (sorted for user convenience)
GROUP_OPTIONS = sorted([
    "Deposit to Checking", "Work", "Match", "Travel", "Furniture", "Transfer",
    "Personal", "Clothing", "Cloud", "Lifestyle", "Health", "Food", "Debt",
    "Insurance", "Securities Purchase", "Income", "Reading", "Car",
    "Applications", "Credit Card", "Kitchen", "Electronics", "Equipment Purchase",
    "Office", "Storage", "Charity", "Dividends", "Interest", "Insured Deposits",
    "Withdrawal", "Deposit", "Third Party Expert Work", "Securities Sale",
    "Automobile Purchase", "Tax", "Gifts", "Household", "Legal Fee",
    "Tools & Home Improvement", "Electrical", "Aviation", "Utilities", "Cellphone",
    "Rent"
])
TYPE_OPTIONS = ['Expense', 'Income', 'Investment']
CASHFLOW_TYPE_OPTIONS = ['Operating Activities', 'Investing Activities', 'Financing Activities', 'Fixed Asset Activities']
DISCRETIONARY_OPTIONS = ['Discretionary', 'Non-Discretionary']

# Path to the JSON file
json_file_path = os.path.join(user_home_dir, 'Github', 'Accountinator', 'csv', 'Test of Budget and Projections Foundation_Transaction Ontology2.json')

def load_json():
    try:
        with open(json_file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        messagebox.showerror("Error", f"Invalid JSON format at line {e.lineno}, column {e.colno}: {e.msg}")
    return None


def save_json(data):
    try:
        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Success", "Data updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

def entry_exists(entries, new_entry):
    for entry in entries:
        if all(entry.get(key) == new_entry.get(key) for key in new_entry):
            return True
    return False

def add_category():
    data = load_json()
    if data is None:
        return

    new_category = {
        "Category": category_entry.get(),
        "Group": group_var.get() if group_var.get() != 'None' else "",
        "Type": type_var.get(),
        "Cashflow Type": cashflow_type_var.get(),
        "Discretionary": discretionary_var.get()
    }

    if not entry_exists(data, new_category):
        data.append(new_category)
        save_json(data)
        messagebox.showinfo("Success", "New category added.")
    else:
        messagebox.showwarning("Duplicate", "This category already exists.")

    category_entry.delete(0, tk.END)
    group_var.set(GROUP_OPTIONS[0])
    type_var.set(TYPE_OPTIONS[0])
    cashflow_type_var.set(CASHFLOW_TYPE_OPTIONS[0])
    discretionary_var.set(DISCRETIONARY_OPTIONS[0])

root = tk.Tk()
root.title("Add New Category")

# Setup input fields and dropdown menus
tk.Label(root, text="Category").grid(row=0, column=0)
category_entry = ttk.Entry(root)
category_entry.grid(row=0, column=1)

group_var = tk.StringVar(value=GROUP_OPTIONS[0])
tk.Label(root, text="Group").grid(row=1, column=0)
group_menu = ttk.Combobox(root, textvariable=group_var, values=GROUP_OPTIONS, state="readonly")
group_menu.grid(row=1, column=1)

type_var = tk.StringVar(value=TYPE_OPTIONS[0])
tk.Label(root, text="Type").grid(row=2, column=0)
type_menu = ttk.Combobox(root, textvariable=type_var, values=TYPE_OPTIONS, state="readonly")
type_menu.grid(row=2, column=1)

cashflow_type_var = tk.StringVar(value=CASHFLOW_TYPE_OPTIONS[0])
tk.Label(root, text="Cashflow Type").grid(row=3, column=0)
cashflow_type_menu = ttk.Combobox(root, textvariable=cashflow_type_var, values=CASHFLOW_TYPE_OPTIONS, state="readonly")
cashflow_type_menu.grid(row=3, column=1)

discretionary_var = tk.StringVar(value=DISCRETIONARY_OPTIONS[0])
tk.Label(root, text="Discretionary").grid(row=4, column=0)
discretionary_menu = ttk.Combobox(root, textvariable=discretionary_var, values=DISCRETIONARY_OPTIONS, state="readonly")
discretionary_menu.grid(row=4, column=1) 

# Add button
add_button = ttk.Button(root, text="Add Category", command=add_category)
add_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()