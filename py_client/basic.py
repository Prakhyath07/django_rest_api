import requests


## returns a html 
# endpoint = "https://httpbin.org"
# resp = requests.get(endpoint)
# print(resp.text)


# endpoint = "https://httpbin.org/status/200"


## returns a json(with .text) which on using .json() returns python dictionary
# endpoint = "https://httpbin.org/anything"

# sample_output_for_ref = {'args': {}, 'data': '{"query": "hello"}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '18', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.2', 'X-Amzn-Trace-Id': 'Root=1-63d1258d-067e6dc3210d63565363fd2f'}, 'json': {'query': 'hello'}, 'method': 'GET', 'origin': '124.40.247.101', 'url': 'https://httpbin.org/anything'}

# # resp = requests.get(endpoint) ## returns dictionary with data : {}
# # resp = requests.get(endpoint, json={"query": "hello"}) ## returns dictionary with data : {{"query": "hello"}}
# resp = requests.get(endpoint, data={"query": "hello"}) ## returns dictionary with form : {{"query": "hello"}}

# print(resp.json())




endpoint = "http://localhost:8000/api"


resp = requests.get(endpoint) 

print(resp.json()['message'])
print(resp.status_code)
