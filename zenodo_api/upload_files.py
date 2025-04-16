import requests
import os
import json
import pathlib


def call_depositions():
    ACCESS_TOKEN = load_access_token()
    empty_upload = requests.get(
        "https://sandbox.zenodo.org/api/deposit/depositions",
        [("access_token", ACCESS_TOKEN), ("size", 200), ("all_versions", "true")],
    )
    return empty_upload


def load_access_token():
    return os.environ.get("ACCESS_TOKEN")


def create_deposition_in_new_record():
    headers = {"Authorization": f"Bearer {load_access_token()}", "Content-Type": "application/json"}
    r = requests.post(
        "https://sandbox.zenodo.org/api/deposit/depositions",
        json={},
        headers=headers,
    )
    return r


def upload_file_in_new_record(file_path):
    empty_upload = create_deposition_in_new_record()

    bucket_url = empty_upload.json()["links"]["bucket"]

    response_upload = upload_file(bucket_url, file_path)
    return {
        "response_upload": response_upload,
        "latest_draft": empty_upload.json()["links"]["latest_draft"],
    }


def upload_file(bucket_url, file_path):
    headers = {"Authorization": f"Bearer {load_access_token()}"}
    path = pathlib.Path(file_path)
    with open(path, "rb") as file_content:
        response_upload = requests.put(
            f"{bucket_url}/{path.name}",
            data=file_content,
            headers=headers,
        )

    return response_upload


def upload_metadata(data_dict):
    empty_upload = create_deposition_in_new_record()
    deposition_id = empty_upload.json()["id"]
    headers = {"Authorization": f"Bearer {load_access_token()}", "Content-Type": "application/json"}
    r = requests.put(
        f"https://sandbox.zenodo.org/api/deposit/depositions/{deposition_id}",
        data=json.dumps(data_dict),
        headers=headers,
    )
    return r
