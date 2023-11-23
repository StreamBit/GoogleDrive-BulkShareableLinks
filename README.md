# Google Drive Shareable Links Generator

## Description
This Python script is designed to generate shareable links for all files within a specified Google Drive folder. It authenticates with Google Drive and fetches links in a read-only mode, ensuring no modifications are made to the drive contents.

## Requirements
- Google Drive API enabled in your Google Cloud project.
- `credentials.json` from the Google Developer Console for OAuth2 authentication.
- Python libraries: `google-auth-oauthlib`, `google-api-python-client`.

## Setup
1. Place your `credentials.json` file in the same directory as the script.
2. Install required libraries:
```
pip install google-auth-oauthlib google-api-python-client
```

## Usage
1. Run the script once to authenticate and save the authentication token:
```
python ScriptName.py # Replace ScriptName.py with the name of this script
```
2. Modify `folder_id` in the script with the ID of the Google Drive folder whose file links you want to generate.
3. Run the script again to fetch and save the links to `links.txt`.

## Features
- Generates shareable links for all files in a specified Google Drive folder.
- Saves the links and corresponding file names in a text file.
- Utilizes read-only access to ensure drive contents are not modified.

## Notes
- If modifying the OAuth scopes, delete `token.pickle` to re-authenticate.
- Ensure your Google Drive API is properly set up in the Google Cloud Console.

## Author
StreamBit
https://github.com/StreamBit
