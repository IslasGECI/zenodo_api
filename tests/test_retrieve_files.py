from zenodo_api.retrieve import retrieve_file

import geci_test_tools as gtt


def tests_retrieve_file():
    id = 124630
    id_file = "cf7efbaa-c355-43b1-a4bd-5cc236cce19d"
    output_file = "paper.pdf"
    gtt.if_exist_remove(output_file)
    obtained = retrieve_file(id, id_file)
    assert obtained.status_code == 200
    gtt.assert_exist(output_file)
