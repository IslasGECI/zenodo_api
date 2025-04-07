import requests
from zenodo_api.upload_files import load_access_token
from zenodo_api.url_selector import url_selector
import json


def get_latest_version(RECORD_ID):
    ACCESS_TOKEN = load_access_token()
    BASE_URL = url_selector(tests=True) + "/records"

    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    response = requests.get(f"{BASE_URL}/{RECORD_ID}", headers=headers)

    print(json.dumps(response.json(), indent=4))

    return response
