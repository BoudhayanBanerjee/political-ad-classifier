from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.file'
CLIENT_SECRET_FILE = '../credentials/client_secret.json'
APPLICATION_NAME = 'googlecloudvisionspeech'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-googlecloudvisionspeech.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def upload(inputPath, uploadType, foldername=None):
    """
    docstring
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    if uploadType != 'folder':
        filename = os.path.basename(inputPath)
        file_metadata = {
            'name': filename
        }
        if uploadType == 'video':
            media = MediaFileUpload(inputPath, mimetype='video/mp4')
        elif uploadType == 'image':
            media = MediaFileUpload(inputPath, mimetype='image/png')
        elif uploadType == 'audio':
            media = MediaFileUpload(inputPath, mimetype='audio/mp3')
        elif uploadType == 'json':
            media = MediaFileUpload(inputPath, mimetype='text/json')
        elif uploadType == 'text':
            media = MediaFileUpload(inputPath, mimetype='text/text')

        file = service.files().create(body=file_metadata,
                                      media_body=media,
                                      fields='id').execute()
    else:
        foldername = foldername
        file_metadata = {
            'name': foldername,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = service.files().create(body=file_metadata,
                                      fields='id').execute()
        folder_id = file.get('id')
        for file in os.listdir(inputPath):
            # determine mimetype
            if file.endswith('.mp4'):
                mimetype = 'video/mp4'
            elif file.endswith('.mp3'):
                mimetype = 'audio/mp3'
            elif file.endswith('.json'):
                mimetype = 'text/json'
            elif file.endswith('.png'):
                mimetype = 'image/png'
            elif file.endswith('.txt'):
                mimetype = 'text/text'
            else:
                mimetype = 'text/text'
            filepath = os.path.join(inputPath, file)
            file_metadata = {
                'name': file,
                'parents': [folder_id]
            }
            media = MediaFileUpload(filepath, mimetype=mimetype)
            file = service.files().create(body=file_metadata,
                                          media_body=media,
                                          fields='id').execute()


if __name__ == '__main__':
    inputPath = r'D:\adclassifier\labelled_dataset\political\videos'
    uploadType = 'folder'
    foldername = 'politcal_videos'
    upload(inputPath=inputPath, uploadType=uploadType, foldername=foldername)
