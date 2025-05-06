import requests
from zenodo_api.upload_files import load_access_token, upload_file, upload_metadata
from zenodo_api.url_selector import url_selector


def get_latest_version_id(concept_rec_id):
    is_sandbox = True
    return xxget_latest_version_id(concept_rec_id, is_sandbox)


def xxget_latest_version_id(concept_rec_id, is_sandbox):
    access_token = load_access_token()
    base_url = url_selector(tests=is_sandbox) + "/records"

    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(f"{base_url}/{concept_rec_id}", headers=headers)

    return response.json()["id"]


def create_draft_of_new_version(latest_version_id):
    access_token = load_access_token()
    base_url = url_selector(tests=True) + "/deposit/depositions"

    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.post(f"{base_url}/{latest_version_id}/actions/newversion", headers=headers)

    return response


def upload_file_in_new_version(concept_rec_id, file_path):
    latest_version_id = xxget_latest_version_id(concept_rec_id, is_sandbox=True)
    new_deposition = create_draft_of_new_version(latest_version_id)

    new_deposition_json = new_deposition.json()
    new_deposition_id = new_deposition_json["id"]
    previous_metadata = new_deposition_json["metadata"]
    upload_metadata(previous_metadata, new_deposition_id)

    delete_previous_files(new_deposition_json)

    bucket_url = new_deposition_json["links"]["bucket"]

    response = upload_file(bucket_url, file_path)
    return response


def delete_previous_files(new_deposition_json):
    access_token = load_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    for files in new_deposition_json["files"]:
        requests.delete(files["links"]["self"], headers=headers)


def publish_new_version(concept_rec_id, file_path, is_test):
    latest_version_id = xxget_latest_version_id(concept_rec_id, is_sandbox=is_test)
    new_deposition = create_draft_of_new_version(latest_version_id)

    new_deposition_json = new_deposition.json()
    new_deposition_id = new_deposition_json["id"]
    previous_metadata = new_deposition_json["metadata"]
    upload_metadata(previous_metadata, new_deposition_id)

    delete_previous_files(new_deposition_json)

    bucket_url = new_deposition_json["links"]["bucket"]

    upload_file(bucket_url, file_path)

    base_url = url_selector(tests=is_test) + "/deposit/depositions"

    print(f"{base_url}/{new_deposition_id}/actions/publish")

    access_token = load_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(
        f"{base_url}/{new_deposition_id}/actions/publish",
        headers=headers,
    )

    return response
