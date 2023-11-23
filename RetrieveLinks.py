import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    return service

def get_shareable_links(service, folder_id):
    query = f"'{folder_id}' in parents"
    results = service.files().list(q=query, pageSize=1000).execute()
    
    items = results.get('files', [])
    links_with_names = [(item['name'], f"https://drive.google.com/file/d/{item['id']}/view") for item in items]
    
    while 'nextPageToken' in results:
        results = service.files().list(q=query, pageSize=1000, pageToken=results['nextPageToken']).execute()
        items = results.get('files', [])
        links_with_names.extend([(item['name'], f"https://drive.google.com/file/d/{item['id']}/view") for item in items])
        
    return links_with_names

def main():
    service = get_service()
    folder_id = 'Your_Folder_ID'  # Replace with your folder ID (the string to the right of the last '/' in the folder URL)
    links_with_names = get_shareable_links(service, folder_id)
    
    with open('links.txt', 'w') as f:
        for file_name, link in links_with_names:
            f.write(f"{file_name}: {link}\n")
    print("Links and file names saved to links.txt")

if __name__ == '__main__':
    main()
