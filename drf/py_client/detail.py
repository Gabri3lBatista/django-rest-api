import requests

endpoint = 'http://localhost:8000/api/products/1/' # URL do endpoint da API

get_response = requests.get(endpoint) # Fazendo uma requisição GET para o endpoint
print(get_response.status_code) # Imprimindo o status da resposta
print(get_response.json()) # Imprimindo o conteúdo da resposta em formato JSON