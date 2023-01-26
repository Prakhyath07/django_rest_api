import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update/"

data = {
    "title":"smartphone"
    
    }

resp = requests.put(endpoint, json=data)

print(resp.json())