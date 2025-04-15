import json
import requests
import time

from zenodo_api.upload_files import (
    call_depositions,
    load_access_token,
    create_deposition_in_new_record,
    upload_file_in_new_record,
    upload_metadata,
)
from zenodo_api.retrieve import search_deposition_by_title


def tests_call_depositions():
    obtained = call_depositions()
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(obtained.json(), f, ensure_ascii=False, indent=4)
    assert obtained.status_code == 200


def test_load_access_token():
    obtained = load_access_token()
    assert obtained is not None


def test_create_empty_upload():
    obtained = create_deposition_in_new_record()
    assert obtained.status_code == 201


def tests_upload_new_file():
    file_path = "tests/data/tests_file.txt"
    obtained = upload_file_in_new_record(file_path)
    assert obtained["response_upload"].status_code == 201
    assert "latest_draft" in obtained.keys()

    latest_draft_link = obtained["latest_draft"]
    time.sleep(1)
    response = requests.delete(latest_draft_link, params={"access_token": load_access_token()})
    assert response.status_code == 204


def tests_upload_metadata():
    title = "GECI first upload"
    data_dict = {
        "metadata": {
            "title": title,
            "upload_type": "poster",
            "description": "This is my first upload",
            "creators": [{"name": "Doe, John", "affiliation": "Zenodo"}],
        }
    }
    obtained = upload_metadata(data_dict)
    assert obtained.status_code == 200

    time.sleep(1)
    access_token = load_access_token()
    latest_draft_link = search_deposition_by_title(title, is_sandbox=True)
    requests.delete(latest_draft_link, params={"access_token": access_token})
