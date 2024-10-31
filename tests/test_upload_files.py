from zenodo_api.upload_files import call_depositions


def tests_call_depositions():
    obtained = call_depositions()
    assert obtained.status_code == 401
