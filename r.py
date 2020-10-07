import requests

response = requests.post(
    'http://127.0.0.1:5000/auth',
    json={'login': 'admin', 'password': '12345'})

print(response.status_code)
