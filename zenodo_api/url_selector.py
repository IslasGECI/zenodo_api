def url_selector(tests=True):
    if tests == True:
        return "https://sandbox.zenodo.org/api"
    else:
        return "https://zenodo.org/api"
