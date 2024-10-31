import requests
import os


def call_depositions():
    ACCESS_TOKEN = load_access_token()
    r = requests.get(
        "https://sandbox.zenodo.org/api/deposit/depositions", [("access_token", ACCESS_TOKEN)]
    )
    return r


def load_access_token():
    return os.environ.get("ACCESS_TOKEN")
