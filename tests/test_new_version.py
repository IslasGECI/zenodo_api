from zenodo_api.new_version import create_draft_of_new_version, get_latest_version_id
from zenodo_api.upload_files import load_access_token

import requests


def test_get_latest_version_id():
    concept_rec_id = "131633"
    obtained = get_latest_version_id(concept_rec_id)

    assert obtained == 137021


def test_create_draft_of_new_version():
    access_token = load_access_token()
    deposition_search = requests.get(
        "https://sandbox.zenodo.org/api/deposit/depositions",
        params={"q": "albatros", "access_token": access_token},
    )
    latest_draft_id = deposition_search.json()[0]["links"]["latest_draft"]
    requests.delete(latest_draft_id, params={"access_token": access_token})
    latest_version_id = 137021
    obtained = create_draft_of_new_version(latest_version_id)

    assert obtained.status_code == 201
