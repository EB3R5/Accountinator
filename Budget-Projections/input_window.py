import tkinter as tk
from tkinter import ttk, messagebox
import json

# Predefined options for the dropdown menus
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
CASHFLOW_TYPE_OPTIONS = ['Operating Activities', 'Investing Activities', 'Financing Activities',
 'Fixed Asset Activities']
DISCRETIONARY_OPTIONS = ['Discretionary', 'Non-Discretionary']  # Added options for discretionary selection

# Path to the JSON file
json_file_path = 'data.json'

def load_json():
    """Load the existing data from the JSON file."""
    try:
        with open(json_file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Invalid JSON format.")
        return None

def save_json(data):
    """Save data to the JSON file."""
    try:
        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Success", "Category added successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

def add_category():
    """Add a new category to the JSON file."""
    data = load_json()
    if data is None:  # If there was an error loading the file
        return

    # Create a new category dictionary
    new_category = {
        "Category": category_entry.get(),
        "Group": group_var.get() if group_var.get() != 'None' else "",
        "Type": type_var.get(),
        "Cashflow Type": cashflow_type_var.get(),
        "Discretionary": discretionary_var.get()  # Capture the discretionary selection
    }

    # Add the new category to the data list and save it
    data.append(new_category)
    save_json(data)

    # Clear the input fields
    category_entry.delete(0, tk.END)
    group_var.set(GROUP_OPTIONS[0])
    type_var.set(TYPE_OPTIONS[0])
    cashflow_type_var.set(CASHFLOW_TYPE_OPTIONS[0])
    discretionary_var.set(DISCRETIONARY_OPTIONS[0])  # Reset the discretionary dropdown

# Create the main window
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

# New dropdown for Discretionary/Non-Discretionary
discretionary_var = tk.StringVar(value=DISCRETIONARY_OPTIONS[0])
tk.Label(root, text="Discretionary").grid(row=4, column=0)
discretionary_menu = ttk.Combobox(root, textvariable=discretionary_var, values=DISCRETIONARY_OPTIONS, state="readonly")
discretionary_menu.grid(row=4, column=1)

# Add button
add_button = ttk.Button(root, text="Add Category", command=add_category)
add_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()