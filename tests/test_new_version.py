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
    obtained = get_latest_version_id(concept_rec_id)

    assert obtained == 200716


def test_create_draft_of_new_version():
    access_token = load_access_token()
    title = "Parámetros para calcular el sexo de Albatros de Laysan"
    latest_draft_link = search_deposition_by_title(title, is_sandbox=True)
    requests.delete(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})

    latest_version_id = 137021
    obtained = create_draft_of_new_version(latest_version_id)
    assert obtained.status_code == 201
    time.sleep(1)
    latest_draft_link = search_deposition_by_title(title, is_sandbox=True)
    requests.delete(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})


def test_upload_file_in_new_version():
    access_token = load_access_token()
    title = "Parámetros para calcular el sexo de Albatros de Laysan"
    latest_draft_link = search_deposition_by_title(title, is_sandbox=True)
    requests.delete(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})
    concept_rec_id = "131633"
    file_path = "tests/data/tests_file.txt"

    obtained = upload_file_in_new_version(concept_rec_id, file_path)
    assert obtained.status_code == 201
    time.sleep(1)
    latest_draft_link = search_deposition_by_title(title, is_sandbox=True)

    expected_number_of_files = 1
    response = requests.get(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})
    response_json = response.json()
    assert response_json["metadata"]["access_right"] == "restricted"
    obtained_number_of_files = len(response.json()["files"])
    assert obtained_number_of_files == expected_number_of_files
    requests.delete(latest_draft_link, headers={"Authorization": f"Bearer {access_token}"})


def test_publish_new_version():
    latest_version_id = 131633
    file_path = "tests/data/tests_file.txt"
    is_test = True
    obtained = publish_new_version(latest_version_id, file_path, is_test)
    assert obtained == "New version published"


@pytest.mark.skipif(
    os.getenv("GITHUB_ACTIONS") is not None, reason="Solo se ejecuta en GitHub Actions"
)
def test_live_publish_new_version():
    concept_rec_id = "200738"
    file_path = "tests/data/tests_file.txt"
    is_test = False
    obtained = publish_new_version(concept_rec_id, file_path, is_test)
    assert obtained.status_code == 202
