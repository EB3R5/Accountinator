import tkinter as tk
from tkinter import ttk
import json
import os
from collections import defaultdict

def load_accounts_from_json():
    json_file_path = os.path.join(os.path.expanduser('~'), 'Github', 'Accountinator', 'csv', 'Account Activity Foundation_Accounts1.json')
    with open(json_file_path, 'r') as f:
        return json.load(f)

def summarize_data(data):
    summary = defaultdict(lambda: defaultdict(list))
    for item in data.values():
        account_class = item.get("Class", "Unknown")
        account_type = item.get("Type", "Unknown")
        summary[account_class][account_type].append(item)
    return summary

def populate_tree(tree, summary):
    for account_class, types in summary.items():
        class_node = tree.insert('', 'end', text=account_class, open=True)
        for account_type, accounts in types.items():
            type_node = tree.insert(class_node, 'end', text=account_type, open=True)
            for account in accounts:
                account_name = account.get("Account", "Unknown Account")
                amount = account.get("Amount", "0")
                detail_text = f"{account_name}: {amount}"
                tree.insert(type_node, 'end', text=detail_text)

# Main application window
root = tk.Tk()
root.title("Account Summary")

tree = ttk.Treeview(root)
tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Load and summarize data
data = load_accounts_from_json()
summary = summarize_data(data)

# Populate the tree with summarized data
populate_tree(tree, summary)

root.mainloop()
