import requests

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return requests.get(url, params=params, headers=headers)

    def post(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return requests.post(url, data=data, json=json, headers=headers)

    def put(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return requests.put(url, data=data, json=json, headers=headers)

    def patch(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return requests.patch(url, data=data, json=json, headers=headers)

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return requests.delete(url, headers=headers)
