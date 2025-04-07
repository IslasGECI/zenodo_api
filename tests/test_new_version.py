from zenodo_api.new_version import get_latest_version


def test_get_latest_version():
    concept_rec_id = "131633"
    obtained = get_latest_version(concept_rec_id)

    assert 200 <= obtained.status_code < 300
    assert obtained.json()["id"] == 137021
