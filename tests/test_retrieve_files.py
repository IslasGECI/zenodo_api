from zenodo_api.retrieve import download_file, download_from_filename, search_record_by_title

import geci_test_tools as gtt
import pytest


def tests_download_file():
    id = 124630
    id_file = "cf7efbaa-c355-43b1-a4bd-5cc236cce19d"
    output_file = "paper.pdf"
    gtt.if_exist_remove(output_file)
    obtained = download_file(id, id_file)
    assert obtained.status_code == 200
    gtt.assert_exist(output_file)


@pytest.mark.skip(reason="not yet 🪙")
def tests_download_from_filename():
    id = 124630
    output_file = "China_2004-es.pdf"
    gtt.if_exist_remove(output_file)
    obtained = download_from_filename(id, output_file)
    assert obtained.status_code == 200
    gtt.assert_exist(output_file)


def tests_search_record_by_title():
    title = "Prueba"
    obtained = search_record_by_title(title)
    assert obtained.status_code == 200
