from zenodo_api.retrieve import (
    download_file,
    download_from_filename,
    extract_record_id_and_file_id,
    retrieve_file_info,
    search_record_by_title,
)

import geci_test_tools as gtt
import pytest
import json


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


def test_extract_record_id_and_file_id():
    response_file = "tests/data/search_by_query_response.json"
    with open(response_file, "r") as file:
        search_response = json.load(file)
    obtained = extract_record_id_and_file_id(search_response)

    expected_record_id = 128040
    assert obtained["record_id"] == expected_record_id

    expected_file_id = "60efcb0a-501b-432d-814a-d29d7716a492"
    assert obtained["file_id"] == expected_file_id


def tests_search_record_by_title():
    title = "Prueba"
    creator = "villlasante"

    obtained = search_record_by_title(title, creator)

    assert obtained.status_code == 200

    obtained_total_hits = obtained.json()["hits"]["total"]
    assert obtained_total_hits == 1

    creator = "xx"
    obtained = search_record_by_title(title, creator)

    with open("data2.json", "w", encoding="utf-8") as f:
        json.dump(obtained.json(), f, ensure_ascii=False, indent=4)

    obtained_total_hits = obtained.json()["hits"]["total"]
    assert obtained_total_hits == 0
