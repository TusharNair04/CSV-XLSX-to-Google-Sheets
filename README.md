
# CSV to Google Sheets Uploader

This Python script automates the process of converting CSV files into Google Sheets and uploading them to a specified folder in Google Drive.

## Features

- **Batch Processing**: Automatically processes multiple CSV files from a specified folder.
- **Google Sheets Creation**: Dynamically creates a new Google Sheet for each CSV file.
- **Folder Organization**: Uploads all created Google Sheets into a specific Google Drive folder.
- **NaN Handling**: Replaces any `NaN` values in the CSV files with empty strings to ensure compatibility with Google Sheets.

## Prerequisites

- Python 3.x
- Google Cloud Platform account
- Enabled Google Sheets API and Google Drive API
- Service account with appropriate permissions

## Dependencies

Install the necessary Python packages using pip:

```bash
pip install gspread pandas oauth2client google-api-python-client
```

## Setup

1. **Google Cloud Platform Configuration**:
   - Create a new project.
   - Enable Google Sheets API and Google Drive API for the project.
   - Create a service account and download the JSON credentials file.

2. **Share Target Folder**:
   - Create a folder in Google Drive where you want to upload the Google Sheets.
   - Share this folder with the email address of your service account.

## Configuration

- Replace `PATH TO YOUR SERVICE ACCOUNT JSON FILE` in the script with the path to your downloaded service account JSON file.
- Update `PATH TO THE FOLDER CONTAINING CSV FILE/FILES` with the path to the folder containing your CSV files.
- Set `GOOGLE DRIVE FOLDER ID` to the ID of the Google Drive folder where you want to upload the Sheets. The ID can be found in the folder's URL.

## Usage

Run the script using Python:

```bash
python upload_csv_to_google_sheets.py
```

## Limitations

- The script assumes that all CSV files in the specified folder are to be uploaded. Ensure that the folder contains only the target CSV files.
- The script replaces `NaN` values in the CSV files with empty strings. Modify the `fillna` method in the script if a different handling of `NaN` values is required.

## Contributing

Contributions to improve the script or address issues are welcome. Please feel free to fork the repository and submit pull requests.
