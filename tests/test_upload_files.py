from zenodo_api.upload_files import (
    call_depositions,
    load_access_token,
    create_empty_upload,
    upload_new_file,
    upload_metadata,
)


def tests_call_depositions():
    obtained = call_depositions()
    assert obtained.status_code == 200


def test_load_access_token():
    obtained = load_access_token()
    assert obtained is not None


def test_create_empty_upload():
    obtained = create_empty_upload()
    assert obtained.status_code == 201


def tests_upload_new_file():
    file_path = "tests/data/tests_file.txt"
    obtained = upload_new_file(file_path)
    assert obtained.status_code == 201


def tests_upload_metadata():
    data_dict = {
        "metadata": {
            "title": "My first upload",
            "upload_type": "poster",
            "description": "This is my first upload",
            "creators": [{"name": "Doe, John", "affiliation": "Zenodo"}],
        }
    }
    obtained = upload_metadata(data_dict)
    assert obtained.status_code == 200
