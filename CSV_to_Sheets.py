import os
import pandas as pd
import gspread
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Path to your Service Account Credential JSON file
credential_path = 'PATH TO YOUR SERVICE ACCOUNT JSON FILE'

# Directory containing the CSV files
csv_folder_path = r'PATH TO THE FOLDER CONTAINING CSV FILE/FILES'

# Google Drive folder ID where the Google Sheets will be saved
google_drive_folder_id = 'GOOGLE DRIVE FOLDER ID' # ID can be found be opening the folder ina  browser and copy the part after https://drive.google.com/drive/folders/xxxxxxxxx

scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive']

# Authenticate using the credential file
credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_path, scope)
gc = gspread.authorize(credentials)
drive_service = build('drive', 'v3', credentials=credentials)

# Function to create and upload a Google Sheet from a CSV file
def upload_csv_to_google_sheets(csv_path, sheet_title, folder_id):
    df = pd.read_csv(csv_path)
    df.fillna("", inplace=True)
    
    sheet = gc.create(sheet_title)
    
    # Move the sheet to the specified folder in Drive
    file = drive_service.files().get(fileId=sheet.id, fields='parents').execute()
    previous_parents = ",".join(file.get('parents'))
    drive_service.files().update(fileId=sheet.id,
                                 addParents=folder_id,
                                 removeParents=previous_parents,
                                 fields='id, parents').execute()
    
    worksheet = sheet.get_worksheet(0)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print(f'Uploaded {sheet_title} to Google Drive folder ID {folder_id}')

# Iterate through CSV files in the folder and upload them as Google Sheets
for csv_file in os.listdir(csv_folder_path):
    if csv_file.endswith('.csv'):
        csv_path = os.path.join(csv_folder_path, csv_file)
        sheet_title = os.path.splitext(csv_file)[0]  # Use the CSV filename as the sheet title
        upload_csv_to_google_sheets(csv_path, sheet_title, google_drive_folder_id)
