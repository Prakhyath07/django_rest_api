import requests


prod_id = input("What is the product id you want to delete? \n")

try:
    prod_id = int(prod_id)

except:
    prod_id = None
    print("Not a vaid id")


endpoint = f"http://127.0.0.1:8000/api/products/{prod_id}/delete/"

resp = requests.delete(endpoint)

print(resp.status_code, resp.status_code == 204)