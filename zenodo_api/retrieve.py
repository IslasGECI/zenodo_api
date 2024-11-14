import requests
from zenodo_api.upload_files import load_access_token


def search_record_by_title(title, creator):
    ACCESS_TOKEN = load_access_token()
    query = f"{title} AND {creator}"
    response_info = requests.get(
        "https://sandbox.zenodo.org/api/records", params={"q": query, "access_token": ACCESS_TOKEN}
    )
    return response_info


def download_from_filename(id, filename):
    response_info = search_record_by_title(id, "villlasante")
    print(response_info.json())
    extracted_id = extract_record_id_and_file_id(response_info.json())
    downloaded_file = download_file(extracted_id["record_id"], extracted_id["file_id"])
    return downloaded_file


def download_file(id, id_file):

    download_info = get_download(id, id_file)
    download_response = requests.get(download_info["url"])

    with open(download_info["filename"], mode="wb") as file:
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


def extract_record_id_and_file_id(search_response):
    record_id = search_response["hits"]["hits"][0]["id"]
    file_id = search_response["hits"]["hits"][0]["files"][0]["id"]

    return {"record_id": record_id, "file_id": file_id}
