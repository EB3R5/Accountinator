import tkinter as tk
from tkinter import ttk
import json

def load_grouped_categories(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    grouped_categories = {}
    for entry in data.values():
        group = entry['Group']
        category = entry['Category']
        if group in grouped_categories:
            grouped_categories[group].append(category)
        else:
            grouped_categories[group] = [category]
    return grouped_categories

def create_window(grouped_categories):
    root = tk.Tk()
    root.title("Categories by Group")

    tree = ttk.Treeview(root)
    tree.pack(expand=True, fill='both')

    # Define the columns
    tree['columns'] = ("Group", "Category")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Group", anchor=tk.W, width=120)
    tree.column("Category", anchor=tk.W, width=180)

    # Define the headings
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("Group", text="Group", anchor=tk.W)
    tree.heading("Category", text="Category", anchor=tk.W)

    # Inserting the grouped categories into the tree view
    for group, categories in grouped_categories.items():
        group_id = tree.insert("", tk.END, text="", values=(group,))  # Insert the group
        for category in categories:
            tree.insert(group_id, tk.END, text="", values=("", category))  # Insert categories under their group

    root.mainloop()

# Path to the JSON file
json_file_path = 'C:\\Users\\christian\\Github\\Accountinator\\csv\\Test of Budget and Projections Foundation1_Transaction Ontology.json'


# Load categories grouped by their group
grouped_categories = load_grouped_categories(json_file_path)

# Create and display the window with the categories grouped by group
create_window(grouped_categories)
