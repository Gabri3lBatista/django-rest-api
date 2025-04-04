import requests

endpoint = "http://localhost:8000/api/products/"



response = requests.post(endpoint)

print(response.json())