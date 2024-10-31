import requests


def call_depositions():
    r = requests.get("https://zenodo.org/api/deposit/depositions")
    return r
