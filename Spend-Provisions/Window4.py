import tkinter as tk
from tkinter import ttk
import json

# Load grouped categories from JSON file
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

# Event handler for category selection
def on_category_selected(event):
    selected_item = event.widget.selection()
    if selected_item:
        item = event.widget.item(selected_item)
        selected_category.set(item['text'])  # Update the label or entry with the selected category name

# Update monthly value for the selected category
def update_monthly_value():
    category = selected_category.get()
    value = value_entry.get()
    print(f"Updating {category} with value {value}")  # Placeholder for actual update logic
    # Here you would include the logic to update your storage with the new value
    selected_category.set('')
    value_entry.delete(0, tk.END)

# Create the main window and layout
root = tk.Tk()
root.title("Categories by Group")

# Frame for the prioritized categories
frame_prioritized = ttk.LabelFrame(root, text="Prioritized Expenses")
frame_prioritized.pack(side="top", fill="x", expand=False)

# Frame for the other categories
frame_other = ttk.LabelFrame(root, text="Other Categories")
frame_other.pack(side="top", fill="x", expand=True)

# Function to create and return a treeview widget
def create_treeview(parent):
    tree = ttk.Treeview(parent)
    tree.pack(expand=True, fill='both')
    return tree

tree_prioritized = create_treeview(frame_prioritized)
tree_other = create_treeview(frame_other)

# Bind the selection event of the treeviews
tree_prioritized.bind('<<TreeviewSelect>>', on_category_selected)
tree_other.bind('<<TreeviewSelect>>', on_category_selected)

# Variable to hold the selected category name
selected_category = tk.StringVar()

# Input field and button for updating monthly values
value_entry = ttk.Entry(root)
value_entry.pack(side="top", fill="x", padx=5, pady=5)

update_button = ttk.Button(root, text="Update Value", command=update_monthly_value)
update_button.pack(side="top", fill="x", padx=5, pady=5)

# Load categories grouped by their group from the JSON file
json_file_path = 'C:\\Users\\christian\\Github\\Accountinator\\csv\\Test of Budget and Projections Foundation1_Transaction Ontology.json'

grouped_prioritized, grouped_other = load_grouped_categories(json_file_path)

# Function to insert data into a treeview widget
def insert_data_into_treeview(tree, grouped_data):
    for group, categories in grouped_data.items():
        group_id = tree.insert("", tk.END, text=group)  # Insert the group
        for category in categories:
            tree.insert(group_id, tk.END, text=category)  # Insert categories under their group

# Insert data into Treeviews
insert_data_into_treeview(tree_prioritized, grouped_prioritized)
insert_data_into_treeview(tree_other, grouped_other)

root.mainloop()
