import requests

from getpass import getpass

endpoint = "http://127.0.0.1:8000/api/auth/"

password = getpass()

auth_resp = requests.post(endpoint, json={"username":'admin',"password": password})

if auth_resp.status_code ==200:
    token = auth_resp.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }

    endpoint = "http://127.0.0.1:8000/api/products/"

    get_resp = requests.get(endpoint, headers=headers)

    print(get_resp.json())