import requests

response = requests.post(
    'http://127.0.0.1:8000/api/v1/products/',
    json={'name': 'Продукт_клиента_1'}
)
print(response.status_code)
print(response.text)

