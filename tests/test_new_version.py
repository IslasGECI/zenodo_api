from zenodo_api.new_version import get_latest_version


def test_get_latest_version():
    record_id = "137021"
    obtained = get_latest_version(record_id)
    assert 200 <= obtained.status_code < 300
