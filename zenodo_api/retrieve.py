import requests
from zenodo_api.upload_files import load_access_token


def retrieve_file(id, id_file):

    download_info = get_download(id, id_file)
    url = download_info["url"]
    filename = download_info["filename"]

    download_response = requests.get(url)

    with open(filename, mode="wb") as file:
        file.write(download_response.content)

    return download_response


def get_download(id, id_file):
    response_info = retrieve_file_info(id, id_file)
    url = response_info.json()["links"]["download"]
    filename = response_info.json()["filename"]

    return {"url": url, "filename": filename}


def retrieve_file_info(id, id_file):
    ACCESS_TOKEN = load_access_token()
    response_info = requests.get(
        f"https://sandbox.zenodo.org/api/deposit/depositions/{id}/files/{id_file}",
        [("access_token", ACCESS_TOKEN), ("size", 100)],
    )

    return response_info
