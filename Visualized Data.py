import tkinter as tk
from tkinter import ttk
import json
import os

def load_accounts_from_json():
    json_file_path = os.path.join(os.path.expanduser('~'), 'Github', 'Accountinator', 'csv', 'Account Activity Foundation_Accounts1.json')
    with open(json_file_path, 'r') as f:
        return json.load(f)

def populate_tree(tree, data):
    for key, value in data.items():
        account = value.get("Account", "Unknown Account")
        # Ensure the account name is not empty
        if account and account != "Unknown Account":  
            account_node = tree.insert('', 'end', text=account, open=True)
            for detail_key, detail_value in value.items():
                # Insert each detail as a child of the account node
                tree.insert(account_node, 'end', text=f"{detail_key}: {detail_value}")

# Main application window
root = tk.Tk()
root.title("Account Details")

# Adjust the column configuration as needed
tree = ttk.Treeview(root)
tree["columns"] = ("one")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.heading("#0",text="Account Details",anchor=tk.W)

# Load JSON data
data = load_accounts_from_json()

# Populate the tree with JSON data
populate_tree(tree, data)

tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

root.mainloop()
