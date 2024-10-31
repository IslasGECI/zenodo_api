from zenodo_api.upload_files import call_depositions, load_access_token


def tests_call_depositions():
    obtained = call_depositions()
    assert obtained.status_code == 403
    assert obtained.json()["message"] == "Permission denied."


def test_load_access_token():
    obtained = load_access_token()
    assert obtained is not None
