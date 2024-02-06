import tkinter as tk
from tkinter import ttk
import json

# Function to load categories from the JSON file
def load_categories(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    # Extract categories, assuming each entry has a 'Category' field
    categories = [entry['Category'] for entry in data.values()]
    return categories

# Create the main window
def create_window(categories):
    root = tk.Tk()
    root.title("Category List")

    # Use a Listbox to display categories
    listbox = tk.Listbox(root, height=20, width=50, bg="white")
    listbox.pack(side="left", fill="y")

    # Scrollbar
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    listbox.config(yscrollcommand=scrollbar.set)

    # Insert categories into the Listbox
    for category in categories:
        listbox.insert(tk.END, category)

    root.mainloop()

# Path to the JSON file
json_file_path = 'C:\\Users\\christian\\Github\\Accountinator\\csv\\Test of Budget and Projections Foundation1_Transaction Ontology.json'

# Load categories from the JSON file
categories = load_categories(json_file_path)

# Create and display the window with the category list
create_window(categories)
