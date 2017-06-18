import os
import json
import requests
from base64 import b64encode

API_KEY = os.environ['google_api_key']


def make_payload(inputfile, filetype):
    """
    create payload in the format google api needs them to be
    """
    with open(inputfile, 'rb') as f:
        file = b64encode(f.read()).decode()
        if filetype == 'audio':
            payload = {
                "config": {
                    "encoding": "FLAC",
                    "sampleRateHertz": 16000,
                    "languageCode": "en-US"
                },
                "audio": {"content": caudio}
            }
            return json.dumps(payload)
        elif filetype == 'image':
            payload = {"requests":
                       {
                           'image': {'content': file},
                           'features': [{
                               'type': 'TEXT_DETECTION',
                                        'maxResults': 1
                                        }]
                       }
                       }
            return json.dumps(payload).encode()
        else:
            return None


def send_to_google(inputfile, filetype):
    """
    docstring
    """
    if filetype == 'audio':
        endpoint = 'https://speech.googleapis.com/v1/speech:recognize'
    elif filetype == 'image':
        endpoint = 'https://vision.googleapis.com/v1/images:annotate'
    else:
        endpoint = ''
    if endpoint:
        response = requests.post(endpoint,
                                 data=make_payload(inputfile=inputfile, filetype=filetype),
                                 params={'key': API_KEY},
                                 headers={'Content-Type': 'application/json'})
        resp = response.json()
        return resp
    else:
        return None
