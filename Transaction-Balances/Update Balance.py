import gspread
from oauth2client.service_account import ServiceAccountCredentials

def update_bank_balance(sheet_name, cell, new_balance):
    # Define the scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('C:\Users\chris\Github\Accountinator', scope)

    # Authorize the clientsheet 
    client = gspread.authorize(creds)

    # Open the sheet
    sheet = client.open(Balance_History).Balance_History  # If your sheet is named differently, adjust this line

    # Update the specified cell
    sheet.update_acell(cell, new_balance)

    print(f"Updated cell {cell} with new balance: {new_balance}")

# Example usage
sheet_name = 'Your Bank Account Balances'  # Name of your Google Sheet
cell = 'B2'  # The cell you want to update, e.g., B2 for the second column, second row
new_balance = '1000'  # New balance you want to set

update_bank_balance(sheet_name, cell, new_balance)
