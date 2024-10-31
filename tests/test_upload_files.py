from zenodo_api.upload_files import (
    call_depositions,
    load_access_token,
    create_empty_upload,
    upload_new_file,
)


def tests_call_depositions():
    obtained = call_depositions()
    print(obtained)
    assert obtained.status_code == 200


def test_load_access_token():
    obtained = load_access_token()
    assert obtained is not None


def test_create_empty_upload():
    obtained = create_empty_upload()
    assert obtained.status_code == 201


def tests_upload_new_file():
    obtained = upload_new_file()
    assert obtained.status_code == 201
