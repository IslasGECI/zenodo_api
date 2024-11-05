import requests
from zenodo_api.upload_files import load_access_token


def retrieve_file(id, id_file):
    ACCESS_TOKEN = load_access_token()
    response_upload = requests.get(
        f"https://sandbox.zenodo.org/api/deposit/depositions/{id}/files/{id_file}",
        [("access_token", ACCESS_TOKEN), ("size", 100)],
    )
    return response_upload
