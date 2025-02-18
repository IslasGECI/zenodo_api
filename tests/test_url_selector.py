from zenodo_api import url_selector


def test_url_selector():
    obtained = url_selector(tests=True)
    expected = "https://sandbox.zenodo.org/api"
    assert obtained == expected

    obtained = url_selector()
    expected = "https://zenodo.org/api"
    assert obtained == expected
