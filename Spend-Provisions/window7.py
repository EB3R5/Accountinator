import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime
from tkinter import messagebox

# Function to create and return a treeview widget
def create_treeview(parent):
    tree = ttk.Treeview(parent)
    tree.pack(expand=True, fill='both')
    return tree

# Function to insert data into a treeview widget
def insert_data_into_treeview(tree, grouped_data):
    for group, categories in grouped_data.items():
        group_id = tree.insert("", tk.END, text=group)  # Insert the group
        for category in categories:
            tree.insert(group_id, tk.END, text=category)  # Insert categories under their group

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

# Update monthly value for the selected category and produce a new JSON file with all category attributes
def update_monthly_value():
    # Retrieve the current category and value input by the user
    category = selected_category.get()
    value = value_entry.get()
    
    # Load the old JSON data
    json_file_path = 'C:\\Users\\christian\\Github\\Accountinator\\csv\\Test of Budget and Projections Foundation1_Transaction Ontology.json'
    with open(json_file_path, 'r') as file:
        old_data = json.load(file)
    
    # Find the category entry in the old data
    category_data = old_data.get(category)
    
    if category_data:
        # Capture the current date and month
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_month = datetime.now().strftime("%B")
        
        # Create or update the entry for the category in the updated data
        updated_category_data = {
            **category_data,  # Include all existing attributes
            "Value": value,
            "Date": current_date,
            "Month": current_month
        }
        
        # Load or initialize the updated data storage
        updated_data_path = 'C:\\Users\\christian\\Github\\Accountinator\\csv\\updated_categories.json'  # Path to the new JSON file
        try:
            with open(updated_data_path, 'r') as file:
                updated_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            updated_data = {}
        
        # Use a unique index for each new entry, based on timestamp or incrementing existing index
        new_index = str(len(updated_data))  # Simple indexing based on count of items
        
        # Add the updated category data to the updated data
        updated_data[new_index] = updated_category_data
        
        # Save the updated data back to the new JSON file
        with open(updated_data_path, 'w') as file:
            json.dump(updated_data, file, indent=4)
        
        messagebox.showinfo("Success", f"Updated {category} with value {value} for {current_month}")
    else:
        messagebox.showerror("Error", f"Category '{category}' not found in the JSON data.")
    
    # Reset the input fields
    selected_category.set('')
    value_entry.delete(0, tk.END)

# Main GUI setup
root = tk.Tk()
root.title("Categories by Group")

# Setup for prioritized and other categories frames
frame_prioritized = ttk.LabelFrame(root, text="Prioritized Expenses")
frame_prioritized.pack(side="top", fill="x", expand=False)

frame_other = ttk.LabelFrame(root, text="Other Categories")
frame_other.pack(side="top", fill="x", expand=True)

# Create treeviews and bind selection events
tree_prioritized = create_treeview(frame_prioritized)
tree_other = create_treeview(frame_other)
tree_prioritized.bind('<<TreeviewSelect>>', on_category_selected)
tree_other.bind('<<TreeviewSelect>>', on_category_selected)

# Variable to hold the selected category name and setup for value input
selected_category = tk.StringVar()
value_entry = ttk.Entry(root)
value_entry.pack(side="top", fill="x", padx=5, pady=5)
update_button = ttk.Button(root, text="Update Value", command=update_monthly_value)
update_button.pack(side="top", fill="x", padx=5, pady=5)

# Load and display categories
json_file_path = 'C:\\Users\\christian\\Github\\Accountinator\\csv\\Test of Budget and Projections Foundation1_Transaction Ontology.json'
grouped_prioritized, grouped_other = load_grouped_categories(json_file_path)
insert_data_into_treeview(tree_prioritized, grouped_prioritized)
insert_data_into_treeview(tree_other, grouped_other)

root.mainloop()
