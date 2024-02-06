import tkinter as tk
from tkinter import ttk
import subprocess
import os

# Functions to run specific scripts with dynamic directory paths
def balance_update():
    script_path = os.path.expanduser(r'~\Github\Accountinator\Transaction-Balances\window6_json.py')
    subprocess.run(["python", script_path], check=True)

def balance_insert():
    script_path = os.path.expanduser(r'~\Github\Accountinator\Transaction-Balances\insert_balance_json2.py')
    subprocess.run(["python", script_path], check=True)

def update_categories():
    script_path = os.path.expanduser(r'~\Github\Accountinator\Budget-Projections\input_window3.py')
    subprocess.run(["python", script_path], check=True)

def insert_categories():
    script_path = os.path.expanduser(r'~\Github\Accountinator\Budget-Projections\compare_and_update_3.py')
    subprocess.run(["python", script_path], check=True)

# Create the main window
root = tk.Tk()
root.title("Accountinator Dashboard")
root.geometry("600x400")

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')  # Expand the notebook to fill the window

# Define sections and their corresponding buttons
sections = {
    "Transactions & Balances": [("Balance Update", balance_update), ("Balance Insert", balance_insert)],
    "Spend Provisions": [],
    "Securities": [],
    "Inventory": [],
    "Data": [],
    "Connectors": [],
    "Budget and Projections": [("Update Categories", update_categories), ("Insert Categories", insert_categories)],
}

for section, buttons in sections.items():
    # Create a frame for each section
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=section)
    
    # Add specific buttons for each section
    for button_text, button_command in buttons:
        ttk.Button(frame, text=button_text, command=button_command).pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
