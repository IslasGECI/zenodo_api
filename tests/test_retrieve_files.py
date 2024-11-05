from zenodo_api.retrieve import retrieve_file


def tests_retrieve_file():
    id = 124630
    id_file = "cf7efbaa-c355-43b1-a4bd-5cc236cce19d"
    obtained = retrieve_file(id, id_file)
    assert obtained.status_code == 200
