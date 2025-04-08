from zenodo_api.new_version import create_draft_of_new_version, get_latest_version_id


def test_get_latest_version_id():
    concept_rec_id = "131633"
    obtained = get_latest_version_id(concept_rec_id)

    assert obtained == 137021


def test_create_draft_of_new_version():
    latest_version_id = 137021
    obtained = create_draft_of_new_version(latest_version_id)

    assert obtained.status_code == 201
