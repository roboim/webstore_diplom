import requests

response = requests.post(
    'http://127.0.0.1:8000/product/',
    json={'name': 'Продукт_клиента_1', 'category': 'тестовая категория', 'description': 'тестовое описание',
          'quantity': 2, 'price': 10}
)
print(response.status_code)
print(response.text)

