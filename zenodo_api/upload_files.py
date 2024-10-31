import requests
import os


def call_depositions():
    ACCESS_TOKEN = load_access_token()
    empty_upload = requests.get(
        "https://sandbox.zenodo.org/api/deposit/depositions", [("access_token", ACCESS_TOKEN)]
    )
    return empty_upload


def load_access_token():
    return os.environ.get("ACCESS_TOKEN")


def create_empty_upload():
    headers = {"Content-Type": "application/json"}
    params = {"access_token": load_access_token()}
    r = requests.post(
        "https://sandbox.zenodo.org/api/deposit/depositions",
        params=params,
        json={},
        headers=headers,
    )
    return r


def upload_new_file():
    params = {"access_token": load_access_token()}
    empty_upload = create_empty_upload()

    bucket_url = empty_upload.json()["links"]["bucket"]
    filename = "tests_file.txt"
    path = f"tests/data/{filename}"

    with open(path, "rb") as file_content:
        response_upload = requests.put(
            f"{bucket_url}/{filename}",
            data=file_content,
            params=params,
        )
    return response_upload
