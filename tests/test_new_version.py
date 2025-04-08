from zenodo_api.new_version import create_draft_of_new_version, get_latest_version_id
from zenodo_api.upload_files import load_access_token
from zenodo_api.retrieve import search_deposition_by_title

import requests


def test_get_latest_version_id():
    concept_rec_id = "131633"
    obtained = get_latest_version_id(concept_rec_id)

    assert obtained == 137021


def test_create_draft_of_new_version():
    access_token = load_access_token()
    latest_draft_link = search_deposition_by_title(
        '"Parámetros para calcular el sexo de Albatros de Laysan"', is_sandbox=True
    )
    requests.delete(latest_draft_link, params={"access_token": access_token})
    latest_version_id = 137021
    obtained = create_draft_of_new_version(latest_version_id)

    assert obtained.status_code == 201
