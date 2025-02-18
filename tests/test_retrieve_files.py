from zenodo_api.retrieve import (
    download_file,
    extract_record_id_and_file_id,
    search_record_by_two_parameters,
    search_by_doi,
)
from zenodo_api.url_selector import url_selector
import geci_test_tools as gtt
import json


def tests_download_file():
    id = 124630
    id_file = "cf7efbaa-c355-43b1-a4bd-5cc236cce19d"
    output_file = "paper.pdf"
    gtt.if_exist_remove(output_file)
    url_api = url_selector(tests=True)
    obtained = download_file(id, id_file, url_api)
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

    url_api = url_selector(tests=True)
    obtained = search_record_by_two_parameters(title, creator, url_api)

    assert obtained.status_code == 200

    obtained_total_hits = obtained.json()["hits"]["total"]
    assert obtained_total_hits == 1

    creator = "Grupo de Ecología y Conservación de Islas"
    id = 131634
    url_api = url_selector(tests=True)
    obtained = search_record_by_two_parameters(id, creator, url_api)
    with open("data3.json", "w", encoding="utf-8") as f:
        json.dump(obtained.json(), f, ensure_ascii=False, indent=4)

    obtained_total_hits = obtained.json()["hits"]["total"]
    assert obtained_total_hits == 1


def tests_custom_search():
    url_api = "https://sandbox.zenodo.org/api"
    doi = "10.5072/zenodo.131633"
    obtained = search_by_doi(doi, url_api)
    assert obtained.status_code == 200
    obtained_total_hits = obtained.json()["hits"]["total"]
    assert obtained_total_hits == 1
