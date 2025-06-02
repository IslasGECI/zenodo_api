import json
import requests
import time

from zenodo_api.upload_files import (
    call_depositions,
    load_access_token,
    create_deposition_in_new_record,
    upload_file_in_new_record,
    xxupload_metadata_in_new_record,
)
from zenodo_api.retrieve import search_deposition_by_title
import re


def tests_call_depositions():
    obtained = call_depositions(is_sandbox=True)
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(obtained.json(), f, ensure_ascii=False, indent=4)
    assert obtained.status_code == 200


def test_load_access_token():
    obtained = load_access_token()
    assert obtained is not None


def test_create_empty_upload():
    obtained = create_deposition_in_new_record(is_sandbox=True)
    assert obtained.status_code == 201


def tests_upload_new_file():
    file_path = "tests/data/tests_file.txt"
    obtained = upload_file_in_new_record(file_path, is_sandbox=True)
    assert obtained["response_upload"].status_code == 201
    assert "latest_draft" in obtained.keys()

    latest_draft_link = obtained["latest_draft"]
    time.sleep(1)
    response = requests.delete(
        latest_draft_link, headers={"Authorization": f"Bearer {load_access_token()}"}
    )
    assert response.status_code == 204


def tests_upload_metadata():
    title = "GECI first upload"
    data_dict = {
        "metadata": {
            "title": title,
            "upload_type": "poster",
            "description": "This is my first upload",
        }
    }
    obtained = xxupload_metadata_in_new_record(data_dict, is_sandbox=True)
    assert obtained.status_code == 200

    obtained_json = obtained.json()
    assert (
        "Grupo de Ecología y Conservación de Islas"
        in obtained_json["metadata"]["creators"][0]["name"]
    )

    pattern = re.compile("^2[0-9]{3}-")
    date = obtained_json["metadata"]["publication_date"]
    is_date = bool(pattern.match(date))
    assert is_date

    assert obtained_json["metadata"]["access_right"] == "open"
    time.sleep(1)
    access_token = load_access_token()
    latest_draft_link = search_deposition_by_title(title, is_sandbox=True)

    requests.delete(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})
