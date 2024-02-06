import tkinter as tk
from tkinter import ttk
import json

def load_grouped_categories(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Define prioritized categories
    prioritized = ["Groceries", "Rent", "Insurance", "Car", "Internet", "Cellphone"]
    
    # Initialize dictionaries for grouped categories
    grouped_prioritized = {}
    grouped_other = {}
    
    for entry in data.values():
        group = entry['Group']
        category = entry['Category']
        target_dict = grouped_prioritized if category in prioritized else grouped_other
        
        if group in target_dict:
            target_dict[group].append(category)
        else:
            target_dict[group] = [category]
    
    return grouped_prioritized, grouped_other

def create_window(grouped_prioritized, grouped_other):
    root = tk.Tk()
    root.title("Categories by Group")

    # Create frames for each section
    frame_prioritized = ttk.Frame(root, padding="3")
    frame_prioritized.pack(side="top", fill="x", expand=False)

    frame_other = ttk.Frame(root, padding="3")
    frame_other.pack(side="top", fill="x", expand=True)

    # Create Treeviews
    tree_prioritized = create_treeview(frame_prioritized, "Prioritized Expenses")
    tree_other = create_treeview(frame_other, "Other Categories")

    # Insert data into Treeviews
    insert_data_into_treeview(tree_prioritized, grouped_prioritized)
    insert_data_into_treeview(tree_other, grouped_other)

    root.mainloop()

def create_treeview(parent, label):
    label = ttk.Label(parent, text=label)
    label.pack(side="top", fill="x", expand=False)
    
    tree = ttk.Treeview(parent)
    tree.pack(side="top", fill="both", expand=True)

    return tree

def insert_data_into_treeview(tree, grouped_data):
    for group, categories in grouped_data.items():
        group_id = tree.insert("", tk.END, text=group)  # Insert the group
        for category in categories:
            tree.insert(group_id, tk.END, text=category)  # Insert categories under their group

# Path to the JSON file
json_file_path = 'C:\\Users\\christian\\Github\\Accountinator\\csv\\Test of Budget and Projections Foundation1_Transaction Ontology.json'



# Load categories grouped by their priority
grouped_prioritized, grouped_other = load_grouped_categories(json_file_path)

# Create and display the window with the categories grouped by priority
create_window(grouped_prioritized, grouped_other)
