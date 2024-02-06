import pandas as pd
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

# Set up the connection to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
user_home_dir = os.path.expanduser('~')
credentials_path = os.path.join(user_home_dir, 'Github', 'Accountinator', 'accountinator1.json')  # Update the path as necessary
client = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope))

# Open the Google Sheets and specific worksheets
workbook1 = client.open("Money Projection Provision")
sheet1 = workbook1.worksheet("Add Projection")  # Adjust to the correct worksheet name if different

workbook2 = client.open("Test of Budget and Projections Foundation")
sheet2 = workbook2.worksheet("2020")  # Adjust to the correct worksheet name if different

all_values = sheet1.get_all_values()

# Assuming the first row is your header (adjust as necessary if it's a different row)
headers = all_values[0]  # This is the header row
data_values = all_values[1:]  # These are the rows of data excluding the header

# Manually create a DataFrame with the specified headers
data1 = pd.DataFrame(data_values, columns=headers)

data2 = pd.DataFrame(sheet2.get_all_records())

# Ensure 'Date' in data1 is datetime type for easier manipulation
data1['Date'] = pd.to_datetime(data1['Date'])

# Add a 'Month' column to data1 for grouping
data1['Month'] = data1['Date'].dt.month_name()

# Aggregate data1 by Category and Month, summing up the 'Value'
aggregated_data1 = data1.groupby(['Category', 'Month'], as_index=False)['Value'].sum()

# Iterate through each row in aggregated_data1 to update data2
for index, row in aggregated_data1.iterrows():
    category = row['Category']
    month = row['Month']
    value = row['Value']
    
    # Find the corresponding row in data2 by Category
    data2_index = data2[data2['Category'] == category].index
    
    if not data2_index.empty:
        # Convert month name to its corresponding column in data2
        # Ensure data2 has columns for each month matching the month name exactly
        if month in data2.columns:
            # Assuming you want to add to the existing value
            current_value = data2.at[data2_index[0], month] or 0  # Handle None or NaN
            data2.at[data2_index[0], month] = current_value + value

# At this point, data2 contains the updated values. Next, update the Google Sheet with data2.
# This step requires using gspread functions to write data2 back to the Google Sheet.
# The following is a placeholder for the update logic:
# workbook2.values_update(
#     sheet2.title,
#     params={'valueInputOption': 'USER_ENTERED'},
#     body={'values': data2.values.tolist()}
# )

# Note: The code above for updating the Google Sheet with data2 may need adjustments based on your exact sheet structure and requirements.
