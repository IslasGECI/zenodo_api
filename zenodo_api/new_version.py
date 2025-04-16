import requests
from zenodo_api.upload_files import load_access_token, xxupload_file
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


def upload_file_in_new_version(latest_version_id, file_path):
    access_token = load_access_token()
    new_deposition = create_draft_of_new_version(latest_version_id)
    previous_file = new_deposition.json()["files"][0]["links"]["self"]
    headers = {"Authorization": f"Bearer {access_token}"}
    requests.delete(previous_file, headers=headers)
    bucket_url = new_deposition.json()["links"]["bucket"]

    params = {"access_token": access_token}
    response = xxupload_file(bucket_url, file_path)
    return response
