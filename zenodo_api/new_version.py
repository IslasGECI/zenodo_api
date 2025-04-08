import requests
from zenodo_api.upload_files import load_access_token
from zenodo_api.url_selector import url_selector


def get_latest_version_id(concept_rec_id):
    access_token = load_access_token()
    base_url = url_selector(tests=True) + "/records"

    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(f"{base_url}/{concept_rec_id}", headers=headers)

    return response.json()["id"]


def create_draft_of_new_version(latest_version_id):
    access_token = load_access_token()
    base_url = url_selector(tests=True) + "/deposit/depositions"

    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.post(f"{base_url}/{latest_version_id}/actions/newversion", headers=headers)

    return response
