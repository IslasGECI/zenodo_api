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


def create_empty_upload():
    headers = {"Content-Type": "application/json"}
    params = {"access_token": load_access_token()}
    r = requests.post(
        "https://sandbox.zenodo.org/api/deposit/depositions",
        params=params,
        json={},
        headers=headers,
    )
    return r
