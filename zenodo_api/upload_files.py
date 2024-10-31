import requests
import os


def call_depositions():
    r = requests.get("https://zenodo.org/api/deposit/depositions")
    return r


def load_access_token():
    return os.environ.get("ACCESS_TOKEN")
