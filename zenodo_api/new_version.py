import requests
from zenodo_api.upload_files import load_access_token
from zenodo_api.url_selector import url_selector
import json


def get_latest_version(concept_rec_id):
    access_token = load_access_token()
    base_url = url_selector(tests=True) + "/records"

    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(f"{base_url}/{concept_rec_id}", headers=headers)

    return response.json()["id"]
