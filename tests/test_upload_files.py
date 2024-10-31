from zenodo_api.upload_files import call_depositions, load_access_token

import os


def tests_call_depositions():
    obtained = call_depositions()
    assert obtained.status_code == 200


def test_load_access_token():
    obtained = load_access_token()
    assert obtained is not None
