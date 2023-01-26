import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title":"TV",
    "price" : 50000,
    # "content": " 50 inch"
}

resp = requests.post(endpoint, json=data)

print(resp.json())