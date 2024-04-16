import os
import tkinter as tk
from tkinter import ttk
import subprocess

def balance_update():
    script_path = os.path.expanduser('~/Documents/Github/Accountinator/Transaction-Balances/window6_json.py')
    try:
        subprocess.run(["python3", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the script: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def balance_insert():
    script_path = os.path.expanduser('~/Documents/Github/Accountinator/Transaction-Balances/insert_balance_json2.py')
    try:
        subprocess.run(["python3", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the script: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def update_categories():
    script_path = os.path.expanduser('~/Documents/Github/Accountinator/Budget-Projections/input_window3.py')
    try:
        subprocess.run(["python3", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the script: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def insert_categories():
    script_path = os.path.expanduser('~/Documents/Github/Accountinator/Budget-Projections/Compare and Update 3.py')
    try:
        subprocess.run(["python3", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the script: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

root = tk.Tk()
root.title("Accountinator Dashboard")
root.geometry("600x400")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

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
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=section)
    for button_text, button_command in buttons:
        ttk.Button(frame, text=button_text, command=button_command).pack(pady=10)

root.mainloop()
