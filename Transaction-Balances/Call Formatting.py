from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

# Set the path to your Google Cloud Platform service account credentials JSON file
SERVICE_ACCOUNT_FILE = os.path.join(os.path.expanduser('~'), 'Github', 'Accountinator', 'accountinator1.json')

# Define the scopes
SCOPES = [
    'https://www.googleapis.com/auth/script.projects',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Authenticate and construct service
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('script', 'v1', credentials=credentials)

# Define the script ID of your Apps Script project
SCRIPT_ID = '16TqtSssdHlmbRVJP-eAIoKUcO1-K84UMP2urlmnFpj2SSJfhtyIAbIxD'

def call_apps_script():
    # Define the API request
    request = {"function": "setColumnFormats"}

    try:
        # Make the API request to run the Apps Script function
        response = service.scripts().run(body=request, scriptId=SCRIPT_ID).execute()

        # Check for any errors in the response
        if 'error' in response:
            # Extract and print the error details from the response
            error = response['error']['details'][0]
            print(f"Script error message: {error['errorMessage']}")
            if 'scriptStackTraceElements' in error:
                print("Script error stacktrace:")
                for trace in error['scriptStackTraceElements']:
                    print(f"\t{trace['function']}: {trace['lineNumber']}")
        else:
            # Print the successful response from the Apps Script function
            print("Script called successfully")

    except Exception as e:
        # Handle any errors during the API request
        print(f"An error occurred: {e}")

# Call the function
call_apps_script()
