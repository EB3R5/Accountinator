import os

from google.oauth2 import service_account
import googleapiclient.discovery

def main():
    # Load the service account key file.
    key_file = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

    # Create a service account credentials object.
    credentials = service_account.Credentials.from_service_account_file(
        key_file
    )

    # Create a Google API client.
    client = googleapiclient.discovery.build(
        "cloudresourcemanager", "v1", credentials=credentials
    )

    # Call the Google API.
    projects = client.projects().list().execute()

    # Print the results.
    print(projects)

if __name__ == "__main__":
    main()
