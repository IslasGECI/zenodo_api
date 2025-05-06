from zenodo_api.new_version import (
    create_draft_of_new_version,
    get_latest_version_id,
    upload_file_in_new_version,
    publish_new_version,
)
from zenodo_api.upload_files import load_access_token
from zenodo_api.retrieve import search_deposition_by_title

import requests
import time
import os
import pytest


def test_get_latest_version_id():
    concept_rec_id = "131633"
    is_sandbox = True
    obtained = get_latest_version_id(concept_rec_id, is_sandbox)

    assert obtained == 200716


def test_create_draft_of_new_version():
    access_token = load_access_token()
    title = "Parámetros para calcular el sexo de Albatros de Laysan"
    latest_draft_link = search_deposition_by_title(title, is_sandbox=True)
    requests.delete(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})

    latest_version_id = 137021
    obtained = create_draft_of_new_version(latest_version_id, is_sandbox=True)
    assert obtained.status_code == 201
    time.sleep(1)
    latest_draft_link = search_deposition_by_title(title, is_sandbox=True)
    requests.delete(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})


def test_upload_file_in_new_version():
    access_token = load_access_token()
    title = "Parámetros para calcular el sexo de Albatros de Laysan"
    is_sandbox = True
    latest_draft_link = search_deposition_by_title(title, is_sandbox)
    requests.delete(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})
    concept_rec_id = "131633"
    file_path = "tests/data/tests_file.txt"

    obtained = upload_file_in_new_version(concept_rec_id, file_path, is_sandbox)
    assert obtained.status_code == 201
    time.sleep(1)
    latest_draft_link = search_deposition_by_title(title, is_sandbox)

    expected_number_of_files = 1
    response = requests.get(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})
    response_json = response.json()
    obtained_number_of_files = len(response_json["files"])
    assert obtained_number_of_files == expected_number_of_files
    requests.delete(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})


@pytest.mark.skipif(os.getenv("GITHUB_ACTIONS") is None, reason="Solo se ejecuta en GitHub Actions")
def test_live_publish_new_version():
    concept_rec_id = "200738"
    file_path = "tests/data/tests_file.txt"
    is_test = True
    obtained = publish_new_version(concept_rec_id, file_path, is_test)
    assert obtained.status_code == 202
